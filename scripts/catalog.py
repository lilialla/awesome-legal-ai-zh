#!/usr/bin/env python3
"""Build and validate the awesome-legal-ai-zh V2 catalog.

The script uses only the Python standard library and the authenticated `gh`
CLI. It stores reviewable metadata, never repository contents or credentials.
"""

from __future__ import annotations

import argparse
import base64
import copy
import datetime as dt
import hashlib
import html
import io
import itertools
import json
import os
import re
import subprocess
import sys
import tempfile
import time
import urllib.error
import urllib.parse
import urllib.request
import zipfile
from collections import Counter, defaultdict
from concurrent.futures import ThreadPoolExecutor, as_completed
from pathlib import Path
from typing import Iterable


SCHEMA_VERSION = 2
REVIEW_DEPTHS = {"metadata", "repo_read", "smoke", "tested"}
REVIEW_RANK = {"metadata": 0, "repo_read": 1, "smoke": 2, "tested": 3}
SCOPES = {"core", "support", "adjacent"}
KINDS = {"suite", "skill", "mcp", "app", "tool", "dataset", "model", "resource", "platform"}
RECOMMENDATIONS = {"primary", "alternative", "indexed", "watch", "retired"}
SOURCE_GRADES = {"verified", "platform_found", "unverified"}
DATA_PATHS = {"local", "self_hosted", "external_api", "mixed", "unknown", "not_applicable"}
SETUP_MODES = {"install", "config", "cli", "self_host", "reference"}
SETUP_DIFFICULTIES = {"ready", "account_required", "technical", "reference"}
RELATION_TYPES = {"fork_of", "contained_in", "near_duplicate_of", "redirected_from"}

CORE_CATEGORIES = {
    "skill-suite",
    "contract-doc-ip",
    "antitrust-competition",
    "cross-border-arbitration",
    "corp-finance-ma-dd",
    "data-compliance",
    "retrieval-mcp",
    "enterprise-check",
    "criminal-admin-exec",
    "labor-family-personal",
    "tax-bankruptcy-realestate",
    "law-firm-mgmt",
}
ADJACENT_CATEGORIES = {"media-ip", "ppt-assets", "tech-foundation"}

CATEGORY_CAPABILITY = {
    "skill-suite": "starter-suites",
    "contract-doc-ip": "contracts",
    "antitrust-competition": "ip-competition",
    "cross-border-arbitration": "cross-border-arbitration",
    "corp-finance-ma-dd": "corporate-ma",
    "data-compliance": "data-compliance",
    "retrieval-mcp": "legal-research",
    "enterprise-check": "enterprise-dd",
    "criminal-admin-exec": "litigation",
    "labor-family-personal": "labor-family",
    "tax-bankruptcy-realestate": "tax-bankruptcy-realestate",
    "law-firm-mgmt": "law-firm-operations",
    "dataset-infra": "datasets-models",
    "llm": "datasets-models",
    "awesome": "supporting-resources",
    "intl-tools": "supporting-resources",
    "media-ip": "adjacent-resources",
    "ppt-assets": "adjacent-resources",
    "tech-foundation": "adjacent-resources",
}

CAPABILITY_TITLES = {
    "starter-suites": "综合套件",
    "contracts": "合同审查与红线",
    "legal-documents": "法律文书与 OCR",
    "legal-research": "法规与案例检索",
    "litigation": "诉讼、证据与期限",
    "enterprise-dd": "企业核查与尽调",
    "corporate-ma": "公司、投融资与并购",
    "data-compliance": "数据合规与脱敏",
    "labor-family": "劳动、家事与个人权益",
    "ip-competition": "知识产权与竞争法",
    "cross-border-arbitration": "涉外与仲裁",
    "law-firm-operations": "律所与案件运营",
    "tax-bankruptcy-realestate": "税务、破产与房地产",
    "datasets-models": "数据集、模型与评测",
    "supporting-resources": "法律资源导航",
    "adjacent-resources": "辅助与相邻资源",
}

KIND_LABELS = {
    "suite": "套件",
    "skill": "Skill",
    "mcp": "MCP",
    "app": "应用",
    "tool": "工具",
    "dataset": "数据/评测",
    "model": "模型",
    "resource": "资源",
    "platform": "平台",
}
DIFFICULTY_LABELS = {
    "ready": "直接安装",
    "account_required": "需账号/API",
    "technical": "需部署",
    "reference": "资料参考",
}
DATA_PATH_LABELS = {
    "local": "本地",
    "self_hosted": "自托管",
    "external_api": "外部 API",
    "mixed": "本地+联网",
    "unknown": "未明确",
    "not_applicable": "不适用",
}
DEPTH_LABELS = {
    "metadata": "元数据核验",
    "repo_read": "仓库审阅",
    "smoke": "Smoke 通过",
    "tested": "测试通过",
}
RECOMMENDATION_LABELS = {
    "primary": "当前推荐",
    "alternative": "关键备选",
    "indexed": "已索引",
    "watch": "观察",
    "retired": "退役",
}

SECRET_PATTERN = re.compile(
    r"(?:github_pat_[A-Za-z0-9_]{20,}|gh[opsu]_[A-Za-z0-9]{20,}|"
    r"AKIA[0-9A-Z]{16}|-----BEGIN (?:[A-Z0-9-]+ )?PRIVATE KEY-----)"
)
URL_PATTERN = re.compile(r"github\.com/([A-Za-z0-9_.-]+/[A-Za-z0-9_.-]+)")
REPO_ID_PATTERN = re.compile(r"^[A-Za-z0-9_.-]+/[A-Za-z0-9_.-]+$")
SLUG_PATTERN = re.compile(r"^[a-z0-9]+(?:-[a-z0-9]+)*$")
MAX_ARCHIVE_BYTES = 200 * 1024 * 1024
MAX_ARCHIVE_MEMBERS = 100_000
MAX_SKILL_BYTES = 2 * 1024 * 1024
MAX_SKILL_TOTAL_BYTES = 128 * 1024 * 1024


class CatalogError(RuntimeError):
    pass


def load_json(path: Path) -> dict:
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except FileNotFoundError as exc:
        raise CatalogError(f"missing catalog file: {path}") from exc
    except json.JSONDecodeError as exc:
        raise CatalogError(f"invalid JSON in {path}: {exc}") from exc


def dump_json(path: Path, value: dict) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    payload = json.dumps(value, ensure_ascii=False, indent=2) + "\n"
    mode = path.stat().st_mode & 0o777 if path.exists() else 0o644
    temporary_path: Path | None = None
    try:
        with tempfile.NamedTemporaryFile(
            mode="w",
            encoding="utf-8",
            dir=path.parent,
            prefix=f".{path.name}.",
            suffix=".tmp",
            delete=False,
        ) as handle:
            temporary_path = Path(handle.name)
            handle.write(payload)
            handle.flush()
            os.fsync(handle.fileno())
        os.chmod(temporary_path, mode)
        os.replace(temporary_path, path)
    finally:
        if temporary_path is not None:
            temporary_path.unlink(missing_ok=True)


def utc_now() -> str:
    return dt.datetime.now(dt.timezone.utc).replace(microsecond=0).isoformat().replace("+00:00", "Z")


def today() -> str:
    return dt.date.today().isoformat()


def project_map(projects_doc: dict) -> dict[str, dict]:
    return {project["id"]: project for project in projects_doc["projects"]}


def metadata_for(project_id: str, metadata_doc: dict) -> dict:
    return metadata_doc.get("repositories", {}).get(project_id, {})


def _require(value: bool, message: str) -> None:
    if not value:
        raise CatalogError(message)


def validate_data(
    projects_doc: dict,
    metadata_doc: dict,
    curation_doc: dict,
    platforms_doc: dict,
    *,
    require_primary_review: bool = True,
) -> None:
    for name, document in (
        ("projects", projects_doc),
        ("metadata", metadata_doc),
        ("curation", curation_doc),
        ("platform resources", platforms_doc),
    ):
        _require(document.get("schema_version") == SCHEMA_VERSION, f"{name} schema_version must be 2")

    projects = projects_doc.get("projects")
    _require(isinstance(projects, list), "projects must be a list")
    ids = [project.get("id") for project in projects]
    duplicates = sorted({project_id for project_id in ids if ids.count(project_id) > 1})
    _require(not duplicates, f"duplicate project id: {', '.join(duplicates)}")
    _require(
        all(isinstance(project_id, str) and REPO_ID_PATTERN.fullmatch(project_id) for project_id in ids),
        "invalid project id",
    )

    capability_items = curation_doc.get("capabilities", [])
    capability_ids = [item.get("id") for item in capability_items]
    _require(len(capability_ids) == len(set(capability_ids)), "duplicate capability id")
    _require(
        all(isinstance(item, str) and SLUG_PATTERN.fullmatch(item) for item in capability_ids),
        "invalid capability id",
    )
    capabilities = set(capability_ids)
    all_capabilities = capabilities | {"datasets-models", "supporting-resources", "adjacent-resources"}
    required = {
        "id",
        "aliases",
        "source",
        "url",
        "name",
        "scope",
        "kind",
        "primary_capability",
        "capabilities",
        "jurisdictions",
        "summary",
        "setup",
        "data_path",
        "recommendation",
        "selection_reason",
        "cautions",
        "relationships",
        "source_grade",
        "review",
    }
    for project in projects:
        missing = required - project.keys()
        _require(not missing, f"{project.get('id')}: missing fields {sorted(missing)}")
        for field in ("name", "summary", "selection_reason"):
            _require(isinstance(project[field], str), f"{project['id']}: {field} must be a string")
        for field in ("aliases", "capabilities", "jurisdictions", "cautions", "relationships"):
            _require(isinstance(project[field], list), f"{project['id']}: {field} must be a list")
        for field in ("aliases", "capabilities", "jurisdictions", "cautions"):
            _require(
                all(isinstance(item, str) for item in project[field]),
                f"{project['id']}: {field} entries must be strings",
            )
        _require(bool(project["capabilities"]), f"{project['id']}: capabilities must not be empty")
        _require(
            set(project["capabilities"]) <= all_capabilities,
            f"{project['id']}: unknown capability in capabilities",
        )
        _require(project["url"] == f"https://github.com/{project['id']}", f"{project['id']}: invalid GitHub URL")
        _require(project["scope"] in SCOPES, f"{project['id']}: invalid scope")
        _require(project["kind"] in KINDS, f"{project['id']}: invalid kind")
        _require(project["recommendation"] in RECOMMENDATIONS, f"{project['id']}: invalid recommendation")
        _require(project["source_grade"] in SOURCE_GRADES, f"{project['id']}: invalid source grade")
        _require(project["data_path"] in DATA_PATHS, f"{project['id']}: invalid data path")
        _require(project["primary_capability"] in all_capabilities, f"{project['id']}: unknown primary capability")
        _require(project["primary_capability"] in project["capabilities"], f"{project['id']}: primary capability missing from capabilities")
        setup = project["setup"]
        _require(isinstance(setup, dict), f"{project['id']}: setup must be an object")
        _require(setup.get("mode") in SETUP_MODES, f"{project['id']}: invalid setup mode")
        _require(setup.get("difficulty") in SETUP_DIFFICULTIES, f"{project['id']}: invalid setup difficulty")
        _require(isinstance(setup.get("services"), list), f"{project['id']}: setup services must be a list")
        _require(
            all(isinstance(item, str) for item in setup["services"]),
            f"{project['id']}: setup services entries must be strings",
        )
        review = project["review"]
        _require(isinstance(review, dict), f"{project['id']}: review must be an object")
        _require(review.get("depth") in REVIEW_DEPTHS, f"{project['id']}: invalid review depth")
        _require(bool(review.get("reviewed_at")), f"{project['id']}: missing review date")
        _require(
            isinstance(review.get("evidence"), list)
            and bool(review["evidence"])
            and all(isinstance(item, str) for item in review["evidence"]),
            f"{project['id']}: review evidence must be a non-empty string list",
        )
        _require(isinstance(review.get("signals"), dict), f"{project['id']}: review signals must be an object")
        for relation in project["relationships"]:
            _require(isinstance(relation, dict), f"{project['id']}: relationship must be an object")
            _require(relation.get("type") in RELATION_TYPES, f"{project['id']}: invalid relationship")
            _require(
                isinstance(relation.get("target"), str)
                and REPO_ID_PATTERN.fullmatch(relation["target"]),
                f"{project['id']}: invalid relationship target",
            )
            _require(
                isinstance(relation.get("evidence"), str) and bool(relation["evidence"]),
                f"{project['id']}: relationship evidence is required",
            )
        serialized = json.dumps(project, ensure_ascii=False)
        _require(not SECRET_PATTERN.search(serialized), f"{project['id']}: possible secret in registry")

    metadata = metadata_doc.get("repositories")
    _require(isinstance(metadata, dict), "metadata repositories must be an object")
    _require(set(metadata) == set(ids), "metadata project ids must exactly match projects")
    for project_id, item in metadata.items():
        _require(isinstance(item, dict), f"{project_id}: metadata must be an object")
        for field in ("accessible", "archived", "disabled", "fork"):
            _require(isinstance(item.get(field), bool), f"{project_id}: metadata {field} must be boolean")
        _require(
            isinstance(item.get("canonical_id"), str)
            and REPO_ID_PATTERN.fullmatch(item["canonical_id"]),
            f"{project_id}: invalid canonical id",
        )

    slots = curation_doc.get("slots", [])
    slot_ids = [slot.get("id") for slot in slots]
    _require(len(slot_ids) == len(set(slot_ids)), "duplicate slot id")
    _require(
        all(isinstance(item, str) and SLUG_PATTERN.fullmatch(item) for item in slot_ids),
        "invalid slot id",
    )
    for slot in slots:
        _require(slot.get("capability") in capabilities, f"{slot.get('id')}: unknown capability")
        _require(bool(slot.get("decision_basis")), f"{slot.get('id')}: decision basis is required")
        alternatives = slot.get("alternatives", [])
        _require(len(alternatives) <= 2, f"{slot.get('id')}: at most two alternatives are allowed")
        selections = ([] if slot.get("primary") is None else [slot["primary"]]) + alternatives
        selected_ids = [selection.get("project") for selection in selections]
        _require(len(selected_ids) == len(set(selected_ids)), f"{slot.get('id')}: duplicate selection")
        for selection in selections:
            _require(isinstance(selection, dict), f"{slot.get('id')}: selection must be an object")
            selected_id = selection.get("project")
            _require(selected_id in ids, f"{slot.get('id')}: unknown selected project {selected_id}")
            _require(bool(selection.get("reason")), f"{slot.get('id')}: selection reason is required")
            _require(
                slot["capability"] in project_map(projects_doc)[selected_id]["capabilities"],
                f"{slot.get('id')}: selected project {selected_id} lacks task capability",
            )
            selected_metadata = metadata[selected_id]
            _require(
                selected_metadata["accessible"]
                and not selected_metadata["archived"]
                and not selected_metadata["disabled"],
                f"{slot.get('id')}: selected project {selected_id} is unavailable or retired",
            )
        if slot.get("primary") and require_primary_review:
            primary_id = slot["primary"]["project"]
            depth = project_map(projects_doc)[primary_id]["review"]["depth"]
            _require(
                REVIEW_RANK[depth] >= REVIEW_RANK["repo_read"],
                f"primary project {primary_id} must reach repo_read",
            )

    creators = curation_doc.get("featured_creators", [])
    creator_ids = [creator.get("id") for creator in creators]
    _require(len(creator_ids) == len(set(creator_ids)), "duplicate featured creator id")
    _require(
        all(isinstance(item, str) and SLUG_PATTERN.fullmatch(item) for item in creator_ids),
        "invalid featured creator id",
    )
    for creator in creators:
        creator_projects = creator.get("projects", [])
        _require(1 <= len(creator_projects) <= 6, f"{creator.get('id')}: feature one to six projects")
        _require(
            len(creator_projects) == len(set(creator_projects)),
            f"{creator.get('id')}: duplicate featured project",
        )
        _require(
            all(project_id in ids for project_id in creator_projects),
            f"{creator.get('id')}: unknown featured project",
        )
        _require(bool(creator.get("name")), f"{creator.get('id')}: creator name is required")
        _require(bool(creator.get("reason")), f"{creator.get('id')}: creator reason is required")
        _require(bool(creator.get("boundary")), f"{creator.get('id')}: creator boundary is required")
        _require(bool(creator.get("coverage")), f"{creator.get('id')}: creator coverage is required")

    homepage_projects = set()
    for slot in curation_doc.get("slots", []):
        if not slot.get("homepage"):
            continue
        if slot.get("primary"):
            homepage_projects.add(slot["primary"]["project"])
        homepage_projects.update(item["project"] for item in slot.get("alternatives", []))
    for creator in creators:
        homepage_projects.update(creator["projects"])
    _require(len(homepage_projects) <= 40, "homepage may feature at most 40 projects")

    resources = platforms_doc.get("resources")
    _require(isinstance(resources, list), "platform resources must be a list")
    for resource in resources:
        _require(resource.get("source_grade") in {"platform_found", "unverified"}, "platform source grade is invalid")
        parsed_url = urllib.parse.urlparse(resource.get("url", ""))
        _require(
            parsed_url.scheme == "https"
            and bool(parsed_url.netloc)
            and not re.search(r"[\x00-\x20]", resource.get("url", "")),
            "platform URL must use HTTPS",
        )
        serialized = json.dumps(resource, ensure_ascii=False)
        _require(not SECRET_PATTERN.search(serialized), "possible secret in platform registry")


def render_seed(projects_doc: dict) -> str:
    lines = [
        "# Generated by scripts/catalog.py build. Do not edit by hand.",
        "# owner/repo<TAB>legacy-category",
    ]
    for project in sorted(projects_doc["projects"], key=lambda item: item["id"].lower()):
        lines.append(f"{project['id']}\t{project.get('legacy_category', 'uncategorized')}")
    return "\n".join(lines) + "\n"


def _repo_link(project: dict) -> str:
    return f"[{project['id']}]({project['url']})"


def _cell(value: object) -> str:
    text = re.sub(r"\s+", " ", str(value)).strip()
    text = html.escape(text, quote=False)
    return text.replace("[", "&#91;").replace("]", "&#93;").replace("|", "\\|")


def _services(project: dict) -> str:
    services = project["setup"].get("services", [])
    return "、".join(services) if services else "无特定平台"


def _license(metadata: dict) -> str:
    return metadata.get("license_spdx") or "未识别"


def _date(value: str | None) -> str:
    return value[:10] if value else "未知"


def _snapshot_date(projects_doc: dict, metadata_doc: dict) -> str:
    refreshed = metadata_doc.get("refreshed_at", "")
    if re.match(r"^\d{4}-\d{2}-\d{2}", refreshed):
        return refreshed[:10]
    reviewed = [
        project.get("review", {}).get("reviewed_at", "")
        for project in projects_doc.get("projects", [])
    ]
    valid = [value[:10] for value in reviewed if re.match(r"^\d{4}-\d{2}-\d{2}", value)]
    return max(valid, default="unknown")


def _effective_statuses(curation_doc: dict) -> dict[str, str]:
    statuses: dict[str, str] = {}
    for slot in curation_doc.get("slots", []):
        if slot.get("primary"):
            statuses[slot["primary"]["project"]] = "primary"
        for alternative in slot.get("alternatives", []):
            statuses.setdefault(alternative["project"], "alternative")
    return statuses


def _task_contexts(curation_doc: dict) -> dict[str, list[str]]:
    contexts: dict[str, list[str]] = defaultdict(list)
    for slot in curation_doc.get("slots", []):
        if slot.get("primary"):
            contexts[slot["primary"]["project"]].append(f"{slot['title']}（当前推荐）")
        for alternative in slot.get("alternatives", []):
            contexts[alternative["project"]].append(f"{slot['title']}（关键备选）")
    return contexts


def _stats(projects_doc: dict, curation_doc: dict) -> dict[str, int]:
    statuses = _effective_statuses(curation_doc)
    projects = projects_doc["projects"]
    return {
        "indexed": len(projects),
        "reviewed": sum(REVIEW_RANK[item["review"]["depth"]] >= REVIEW_RANK["repo_read"] for item in projects),
        "tested": sum(item["review"]["depth"] in {"smoke", "tested"} for item in projects),
        "primary": sum(status == "primary" for status in statuses.values()),
        "homepage_tasks": sum(bool(item.get("homepage")) for item in curation_doc.get("slots", [])),
        "capabilities": len(curation_doc.get("capabilities", [])),
    }


def _capability_pool_size(projects_doc: dict, capability: str) -> int:
    return sum(
        project["scope"] == "core" and capability in project["capabilities"]
        for project in projects_doc["projects"]
    )


def _selection_link(selection: dict, projects: dict[str, dict], *, include_reason: bool) -> str:
    project = projects[selection["project"]]
    link = _repo_link(project)
    if not include_reason:
        return link
    return f"{link}：{_cell(selection['reason'])}"


def render_readme(projects_doc: dict, metadata_doc: dict, curation_doc: dict, platforms_doc: dict) -> str:
    projects = project_map(projects_doc)
    stats = _stats(projects_doc, curation_doc)
    snapshot = _snapshot_date(projects_doc, metadata_doc)
    lines = [
        '<div align="center">',
        "",
        '<picture><source media="(prefers-color-scheme: light)" srcset="assets/logo-light.svg"><img src="assets/logo.svg" width="96" alt="awesome-legal-ai-zh"></picture>',
        "",
        "# awesome-legal-ai-zh · 法律 AI 选型指南",
        "",
        f"![Indexed](https://img.shields.io/badge/完整索引-{stats['indexed']}_仓-3a5a8c) ![Reviewed](https://img.shields.io/badge/仓库审阅-{stats['reviewed']}-2e8b57) ![Tasks](https://img.shields.io/badge/首页任务-{stats['homepage_tasks']}-b5462f) ![Updated](https://img.shields.io/badge/快照-{snapshot.replace('-', '--')}-6b7280)",
        "",
        "**给个人律师和法务的开源法律 AI 选型入口：先看任务，再看上手门槛、数据路径、外部依赖和核验深度。**",
        "",
        "</div>",
        "",
        "本页只展示经过策展的法律核心入口。全部 GitHub 项目见 [完整索引](docs/CATALOG.md)，同类项目差异和能力缺口见 [能力地图](docs/CAPABILITIES.md)。",
        "",
        "## 怎么看",
        "",
        "- **当前推荐**是编辑判断，不是客观“最好”或综合分；每个具体任务最多一个当前推荐。",
        "- **能力池**是已审阅且标记为该大类的法律核心项目数；具体任务只在其中比较真正可替代的项目。",
        "- **数据路径**只描述项目公开实现：本地、自托管、外部 API、混合或未明确，不等同于安全背书。",
        "- **核验深度**分为元数据核验、仓库审阅、Smoke 通过和测试通过；Star 不参与推荐排序。",
        "- **测试通过**只说明指定工程测试在记录环境中运行成功，不证明法条、金额或法律结论正确。",
        "- License 和权利限制保留在完整索引，不再占用首页主列。",
        "",
        "## 按任务选工具",
        "",
        "| 具体任务 | 当前推荐 | 关键备选 | 上手 | 数据路径 | 外部依赖 | 能力池 | 核验 | 选择理由 |",
        "|---|---|---|---|---|---|---:|---|---|",
    ]
    slots = sorted(
        (slot for slot in curation_doc["slots"] if slot.get("homepage")),
        key=lambda slot: slot.get("order", 999),
    )
    for slot in slots:
        alternatives = "<br>".join(
            _selection_link(selection, projects, include_reason=True)
            for selection in slot.get("alternatives", [])
        ) or "-"
        pool_size = _capability_pool_size(projects_doc, slot["capability"])
        if not slot.get("primary"):
            lines.append(
                f"| {_cell(slot['title'])} | 暂无 | {alternatives} | - | - | - | {pool_size} 项 | - | {_cell(slot.get('gap') or slot['decision_basis'])} |"
            )
            continue
        selection = slot["primary"]
        project = projects[selection["project"]]
        lines.append(
            "| {task} | {repo} | {alternatives} | {difficulty} | {data_path} | {services} | {pool} 项 | {depth} | {reason} |".format(
                task=_cell(slot["title"]),
                repo=_repo_link(project),
                alternatives=alternatives,
                difficulty=DIFFICULTY_LABELS[project["setup"]["difficulty"]],
                data_path=DATA_PATH_LABELS[project["data_path"]],
                services=_cell(_services(project)),
                pool=pool_size,
                depth=DEPTH_LABELS[project["review"]["depth"]],
                reason=_cell(selection["reason"]),
            )
        )

    lines.extend(
        [
            "",
            "## 重点作者与系列",
            "",
            "这一节解决按任务导航容易隐藏优质作者的问题。单列不等于作者的所有项目都是当前推荐。",
            "",
            "| 作者 / 系列 | 覆盖任务 | 代表项目 | 为什么单列 | 审查边界 |",
            "|---|---|---|---|---|",
        ]
    )
    for creator in curation_doc.get("featured_creators", []):
        featured = "<br>".join(_repo_link(projects[project_id]) for project_id in creator["projects"])
        lines.append(
            f"| {_cell(creator['name'])} | {_cell(creator['coverage'])} | {featured} | {_cell(creator['reason'])} | {_cell(creator['boundary'])} |"
        )

    lines.extend(
        [
            "",
            "## 进一步比较",
            "",
            "- [能力地图](docs/CAPABILITIES.md)：查看每个任务的当前推荐、关键备选、比较口径和当前缺口。",
            "- [完整索引](docs/CATALOG.md)：查看全部项目、Star、更新时间、license、审查层级和降级理由。",
            "- [贡献指南](CONTRIBUTING.md)：推荐项目或修正审查信息。",
            "- [合规说明](COMPLIANCE.md)：本仓只做链接、元数据和原创点评，不搬运第三方内容。",
            "",
            "## 平台与公开线索",
            "",
            "商业平台、公众号和社区线索不计入 GitHub 仓库数。未由 GitHub 或仓库文件交叉核验的内容明确标记为 `platform_found` 或 `unverified`。",
            "",
        ]
    )
    for resource in platforms_doc.get("resources", []):
        lines.append(
            f"- [{_cell(resource['title'])}]({resource['url']}) · `{resource['source_grade']}` · {_cell(resource['summary'])}"
        )
    lines.extend(
        [
            "",
            "## 维护与合规",
            "",
            "所有公开页面均由结构化 registry 生成。使用 `python3 scripts/catalog.py check` 检查数据和页面是否一致；使用 `python3 scripts/catalog.py refresh` 更新 GitHub 动态元数据。",
            "",
            "收录不构成质量、安全性或合法性背书。处理合同、证据、个人信息或客户材料前，请自行核验项目的数据流、平台条款和最新许可。",
            "",
            "## 联系与交流",
            "",
            '<div align="center">',
            "",
            "**维护者：赖宁** · [GitHub Issues](https://github.com/lilialla/awesome-legal-ai-zh/issues)",
            "",
            '<img src="assets/contact-qr.png" alt="加作者微信" width="170">',
            "",
            "</div>",
            "",
        ]
    )
    return "\n".join(lines)


def render_capabilities(projects_doc: dict, metadata_doc: dict, curation_doc: dict) -> str:
    projects = project_map(projects_doc)
    snapshot = _snapshot_date(projects_doc, metadata_doc)
    lines = [
        "# 法律 AI 能力地图",
        "",
        f"> 快照 {snapshot}。当前推荐是编辑判断，不是客观“最好”或综合分；相似度检测只用于产生人工复核线索；工程测试通过不等于法律内容正确。",
        "",
        "## 覆盖总览",
        "",
        "| 能力 | 有当前推荐的任务 | 备选项目 | 明确缺口 |",
        "|---|---:|---:|---:|",
    ]
    slots_by_capability: dict[str, list[dict]] = defaultdict(list)
    for slot in curation_doc["slots"]:
        slots_by_capability[slot["capability"]].append(slot)
    for capability in sorted(curation_doc["capabilities"], key=lambda item: item["order"]):
        slots = slots_by_capability[capability["id"]]
        lines.append(
            f"| [{_cell(capability['title'])}](#{capability['id']}) | {sum(bool(slot.get('primary')) for slot in slots)} | {sum(len(slot.get('alternatives', [])) for slot in slots)} | {sum(bool(slot.get('gap')) for slot in slots)} |"
        )

    for capability in sorted(curation_doc["capabilities"], key=lambda item: item["order"]):
        lines.extend(
            [
                "",
                f'<a id="{capability["id"]}"></a>',
                "",
                f"## {_cell(capability['title'])}",
                "",
                _cell(capability["description"]),
                "",
            ]
        )
        for slot in sorted(slots_by_capability[capability["id"]], key=lambda item: item.get("order", 999)):
            lines.extend([f"### {_cell(slot['title'])}", ""])
            pool_size = _capability_pool_size(projects_doc, slot["capability"])
            lines.append(
                f"**比较口径**：{_cell(slot['decision_basis'])}  ·  **大类能力池**：{pool_size} 项"
            )
            lines.append("")
            if slot.get("gap"):
                lines.append(f"> **缺口**：{_cell(slot['gap'])}")
                lines.append("")
            selections: list[tuple[str, dict]] = []
            if slot.get("primary"):
                selections.append(("当前推荐", slot["primary"]))
            selections.extend(("关键备选", item) for item in slot.get("alternatives", []))
            if not selections:
                lines.append("当前没有达到推荐或关键备选门槛的项目。")
                lines.append("")
                continue
            lines.extend(
                [
                    "| 定位 | 项目 | 适用差异 | 上手 | 数据路径 | 依赖 | 核验 | 注意事项 |",
                    "|---|---|---|---|---|---|---|---|",
                ]
            )
            for role, selection in selections:
                project = projects[selection["project"]]
                caution = _cell("；".join(project["cautions"][:2]) or "无特别提示")
                lines.append(
                    f"| {role} | {_repo_link(project)} | {_cell(selection['reason'])} | {DIFFICULTY_LABELS[project['setup']['difficulty']]} | {DATA_PATH_LABELS[project['data_path']]} | {_cell(_services(project))} | {DEPTH_LABELS[project['review']['depth']]} | {caution} |"
                )
            lines.append("")
            lines.append(f"[查看该能力的完整索引](CATALOG.md#{capability['id']})")
            lines.append("")
    return "\n".join(lines)


def render_catalog(projects_doc: dict, metadata_doc: dict, curation_doc: dict) -> str:
    statuses = _effective_statuses(curation_doc)
    task_contexts = _task_contexts(curation_doc)
    projects = projects_doc["projects"]
    lines = [
        "# 完整项目索引",
        "",
        f"> {len(projects)} 个 GitHub 仓库；GitHub 元数据刷新于 {metadata_doc.get('refreshed_at', '未知')}。完整索引保留同质、轻量、观察和退役项目，不等于推荐清单。",
        "",
        "状态：`当前推荐`、`关键备选`、`已索引`、`观察`、`退役`。License 只陈述仓库识别结果及人工提示，不构成授权意见。",
    ]
    groups = [
        ("core", "法律核心"),
        ("support", "法律支撑资源"),
        ("adjacent", "辅助与相邻资源"),
    ]
    for scope, scope_title in groups:
        lines.extend(["", f"## {scope_title}", ""])
        capabilities = sorted(
            {project["primary_capability"] for project in projects if project["scope"] == scope},
            key=lambda item: CAPABILITY_TITLES.get(item, item),
        )
        for capability in capabilities:
            lines.extend(
                [
                    f'<a id="{capability}"></a>',
                    "",
                    f"### {_cell(CAPABILITY_TITLES.get(capability, capability))}",
                    "",
                ]
            )
            lines.extend(
                [
                    "| 状态 | 对应任务 | 项目 | 类型 | ★ | 最近更新 | License | 核验 | 一句话定位 / 注意事项 |",
                    "|---|---|---|---|---:|---|---|---|---|",
                ]
            )
            matching = [
                project
                for project in projects
                if project["scope"] == scope and project["primary_capability"] == capability
            ]
            matching.sort(
                key=lambda project: (
                    -REVIEW_RANK[project["review"]["depth"]],
                    -metadata_for(project["id"], metadata_doc).get("stars", 0),
                    project["id"].lower(),
                )
            )
            for project in matching:
                metadata = metadata_for(project["id"], metadata_doc)
                status = statuses.get(project["id"], project["recommendation"])
                note = project["summary"]
                if project["cautions"]:
                    note += "；注意：" + "；".join(project["cautions"][:2])
                contexts = "<br>".join(_cell(item) for item in task_contexts.get(project["id"], [])) or "-"
                lines.append(
                    f"| {RECOMMENDATION_LABELS[status]} | {contexts} | {_repo_link(project)} | {KIND_LABELS[project['kind']]} | {metadata.get('stars', 0)} | {_date(metadata.get('pushed_at'))} | {_cell(_license(metadata))} | {DEPTH_LABELS[project['review']['depth']]} | {_cell(note)} |"
                )
            lines.append("")
    return "\n".join(lines)


def render_documents(projects_doc: dict, metadata_doc: dict, curation_doc: dict, platforms_doc: dict) -> dict[str, str]:
    validate_data(projects_doc, metadata_doc, curation_doc, platforms_doc)
    return {
        "README.md": render_readme(projects_doc, metadata_doc, curation_doc, platforms_doc),
        "docs/CAPABILITIES.md": render_capabilities(projects_doc, metadata_doc, curation_doc),
        "docs/CATALOG.md": render_catalog(projects_doc, metadata_doc, curation_doc),
        "registry/seed-repos.txt": render_seed(projects_doc),
    }


def _document_anchors(content: str) -> set[str]:
    return set(re.findall(r'<a\s+id="([a-z0-9-]+)"\s*></a>', content))


def validate_generated_documents(
    root: Path, documents: dict[str, str], projects_doc: dict
) -> None:
    readme = documents["README.md"]
    catalog = documents["docs/CATALOG.md"]
    project_ids = {project["id"] for project in projects_doc["projects"]}
    _require(len(readme.splitlines()) <= 220, "README must not exceed 220 lines")
    readme_repos = set(URL_PATTERN.findall(readme)) & project_ids
    _require(len(readme_repos) <= 40, "README may feature at most 40 catalog projects")
    catalog_repo_counts = Counter(URL_PATTERN.findall(catalog))
    _require(
        set(catalog_repo_counts) == project_ids
        and all(count == 1 for count in catalog_repo_counts.values()),
        "complete catalog must contain every project exactly once",
    )

    anchors_by_path = {
        relative: _document_anchors(content) for relative, content in documents.items()
    }
    markdown_link_pattern = re.compile(r"\[[^\]]*\]\(([^)]+)\)")
    html_source_pattern = re.compile(r'(?:src|srcset)="([^"]+)"')
    for relative, content in documents.items():
        _require(not SECRET_PATTERN.search(content), f"possible secret in generated file: {relative}")
        root_resolved = root.resolve()
        source_path = (root / relative).resolve()
        targets = markdown_link_pattern.findall(content) + html_source_pattern.findall(content)
        for raw_target in targets:
            target = raw_target.strip().split(maxsplit=1)[0]
            parsed = urllib.parse.urlparse(target)
            if parsed.scheme in {"http", "https", "mailto"}:
                continue
            target_file = urllib.parse.unquote(parsed.path)
            resolved = source_path if not target_file else (source_path.parent / target_file).resolve()
            _require(resolved.is_relative_to(root_resolved), f"{relative}: link escapes repository {target}")
            target_relative = resolved.relative_to(root_resolved).as_posix()
            _require(resolved.exists() or target_relative in documents, f"{relative}: broken relative link {target}")
            if parsed.fragment:
                anchors = anchors_by_path.get(target_relative, set())
                _require(parsed.fragment in anchors, f"{relative}: missing anchor {target}")


def build(root: Path, *, check: bool) -> None:
    registry = root / "registry"
    projects = load_json(registry / "projects.json")
    metadata = load_json(registry / "github-metadata.json")
    curation = load_json(registry / "curation.json")
    platforms = load_json(registry / "platform-resources.json")
    original_projects = copy.deepcopy(projects)
    _apply_catalog_overrides(projects, root, curation, metadata)
    if projects != original_projects:
        if check:
            raise CatalogError("projects registry is stale: run python3 scripts/catalog.py build")
        dump_json(registry / "projects.json", projects)
    documents = render_documents(projects, metadata, curation, platforms)
    validate_generated_documents(root, documents, projects)
    changed: list[str] = []
    for relative, content in documents.items():
        path = root / relative
        normalized = content.rstrip() + "\n"
        existing = path.read_text(encoding="utf-8") if path.exists() else None
        if existing != normalized:
            changed.append(relative)
            if not check:
                path.parent.mkdir(parents=True, exist_ok=True)
                path.write_text(normalized, encoding="utf-8")
    if check and changed:
        raise CatalogError("generated files are stale: " + ", ".join(changed))
    action = "checked" if check else "built"
    print(f"{action} {len(documents)} generated files")


def _clean_markdown(value: str) -> str:
    value = re.sub(r"<[^>]+>", " ", value)
    value = re.sub(r"!\[[^]]*\]\([^)]+\)", " ", value)
    value = re.sub(r"\[([^]]+)\]\([^)]+\)", r"\1", value)
    value = value.replace("`", "")
    value = re.sub(r"[*_#>|]", " ", value)
    value = re.sub(r"\s+", " ", value).strip()
    return value


def _extract_readme_entries(readme: str) -> dict[str, dict]:
    entries: dict[str, dict] = {}
    for line in readme.splitlines():
        repos = [repo.rstrip("/.") for repo in URL_PATTERN.findall(line)]
        if not repos:
            continue
        cells = [cell.strip() for cell in line.strip().strip("|").split("|")]
        for repo in repos:
            summary = ""
            kind_text = line
            if line.lstrip().startswith("|") and len(cells) >= 5:
                summary = cells[-1]
                kind_text = cells[1]
            else:
                after = line.split(f"github.com/{repo}", 1)[-1]
                summary = after.split(" · ", 1)[0]
            entries.setdefault(repo, {"summary": _clean_markdown(summary), "kind_text": kind_text, "line": line})
    return entries


def _kind(kind_text: str, category: str) -> str:
    text = kind_text.lower()
    if "mcp" in text or "🔌" in text:
        return "mcp"
    if "数据" in text or "评测" in text or category == "dataset-infra":
        return "dataset"
    if "模型" in text or category == "llm":
        return "model"
    if "平台" in text or "套件" in text or category == "skill-suite":
        return "suite"
    if "skill" in text or "agent" in text or "🧩" in text:
        return "skill"
    if "app" in text or "应用" in text:
        return "app"
    if "工具" in text or "cli" in text:
        return "tool"
    return "resource"


def _scope(category: str) -> str:
    if category in CORE_CATEGORIES:
        return "core"
    if category in ADJACENT_CATEGORIES:
        return "adjacent"
    return "support"


def _jurisdictions(text: str) -> list[str]:
    lowered = text.lower()
    result: list[str] = []
    if any(term in lowered for term in ("中国", "中文", "prc", "民法典", "企查查", "元典", "北大法宝")):
        result.append("prc")
    if any(term in lowered for term in ("涉外", "跨境", "国际", "global", "sanction", "sec ", "美国", "台湾")):
        result.append("cross_border")
    return result or ["general"]


def _services_from_text(text: str) -> list[str]:
    services = []
    terms = {
        "企查查": ("企查查", "qcc"),
        "元典": ("元典", "yuandian"),
        "北大法宝": ("北大法宝", "pkulaw"),
        "天眼查": ("天眼查",),
        "SEC/EDGAR": ("sec ", "edgar"),
        "外部 LLM": ("openai", "anthropic api", "llm api", "api key"),
    }
    lowered = text.lower()
    for label, needles in terms.items():
        if any(needle.lower() in lowered for needle in needles):
            services.append(label)
    return services


def _setup(kind: str, text: str) -> dict:
    services = _services_from_text(text)
    lowered = text.lower()
    if kind == "mcp":
        mode = "config"
    elif kind == "skill":
        mode = "install"
    elif kind in {"suite", "app", "tool"}:
        mode = "self_host" if any(term in lowered for term in ("docker", "自部署", "self-host", "fastapi", "django", "react")) else "cli"
    else:
        mode = "reference"
    if mode == "reference":
        difficulty = "reference"
    elif services:
        difficulty = "account_required"
    elif mode in {"self_host", "cli"}:
        difficulty = "technical"
    else:
        difficulty = "ready"
    return {"mode": mode, "difficulty": difficulty, "services": services}


def _data_path(kind: str, text: str, services: list[str]) -> str:
    if kind in {"dataset", "model", "resource"}:
        return "not_applicable"
    lowered = text.lower()
    local = any(term in lowered for term in ("本地", "离线", "local-first", "local first", "localhost"))
    self_hosted = any(term in lowered for term in ("自部署", "self-host", "docker"))
    external = bool(services) or any(term in lowered for term in ("api key", "远端", "cloud api"))
    if (local or self_hosted) and external:
        return "mixed"
    if local:
        return "local"
    if self_hosted:
        return "self_hosted"
    if external:
        return "external_api"
    return "unknown"


def _default_summary(repo: str, category: str) -> str:
    return f"{CAPABILITY_TITLES.get(CATEGORY_CAPABILITY.get(category, ''), '法律 AI')}相关开源项目；旧版 README 未单独展示，待能力页说明。"


def default_platform_resources() -> dict:
    return {
        "schema_version": SCHEMA_VERSION,
        "resources": [
            {
                "id": "yuanli-vault",
                "title": "法律元力 Yuanli Vault",
                "url": "https://yuanli.ailaw.cn",
                "source_grade": "platform_found",
                "summary": "法律 Skill 与工具包聚合平台；平台独占内容未纳入 GitHub 仓库数。",
            },
            {
                "id": "ettalaw-skills",
                "title": "EttaLaw Skill 库",
                "url": "https://ettalawailab.com/skills",
                "source_grade": "platform_found",
                "summary": "法律 Skill 登录下载平台；只记录公开页面信息和既有包级核验结论。",
            },
            {
                "id": "wechat-long-tail",
                "title": "微信公众号长尾线索",
                "url": "https://github.com/lilialla/awesome-legal-ai-zh#平台与公开线索",
                "source_grade": "unverified",
                "summary": "未与公开仓库交叉核验的公众号线索，仅作后续扫描入口。",
            },
        ],
    }


def default_curation() -> dict:
    capabilities = [
        ("starter-suites", "综合套件", "从覆盖面、中文适配和可验证性选择入门套件。"),
        ("contracts", "合同审查与红线", "区分通用审查、专项审查和红线交付。"),
        ("legal-documents", "法律文书与 OCR", "文书格式、OCR、转换和本地脱敏。"),
        ("legal-research", "法规与案例检索", "区分本地法规、案例库、商业数据库接口和现行性核验。"),
        ("litigation", "诉讼、证据与期限", "案件分析、请求权基础、证据和程序期限。"),
        ("enterprise-dd", "企业核查与尽调", "企业数据入口、批量核查和尽调工作流。"),
        ("corporate-ma", "公司、投融资与并购", "股权交易、公司治理、投融资和并购尽调。"),
        ("data-compliance", "数据合规与脱敏", "数据合规检查、隐私文书和材料脱敏。"),
        ("labor-family", "劳动、家事与个人权益", "劳动争议优先；家事与个人权益仍有明显缺口。"),
        ("ip-competition", "知识产权与竞争法", "软著、专利、商标和经营者集中。"),
        ("cross-border-arbitration", "涉外与仲裁", "域外研究、制裁筛查和跨境合同；国际仲裁仍是缺口。"),
        ("law-firm-operations", "律所与案件运营", "个人案件提醒、案件管理和律所工作流。"),
        ("tax-bankruptcy-realestate", "税务、破产与房地产", "中国法专用成熟项目仍然稀缺。"),
    ]

    def pick(project: str, reason: str) -> dict:
        return {"project": project, "reason": reason}

    slots = [
        ("suite-start", "starter-suites", "综合套件", True, pick("NEU-ZHA/legal-ai-skills", "中国法律工作覆盖较完整，且已有脚本级实测证据。"), [pick("CSlawyer1985/claude-for-legal-ZH", "适合需要 Anthropic 法律套件中国法适配的用户。"), pick("zgbrenner/agentcounsel", "适合需要大规模团队化 skill 与验证框架的用户。")], None),
        ("contract-review", "contracts", "合同审查与红线", True, pick("nwwfewx/contract-review", "兼顾中国合同审查路线、结构化资料和 DOCX 辅助脚本。"), [pick("Xigua9xi/ai-legal-review-skillkit", "适合希望自行扩展规则和测试夹具的用户。"), pick("evolsb/legal-redline-tools", "适合把修改意见交付为 Word 红线和 PDF 的用户。")], None),
        ("legal-doc-format", "legal-documents", "法律文书、OCR 与脱敏", True, pick("lilialla/legal-document-format-skill", "直接面向 Word 模板执行、批处理和格式门禁。"), [pick("opendatalab/MinerU", "适合扫描案卷和复杂 PDF 转换。"), pick("moyupeng0422/legal-doc-redactor", "适合本地 DOCX 一致脱敏和审阅痕迹还原。")], None),
        ("law-search", "legal-research", "法规、案例与现行性核验", True, pick("nh59yytyd5-dev/chinalaw-cli", "提供本地法规 CLI/MCP、来源元数据和大规模测试。"), [pick("245678000000/caselaw-mcp-server", "适合接入本地中国案例库。"), pick("bangchuiLee/yuandian-current-law-verifier", "适合在引用法规前强制核验版本和时效。")], None),
        ("litigation-analysis", "litigation", "诉讼分析、证据与期限", True, pick("cat-xierluo/SuitAgent", "以多角色诉讼分析覆盖争点、证据和攻防。"), [pick("SimbaCD/legal-period-manager-skills", "适合诉讼、仲裁和执行期限管理。"), pick("yxk-lawyer/litigation-prep-skill-cn", "适合公司民商事诉讼的请求权与证据清单。")], None),
        ("enterprise-check", "enterprise-dd", "企业核查与尽调", True, pick("zhanglunet/qcc", "同时提供 MCP、双语言客户端和法律工作流 skill。"), [pick("duhu2000/qcc-agent-cli", "适合偏好 CLI、工具自省和配置诊断的用户。"), pick("wgpsec/ENScan_GO", "适合不局限单一商业平台的企业信息聚合。")], None),
        ("corporate-transactions", "corporate-ma", "公司、股权与并购", True, pick("lilialla/equity-transfer-review-skill", "聚焦中国股权转让、出资责任、监管闸门和交割条件。"), [pick("malnlda/legal-due-diligence", "适合中国法律尽调任务。"), pick("skala-io/legal-skills", "适合跨境创业融资和离岸架构场景。")], None),
        ("privacy-redaction", "data-compliance", "数据合规与脱敏", True, pick("moyupeng0422/legal-doc-redactor", "离线处理法律 DOCX，适合个人律师控制材料外传。"), [pick("yangyc03/yangyc-legalai-skills", "适合同时需要本地脱敏和法律关系核验的用户。"), pick("Youchu-lawhub/app-compliance-review", "适合 APP 个人信息保护合规检查。")], None),
        ("labor-dispute", "labor-family", "劳动与家事", True, pick("f12336414-ship-it/labor-arbitration-skill", "围绕法条、时效、金额和证据引用设置核验内核，测试覆盖最强。"), [pick("worker-aid-ai/worker-aid-agent", "适合劳动者自助整理材料和仲裁申请草稿。"), pick("wangchangwei/arb-skill", "适合需要轻量劳动仲裁实务 Skill 的用户。")], "离婚财产分割、继承份额等中国家事工具仍缺成熟首选。"),
        ("ip-work", "ip-competition", "知识产权与竞争法", True, pick("handsomestWei/patent-disclosure-skill", "专利交底材料路径清晰，并强调本地脱敏和查新。"), [pick("Fokkyp/SoftwareCopyright-Skill", "适合软件著作权申请材料生成。"), pick("yuc16/PatentRadar", "适合专利 claim 拆解和侵权竞品分析。")], None),
        ("foreign-law", "cross-border-arbitration", "涉外、制裁与国际仲裁", True, pick("imchongliu/foreign-law-research", "提供面向中国律师的域外法律研究路径。"), [pick("open-agreements/open-agreements", "适合美国及跨境合同模板、清单和 DOCX 生成。"), pick("TracyWang95/DataInftra-CrossBoardTrustedDataPace-SanctionScreening", "适合跨境数据空间和制裁筛查任务。")], "中文开源国际商事仲裁全流程项目仍未形成成熟首选。"),
        ("law-firm-ops", "law-firm-operations", "律所与案件运营", True, pick("AzureTsui/GiGi", "本地优先，聚焦个人律师开庭提醒和卷宗看板。"), [pick("lawflow-boop/LawLink", "适合自部署中小律所案件与执业管理。"), pick("Lawyer-ray/FachuanHybridSystem", "适合需要送达、立案、委托材料和知识库的一体化工作台。")], None),
        ("tax-bankruptcy", "tax-bankruptcy-realestate", "税务、破产与房地产", True, None, [pick("openaccountants/openaccountants", "覆盖多法域税务 Skill，可作为扩展参考。"), pick("fapiaoapi/invoice", "可作为中国发票接口技术底座。")], "尚无同时满足中国法、个人律师可用和实质审查门槛的综合首选。"),
        ("case-search", "legal-research", "中国案例检索", False, pick("245678000000/caselaw-mcp-server", "标准 MCP 与 FastAPI 接口，已有 mock 测试。"), [pick("cncases/cases", "适合作为本地离线案例数据底座。")], None),
        ("law-validity", "legal-research", "法规现行性核验", False, pick("bangchuiLee/yuandian-current-law-verifier", "在法律输出前执行版本、正文和时效核验。"), [pick("yuandian-ailaw/yuandian-mcp-server", "需要更广元典开放平台能力时使用。")], None),
        ("international-arbitration", "cross-border-arbitration", "国际商事仲裁", False, None, [], "当前索引只有域外法、制裁和跨境合同最近邻，缺成品仲裁工作流。"),
    ]
    return {
        "schema_version": SCHEMA_VERSION,
        "capabilities": [
            {"id": capability_id, "title": title, "description": description, "order": order}
            for order, (capability_id, title, description) in enumerate(capabilities, 1)
        ],
        "slots": [
            {
                "id": slot_id,
                "capability": capability,
                "title": title,
                "homepage": homepage,
                "primary": primary,
                "alternatives": alternatives,
                "gap": gap,
                "order": order,
            }
            for order, (slot_id, capability, title, homepage, primary, alternatives, gap) in enumerate(slots, 1)
        ],
    }


def migrate(root: Path, *, force: bool) -> None:
    registry = root / "registry"
    target = registry / "projects.json"
    if target.exists() and not force:
        raise CatalogError("projects.json already exists; use --force to rebuild")
    seed_path = registry / "seed-repos.txt"
    readme_entries = _extract_readme_entries((root / "README.md").read_text(encoding="utf-8"))
    canonical_overrides = {"microsoft/presidio": "data-privacy-stack/presidio"}
    rows: list[tuple[str, str, str]] = []
    for line in seed_path.read_text(encoding="utf-8").splitlines():
        if not line or line.startswith("#"):
            continue
        repo, category = line.split("\t", 1)
        rows.append((canonical_overrides.get(repo, repo), category, repo))
    projects = []
    for repo, category, legacy_repo in rows:
        entry = readme_entries.get(legacy_repo, {})
        source_text = entry.get("line", "")
        summary = entry.get("summary") or _default_summary(repo, category)
        kind = _kind(entry.get("kind_text", source_text), category)
        capability = CATEGORY_CAPABILITY[category]
        scope = _scope(category)
        setup = _setup(kind, source_text + " " + summary)
        aliases = [legacy_repo] if legacy_repo != repo else []
        relationships = (
            [{"type": "redirected_from", "target": legacy_repo, "evidence": "GitHub canonical repository redirect."}]
            if aliases
            else []
        )
        projects.append(
            {
                "id": repo,
                "aliases": aliases,
                "source": "github",
                "url": f"https://github.com/{repo}",
                "name": repo.split("/", 1)[1],
                "scope": scope,
                "kind": kind,
                "primary_capability": capability,
                "capabilities": [capability],
                "jurisdictions": _jurisdictions(source_text + " " + summary),
                "summary": summary[:280],
                "setup": setup,
                "data_path": _data_path(kind, source_text + " " + summary, setup["services"]),
                "recommendation": "indexed",
                "selection_reason": "",
                "cautions": [],
                "relationships": relationships,
                "source_grade": "verified",
                "review": {
                    "depth": "metadata",
                    "reviewed_at": today(),
                    "evidence": ["Migrated from the existing verified GitHub registry and README."],
                    "signals": {"skill_files": 0, "test_files": 0, "code_files": 0},
                },
                "legacy_category": category,
            }
        )
    projects_doc = {"schema_version": SCHEMA_VERSION, "projects": sorted(projects, key=lambda item: item["id"].lower())}
    empty_metadata = {
        "schema_version": SCHEMA_VERSION,
        "refreshed_at": "",
        "repositories": {
            project["id"]: {
                "accessible": False,
                "canonical_id": project["id"],
                "stars": 0,
                "pushed_at": None,
                "updated_at": None,
                "license_spdx": None,
                "archived": False,
                "disabled": False,
                "fork": False,
                "parent": None,
                "default_branch": None,
            }
            for project in projects_doc["projects"]
        },
    }
    dump_json(target, projects_doc)
    dump_json(registry / "github-metadata.json", empty_metadata)
    dump_json(registry / "curation.json", default_curation())
    dump_json(registry / "platform-resources.json", default_platform_resources())
    print(f"migrated {len(projects)} projects")


def _run_gh(arguments: list[str], *, timeout: int = 30, attempts: int = 3) -> dict:
    last_error = "unknown gh error"
    for attempt in range(1, attempts + 1):
        try:
            process = subprocess.run(
                ["gh", *arguments], capture_output=True, text=True, timeout=timeout
            )
        except subprocess.TimeoutExpired:
            last_error = f"timed out after {timeout}s"
        else:
            if process.returncode == 0:
                try:
                    return json.loads(process.stdout)
                except json.JSONDecodeError as exc:
                    last_error = f"invalid JSON: {exc}"
            else:
                last_error = process.stderr.strip() or process.stdout.strip()
        if attempt < attempts:
            time.sleep(attempt)
    raise CatalogError(f"gh command failed after {attempts} attempts: {last_error}")


def refresh(root: Path) -> None:
    registry = root / "registry"
    projects_doc = load_json(registry / "projects.json")
    repositories = [project["id"] for project in projects_doc["projects"]]
    _require(
        all(isinstance(repo, str) and REPO_ID_PATTERN.fullmatch(repo) for repo in repositories),
        "invalid project id",
    )
    result: dict[str, dict] = {}
    for base in range(0, len(repositories), 40):
        batch = repositories[base : base + 40]
        fields = []
        for index, repo in enumerate(batch):
            owner, name = repo.split("/", 1)
            fields.append(
                "r{index}: repository(owner: {owner}, name: {name}) {{ "
                "nameWithOwner isArchived isFork isDisabled stargazerCount pushedAt updatedAt "
                "diskUsage isTemplate description homepageUrl defaultBranchRef {{ name }} "
                "primaryLanguage {{ name }} licenseInfo {{ spdxId }} parent {{ nameWithOwner }} }}".format(
                    index=index, owner=json.dumps(owner), name=json.dumps(name)
                )
            )
        query = "query {" + " ".join(fields) + "}"
        payload = _run_gh(["api", "graphql", "-f", f"query={query}"])
        data = payload.get("data", {})
        for index, repo in enumerate(batch):
            item = data.get(f"r{index}")
            if item is None:
                result[repo] = {
                    "accessible": False,
                    "canonical_id": repo,
                    "stars": 0,
                    "pushed_at": None,
                    "updated_at": None,
                    "license_spdx": None,
                    "archived": False,
                    "disabled": False,
                    "fork": False,
                    "parent": None,
                    "default_branch": None,
                }
                continue
            result[repo] = {
                "accessible": True,
                "canonical_id": item["nameWithOwner"],
                "stars": item["stargazerCount"],
                "pushed_at": item["pushedAt"],
                "updated_at": item["updatedAt"],
                "license_spdx": (item.get("licenseInfo") or {}).get("spdxId"),
                "archived": item["isArchived"],
                "disabled": item["isDisabled"],
                "fork": item["isFork"],
                "parent": (item.get("parent") or {}).get("nameWithOwner"),
                "default_branch": (item.get("defaultBranchRef") or {}).get("name"),
                "description": item.get("description"),
                "homepage": item.get("homepageUrl"),
                "primary_language": (item.get("primaryLanguage") or {}).get("name"),
                "disk_kb": item.get("diskUsage"),
                "template": item.get("isTemplate", False),
            }
        print(f"metadata {min(base + len(batch), len(repositories))}/{len(repositories)}", flush=True)
    metadata_doc = {"schema_version": SCHEMA_VERSION, "refreshed_at": utc_now(), "repositories": result}
    dump_json(registry / "github-metadata.json", metadata_doc)
    print(f"refreshed {len(result)} repositories")


def _api_json(endpoint: str) -> dict:
    return _run_gh(["api", "--cache", "1h", endpoint])


def _read_repository_readme(repo: str) -> str:
    try:
        payload = _api_json(f"repos/{repo}/readme")
    except CatalogError:
        return ""
    content = payload.get("content", "")
    try:
        return base64.b64decode(content).decode("utf-8", errors="replace")
    except (ValueError, TypeError):
        return ""


def _repository_tree(repo: str, branch: str) -> tuple[list[dict], bool]:
    encoded_branch = urllib.parse.quote(branch, safe="")
    payload = _api_json(f"repos/{repo}/git/trees/{encoded_branch}?recursive=1")
    return payload.get("tree", []), bool(payload.get("truncated"))


def _normalize_skill(text: str) -> str:
    text = re.sub(r"\A---\s*\n.*?\n---\s*\n", "", text, flags=re.DOTALL)
    text = re.sub(r"https?://\S+", "<url>", text)
    text = re.sub(r"\s+", " ", text).strip().lower()
    return text


def _shingles(text: str, width: int = 5) -> set[str]:
    compact = text.replace(" ", "")
    return {compact[index : index + width] for index in range(max(0, len(compact) - width + 1))}


def _hashed_shingles(text: str, width: int = 5) -> set[int]:
    compact = text.replace(" ", "")
    return {
        int.from_bytes(
            hashlib.blake2b(compact[index : index + width].encode("utf-8"), digest_size=8).digest(),
            "big",
        )
        for index in range(max(0, len(compact) - width + 1))
    }


def _fetch_raw(repo: str, branch: str, path: str) -> str:
    quoted_path = urllib.parse.quote(path, safe="/")
    url = f"https://raw.githubusercontent.com/{repo}/{urllib.parse.quote(branch, safe='')}/{quoted_path}"
    request = urllib.request.Request(url, headers={"User-Agent": "awesome-legal-ai-zh-audit/2"})
    last_error = "unknown raw download error"
    for attempt in range(1, 3):
        try:
            with urllib.request.urlopen(request, timeout=15) as response:
                raw = response.read(MAX_SKILL_BYTES + 1)
                if len(raw) > MAX_SKILL_BYTES:
                    raise CatalogError("SKILL.md exceeds 2 MB audit limit")
                return raw.decode("utf-8", errors="replace")
        except (urllib.error.URLError, TimeoutError) as exc:
            last_error = str(exc)
            if attempt < 2:
                time.sleep(attempt)
    raise CatalogError(f"raw file read failed: {last_error}")


def _fetch_skill_documents(repo: str, branch: str, fingerprints: list[dict]) -> list[dict]:
    if len(fingerprints) <= 50:
        results = []

        def fetch_one(fingerprint: dict) -> dict | None:
            try:
                text = _fetch_raw(repo, branch, fingerprint["path"])
            except CatalogError:
                return None
            return {**fingerprint, "normalized": _normalize_skill(text)}

        with ThreadPoolExecutor(max_workers=min(4, max(1, len(fingerprints)))) as executor:
            for result in executor.map(fetch_one, fingerprints):
                if result is not None:
                    results.append(result)
        return results

    archive_url = f"https://codeload.github.com/{repo}/zip/{urllib.parse.quote(branch, safe='')}"
    request = urllib.request.Request(
        archive_url, headers={"User-Agent": "awesome-legal-ai-zh-audit/2"}
    )
    last_error = "unknown archive download error"
    for attempt in range(1, 3):
        try:
            with urllib.request.urlopen(request, timeout=120) as response:
                content_length = int(response.headers.get("Content-Length") or 0)
                if content_length > MAX_ARCHIVE_BYTES:
                    raise CatalogError("repository archive exceeds 200 MB audit limit")
                archive_bytes = response.read(MAX_ARCHIVE_BYTES + 1)
                if len(archive_bytes) > MAX_ARCHIVE_BYTES:
                    raise CatalogError("repository archive exceeds 200 MB audit limit")
            with zipfile.ZipFile(io.BytesIO(archive_bytes)) as archive:
                infos = archive.infolist()
                if len(infos) > MAX_ARCHIVE_MEMBERS:
                    raise CatalogError("repository archive contains too many members")
                members = {}
                for info in infos:
                    name = info.filename
                    relative = name.split("/", 1)[1] if "/" in name else name
                    members[relative] = info
                results = []
                total_skill_bytes = 0
                for fingerprint in fingerprints:
                    member = members.get(fingerprint["path"])
                    if not member:
                        continue
                    if member.flag_bits & 0x1:
                        raise CatalogError("encrypted SKILL.md is not auditable")
                    if member.file_size > MAX_SKILL_BYTES:
                        raise CatalogError("SKILL.md exceeds 2 MB audit limit")
                    total_skill_bytes += member.file_size
                    if total_skill_bytes > MAX_SKILL_TOTAL_BYTES:
                        raise CatalogError("repository SKILL.md files exceed 128 MB audit limit")
                    with archive.open(member) as source:
                        raw = source.read(MAX_SKILL_BYTES + 1)
                    if len(raw) > MAX_SKILL_BYTES:
                        raise CatalogError("SKILL.md exceeds 2 MB audit limit")
                    text = raw.decode("utf-8", errors="replace")
                    results.append({**fingerprint, "normalized": _normalize_skill(text)})
                return results
        except (urllib.error.URLError, TimeoutError, zipfile.BadZipFile, RuntimeError, CatalogError) as exc:
            last_error = str(exc)
            if attempt < 2:
                time.sleep(attempt)
    raise CatalogError(f"repository archive read failed: {last_error}")


def _detect_repository(project: dict, readme: str, tree: list[dict], metadata: dict) -> tuple[dict, list[dict]]:
    paths = [item.get("path", "") for item in tree if item.get("type") == "blob"]
    lowered_paths = [path.lower() for path in paths]
    skill_items = [item for item in tree if item.get("type") == "blob" and item.get("path", "").lower().endswith("skill.md")]
    test_paths = [
        path
        for path in paths
        if re.search(r"(^|/)(tests?|__tests__)(/|$)|(^|/).*\.(test|spec)\.(js|ts|tsx)$", path.lower())
    ]
    code_extensions = {".py", ".js", ".ts", ".tsx", ".jsx", ".rs", ".go", ".java", ".kt", ".sh"}
    code_paths = [path for path in paths if Path(path).suffix.lower() in code_extensions]
    text = (readme + "\n" + "\n".join(paths[:3000])).lower()

    kind = project["kind"]
    if skill_items and len(skill_items) > 1:
        kind = "suite"
    elif skill_items:
        kind = "skill"
    elif any("mcp" in path for path in lowered_paths) or "model context protocol" in text:
        kind = "mcp"
    elif any(path in lowered_paths for path in ("package.json", "pyproject.toml", "cargo.toml", "go.mod")):
        kind = "app" if any(term in text for term in ("react", "vue", "django", "fastapi", "tauri")) else "tool"

    services = _services_from_text(text)
    setup = _setup(kind, text)
    setup["services"] = services
    data_path = _data_path(kind, text, services)
    cautions = [item for item in project["cautions"] if not item.startswith(("长期未更新", "GitHub 未识别", "Fork：", "仓库已归档"))]
    if metadata.get("archived"):
        cautions.append("仓库已归档")
    pushed_at = metadata.get("pushed_at")
    if pushed_at and pushed_at[:10] < (dt.date.today() - dt.timedelta(days=365)).isoformat():
        cautions.append("长期未更新，使用前检查依赖和法律时效")
    if not metadata.get("license_spdx"):
        cautions.append("GitHub 未识别许可证，复制、修改或分发前需另行核验")
    if metadata.get("fork"):
        cautions.append(f"Fork：上游为 {metadata.get('parent') or '未知'}")
    if any(term in text for term in ("cookie", "localstorage", "token")) and any(term in text for term in ("浏览器", "browser", "登录")):
        cautions.append("涉及登录态或访问令牌，使用前核验获取方式与平台条款")
    if any(term in text for term in ("自动上传", "auto upload", "telemetry")):
        cautions.append("发现自动上传或遥测描述，处理客户材料前需复核数据流")
    if any(term in text for term in ("公众号", "微信号")) and any(term in text for term in ("每5轮", "每 5 轮", "首次对话")):
        cautions.append("包含对话内推广规则")

    relationships = [relation for relation in project["relationships"] if relation["type"] != "fork_of"]
    if metadata.get("fork") and metadata.get("parent"):
        relationships.append(
            {"type": "fork_of", "target": metadata["parent"], "evidence": "GitHub repository metadata."}
        )

    reviewed = copy.deepcopy(project)
    reviewed.update(
        {
            "kind": kind,
            "setup": setup,
            "data_path": data_path,
            "cautions": list(dict.fromkeys(cautions)),
            "relationships": relationships,
            "review": {
                "depth": "repo_read",
                "reviewed_at": today(),
                "evidence": [
                    "GitHub API metadata verified.",
                    "Repository README and recursive file tree reviewed.",
                ],
                "signals": {
                    "skill_files": len(skill_items),
                    "test_files": len(test_paths),
                    "code_files": len(code_paths),
                    "tree_truncated": False,
                },
            },
        }
    )
    fingerprints = []
    for item in skill_items:
        fingerprints.append({"repo": project["id"], "path": item["path"], "sha": item["sha"]})
    return reviewed, fingerprints


def _apply_review_overrides(projects_doc: dict, root: Path) -> None:
    path = root / "registry" / "review-overrides.json"
    if not path.exists():
        return
    document = load_json(path)
    _require(document.get("schema_version") == SCHEMA_VERSION, "review overrides schema_version must be 2")
    overrides = document.get("projects", {})
    projects = project_map(projects_doc)
    for project_id, override in overrides.items():
        if project_id not in projects:
            raise CatalogError(f"review override references unknown project: {project_id}")
        project = projects[project_id]
        project["review"]["depth"] = override["depth"]
        project["review"]["reviewed_at"] = override.get("reviewed_at", today())
        project["review"]["evidence"].extend(override.get("evidence", []))
        project["review"]["evidence"] = list(dict.fromkeys(project["review"]["evidence"]))
        removed_cautions = set(override.get("remove_cautions", []))
        project["cautions"] = [
            caution for caution in project["cautions"] if caution not in removed_cautions
        ]
        project["cautions"].extend(override.get("cautions", []))
        project["cautions"] = list(dict.fromkeys(project["cautions"]))
        if override.get("summary"):
            project["summary"] = override["summary"]
        if override.get("data_path"):
            project["data_path"] = override["data_path"]
        if override.get("setup"):
            project["setup"].update(override["setup"])


def _repair_legacy_summary(summary: str, metadata: dict, project_name: str) -> str:
    if not summary.strip().startswith(")"):
        return summary
    inner = summary.strip()[1:].strip()
    opening = inner.find("(")
    if opening >= 0 and not re.search(r"[A-Za-z0-9\u4e00-\u9fff]", inner[:opening]):
        inner = inner[opening + 1 :]
    inner = inner.rstrip(")").strip()
    meaningful = []
    for part in inner.split("·"):
        cleaned = part.strip()
        cleaned = re.sub(r"^[✅⚠️❌🔒⭐💎❄️🗄️🛠️🧩🔌🏛️📊🧠📚]+", "", cleaned).strip()
        if not cleaned or re.fullmatch(r"[0-9,]+", cleaned):
            continue
        if cleaned.lstrip("（(").startswith("见 "):
            continue
        meaningful.append(cleaned)
    candidate = "；".join(meaningful).strip()
    if len(candidate) >= 4:
        return candidate[:280]
    description = (metadata.get("description") or "").strip()
    return description[:280] if description else f"{project_name} 项目，待补充编辑摘要。"


def _apply_dynamic_signals(projects_doc: dict, metadata_doc: dict) -> None:
    snapshot = _snapshot_date(projects_doc, metadata_doc)
    try:
        cutoff = dt.date.fromisoformat(snapshot) - dt.timedelta(days=365)
    except ValueError:
        cutoff = dt.date.min
    auto_prefixes = (
        "截至元数据快照已超过一年未更新",
        "长期未更新",
        "GitHub 未识别许可证",
        "Fork：",
        "仓库已归档",
        "仓库当前不可访问",
    )
    for project in projects_doc["projects"]:
        metadata = metadata_for(project["id"], metadata_doc)
        project["summary"] = _repair_legacy_summary(
            project["summary"], metadata, project["name"]
        )
        cautions = [
            caution
            for caution in project["cautions"]
            if not caution.startswith(auto_prefixes)
        ]
        if not metadata.get("accessible", True):
            cautions.append("仓库当前不可访问")
        if metadata.get("archived"):
            cautions.append("仓库已归档，仅作历史索引")
        pushed_at = metadata.get("pushed_at")
        if pushed_at:
            try:
                pushed_date = dt.date.fromisoformat(pushed_at[:10])
            except ValueError:
                pushed_date = None
            if pushed_date and pushed_date < cutoff:
                cautions.append("截至元数据快照已超过一年未更新，保留为历史或基础资源")
        if metadata.get("license_spdx") in {None, "", "NOASSERTION", "OTHER"}:
            cautions.append("GitHub 未识别许可证，复制、修改或分发前需另行核验")
        if metadata.get("fork"):
            cautions.append(f"Fork：上游为 {metadata.get('parent') or '未知'}")
        project["cautions"] = list(dict.fromkeys(cautions))

        relationships = [
            relation for relation in project["relationships"] if relation["type"] != "fork_of"
        ]
        if metadata.get("fork") and metadata.get("parent"):
            relationships.append(
                {
                    "type": "fork_of",
                    "target": metadata["parent"],
                    "evidence": "GitHub repository metadata.",
                }
            )
        project["relationships"] = relationships


def _apply_editorial_status(projects_doc: dict, curation_doc: dict, metadata_doc: dict) -> None:
    selected = _effective_statuses(curation_doc)
    for project in projects_doc["projects"]:
        metadata = metadata_for(project["id"], metadata_doc)
        if metadata.get("archived") or not metadata.get("accessible", True):
            project["recommendation"] = "retired"
        elif project["id"] in selected:
            project["recommendation"] = selected[project["id"]]
        elif project["recommendation"] not in {"watch", "retired"}:
            project["recommendation"] = "indexed"


def _apply_editorial_overrides(projects_doc: dict, root: Path) -> None:
    path = root / "registry" / "editorial-overrides.json"
    if not path.exists():
        return
    document = load_json(path)
    _require(document.get("schema_version") == SCHEMA_VERSION, "editorial overrides schema_version must be 2")
    overrides = document.get("projects", {})
    projects = project_map(projects_doc)
    for project_id, override in overrides.items():
        if project_id not in projects:
            raise CatalogError(f"editorial override references unknown project: {project_id}")
        project = projects[project_id]
        if override.get("recommendation"):
            project["recommendation"] = override["recommendation"]
        if override.get("summary"):
            project["summary"] = override["summary"]
        if override.get("primary_capability"):
            project["primary_capability"] = override["primary_capability"]
        if override.get("capabilities"):
            project["capabilities"] = list(dict.fromkeys(override["capabilities"]))
        if override.get("data_path"):
            project["data_path"] = override["data_path"]
        if override.get("setup"):
            project["setup"].update(override["setup"])
        if "selection_reason" in override:
            project["selection_reason"] = override["selection_reason"]
        removed_cautions = set(override.get("remove_cautions", []))
        project["cautions"] = list(
            dict.fromkeys(
                [caution for caution in project["cautions"] if caution not in removed_cautions]
                + override.get("cautions", [])
            )
        )
        existing_relations = {
            (relation["type"], relation.get("target")) for relation in project["relationships"]
        }
        for relation in override.get("relationships", []):
            key = (relation["type"], relation.get("target"))
            if key not in existing_relations:
                project["relationships"].append(relation)
                existing_relations.add(key)


def _apply_catalog_overrides(
    projects_doc: dict, root: Path, curation_doc: dict, metadata_doc: dict
) -> None:
    _apply_dynamic_signals(projects_doc, metadata_doc)
    _apply_review_overrides(projects_doc, root)
    _apply_editorial_status(projects_doc, curation_doc, metadata_doc)
    _apply_editorial_overrides(projects_doc, root)


def _similarity_report(fingerprints: list[dict], capability_by_repo: dict[str, str]) -> dict:
    exact: dict[str, list[dict]] = defaultdict(list)
    documents: list[dict] = []
    for item in sorted(
        fingerprints,
        key=lambda value: (value.get("repo", ""), value.get("path", ""), value.get("normalized", "")),
    ):
        normalized = item.get("normalized", "")
        if not normalized:
            continue
        digest = hashlib.sha256(normalized.encode("utf-8")).hexdigest()
        record = {"repo": item["repo"], "path": item["path"], "hash": digest, "chars": len(normalized)}
        exact[digest].append(record)
        if 200 <= len(normalized) <= 50000:
            documents.append({**record, "normalized": normalized})
    exact_groups = [
        sorted(group, key=lambda item: (item["repo"], item["path"]))
        for group in exact.values()
        if len({item["repo"] for item in group}) > 1
    ]
    exact_groups.sort(key=lambda group: tuple((item["repo"], item["path"]) for item in group))

    near = []
    by_capability: dict[str, list[dict]] = defaultdict(list)
    for document in documents:
        by_capability[capability_by_repo[document["repo"]]].append(document)
    for capability in sorted(by_capability):
        items = sorted(by_capability[capability], key=lambda item: (item["repo"], item["path"]))
        shingle_sets = [_hashed_shingles(item["normalized"]) for item in items]
        sketches = [set(sorted(shingles)[:64]) for shingles in shingle_sets]
        inverted: dict[int, list[int]] = defaultdict(list)
        for index, sketch in enumerate(sketches):
            for token in sketch:
                inverted[token].append(index)
        candidate_hits: dict[tuple[int, int], int] = defaultdict(int)
        for bucket in inverted.values():
            if len(bucket) < 2 or len(bucket) > 100:
                continue
            for left_index, right_index in itertools.combinations(bucket, 2):
                candidate_hits[(left_index, right_index)] += 1
        for (left_index, right_index), sketch_overlap in candidate_hits.items():
            if sketch_overlap < 3:
                continue
            left = items[left_index]
            right = items[right_index]
            if left["repo"] == right["repo"] or left["hash"] == right["hash"]:
                continue
            ratio = min(left["chars"], right["chars"]) / max(left["chars"], right["chars"])
            if ratio < 0.65:
                continue
            left_set = shingle_sets[left_index]
            right_set = shingle_sets[right_index]
            if not left_set or not right_set:
                continue
            intersection = len(left_set & right_set)
            score = intersection / len(left_set | right_set)
            if score >= 0.65:
                near.append(
                    {
                        "capability": capability,
                        "left": {key: left[key] for key in ("repo", "path", "hash", "chars")},
                        "right": {key: right[key] for key in ("repo", "path", "hash", "chars")},
                        "jaccard": round(score, 4),
                        "review_band": "near_duplicate" if score >= 0.85 else "overlap_review",
                    }
                )
    near.sort(
        key=lambda item: (
            -item["jaccard"],
            item["capability"],
            item["left"]["repo"],
            item["left"]["path"],
            item["right"]["repo"],
            item["right"]["path"],
        )
    )
    return {
        "schema_version": SCHEMA_VERSION,
        "generated_at": utc_now(),
        "method": "Normalized SKILL.md SHA-256; bottom-64 hashed 5-character shingle sketches generate candidates, then exact Jaccard scores candidates. Findings require human review.",
        "exact_groups": exact_groups,
        "similar_pairs": near,
    }


def audit(root: Path) -> None:
    registry = root / "registry"
    projects_doc = load_json(registry / "projects.json")
    metadata_doc = load_json(registry / "github-metadata.json")
    curation_doc = load_json(registry / "curation.json")
    validate_data(
        projects_doc,
        metadata_doc,
        curation_doc,
        load_json(registry / "platform-resources.json"),
        require_primary_review=False,
    )
    selected = set(_effective_statuses(curation_doc))
    targets = [
        project
        for project in projects_doc["projects"]
        if project["scope"] == "core" or project["id"] in selected
    ]
    projects_by_id = project_map(projects_doc)
    fingerprints: list[dict] = []
    failures: list[str] = []
    checkpoint_path = registry / ".audit-checkpoint.json"

    def review_target(source_project: dict) -> tuple[str, dict, list[dict], str | None]:
        project = copy.deepcopy(source_project)
        metadata = metadata_for(project["id"], metadata_doc)
        branch = metadata.get("default_branch")
        if not metadata.get("accessible") or not branch:
            return project["id"], project, [], "missing default branch or inaccessible"
        try:
            readme = _read_repository_readme(project["id"])
            tree, truncated = _repository_tree(project["id"], branch)
            reviewed, repo_fingerprints = _detect_repository(project, readme, tree, metadata)
            reviewed["review"]["signals"]["tree_truncated"] = truncated
            normalized_fingerprints = _fetch_skill_documents(
                project["id"], branch, repo_fingerprints
            )
            return project["id"], reviewed, normalized_fingerprints, None
        except CatalogError as exc:
            return project["id"], project, [], str(exc)

    target_ids = {project["id"] for project in targets}
    completed_ids: set[str] = set()
    checkpoint_fingerprints: list[dict] = []
    if checkpoint_path.exists():
        checkpoint = load_json(checkpoint_path)
        if (
            checkpoint.get("schema_version") == SCHEMA_VERSION
            and set(checkpoint.get("target_ids", [])) == target_ids
        ):
            completed_ids = set(checkpoint.get("completed_ids", [])) & target_ids
            checkpoint_fingerprints = [
                item
                for item in checkpoint.get("fingerprints", [])
                if item.get("repo") in completed_ids
                and REPO_ID_PATTERN.fullmatch(item.get("repo", ""))
                and isinstance(item.get("path"), str)
                and isinstance(item.get("sha"), str)
            ]

    if completed_ids:
        refs_by_repo: dict[str, list[dict]] = defaultdict(list)
        for item in checkpoint_fingerprints:
            refs_by_repo[item["repo"]].append(item)

        def restore_fingerprints(project_id: str) -> tuple[str, list[dict], str | None]:
            branch = metadata_for(project_id, metadata_doc).get("default_branch")
            if not branch:
                return project_id, [], "missing default branch while resuming"
            try:
                restored = _fetch_skill_documents(project_id, branch, refs_by_repo[project_id])
                return project_id, restored, None
            except CatalogError as exc:
                return project_id, [], str(exc)

        with ThreadPoolExecutor(max_workers=4) as executor:
            restored_results = executor.map(restore_fingerprints, sorted(completed_ids))
            for project_id, restored, failure in restored_results:
                if failure:
                    completed_ids.remove(project_id)
                    failures.append(f"{project_id}: resume fingerprint refresh failed: {failure}")
                else:
                    fingerprints.extend(restored)
        checkpoint_fingerprints = [
            item for item in checkpoint_fingerprints if item["repo"] in completed_ids
        ]
        print(
            f"resumed {len(completed_ids)}/{len(targets)} repository reviews; "
            f"restored {len(fingerprints)} skill files",
            flush=True,
        )

    pending_targets = [project for project in targets if project["id"] not in completed_ids]
    processed = len(completed_ids)
    with ThreadPoolExecutor(max_workers=8) as executor:
        futures = {
            executor.submit(review_target, project): project["id"] for project in pending_targets
        }
        for future in as_completed(futures):
            project_id = futures[future]
            try:
                result_id, reviewed, repo_fingerprints, failure = future.result()
            except Exception as exc:  # Keep one repository failure from stopping the full audit.
                failures.append(f"{project_id}: unexpected review error: {exc}")
            else:
                if failure:
                    failures.append(f"{result_id}: {failure}")
                else:
                    projects_by_id[result_id].clear()
                    projects_by_id[result_id].update(reviewed)
                    fingerprints.extend(repo_fingerprints)
                    completed_ids.add(result_id)
                    checkpoint_fingerprints.extend(
                        {key: item[key] for key in ("repo", "path", "sha")}
                        for item in repo_fingerprints
                    )
            processed += 1
            if processed % 5 == 0 or processed == len(targets):
                dump_json(
                    checkpoint_path,
                    {
                        "schema_version": SCHEMA_VERSION,
                        "completed": len(completed_ids),
                        "total": len(targets),
                        "target_ids": sorted(target_ids),
                        "completed_ids": sorted(completed_ids),
                        "fingerprints": sorted(
                            checkpoint_fingerprints,
                            key=lambda item: (item["repo"], item["path"]),
                        ),
                        "updated_at": utc_now(),
                    },
                )
                dump_json(registry / "projects.json", projects_doc)
                print(
                    f"repository review {processed}/{len(targets)}; skill files {len(fingerprints)}",
                    flush=True,
                )

    if completed_ids != target_ids:
        dump_json(registry / "projects.json", projects_doc)
        raise CatalogError(
            f"audit interrupted with {len(target_ids - completed_ids)} repositories pending; rerun audit to resume"
        )

    _apply_catalog_overrides(projects_doc, root, curation_doc, metadata_doc)
    capability_by_repo = {project["id"]: project["primary_capability"] for project in projects_doc["projects"]}
    similarity = _similarity_report(fingerprints, capability_by_repo)
    dump_json(registry / "similarity-report.json", similarity)
    dump_json(registry / "projects.json", projects_doc)
    if checkpoint_path.exists():
        checkpoint_path.unlink()
    print(
        f"reviewed {len(targets)} repositories; {len(fingerprints)} SKILL.md fingerprints; "
        f"{len(similarity['exact_groups'])} exact groups; {len(similarity['similar_pairs'])} similar pairs"
    )
    if failures:
        print(f"review warnings: {len(failures)}", file=sys.stderr)


def validate_command(root: Path) -> None:
    registry = root / "registry"
    validate_data(
        load_json(registry / "projects.json"),
        load_json(registry / "github-metadata.json"),
        load_json(registry / "curation.json"),
        load_json(registry / "platform-resources.json"),
    )
    print("catalog validation passed")


def parse_args(argv: list[str]) -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=Path(__file__).resolve().parents[1])
    subparsers = parser.add_subparsers(dest="command", required=True)
    migrate_parser = subparsers.add_parser("migrate", help="migrate the legacy seed and README")
    migrate_parser.add_argument("--force", action="store_true")
    subparsers.add_parser("refresh", help="refresh GitHub metadata through gh GraphQL")
    subparsers.add_parser("audit", help="review legal-core repository files and Skill similarity")
    subparsers.add_parser("validate", help="validate registry data")
    subparsers.add_parser("build", help="generate README and catalog pages")
    subparsers.add_parser("check", help="validate and check generated files")
    return parser.parse_args(argv)


def main(argv: list[str] | None = None) -> int:
    args = parse_args(argv or sys.argv[1:])
    root = args.root.resolve()
    try:
        if args.command == "migrate":
            migrate(root, force=args.force)
        elif args.command == "refresh":
            refresh(root)
        elif args.command == "audit":
            audit(root)
        elif args.command == "validate":
            validate_command(root)
        elif args.command == "build":
            build(root, check=False)
        elif args.command == "check":
            validate_command(root)
            build(root, check=True)
    except CatalogError as exc:
        print(f"catalog error: {exc}", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
