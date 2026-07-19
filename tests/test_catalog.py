from __future__ import annotations

import importlib.util
import json
import tempfile
import unittest
from pathlib import Path
from unittest import mock


ROOT = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location("catalog", ROOT / "scripts" / "catalog.py")
assert SPEC and SPEC.loader
catalog = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(catalog)


def project(project_id: str, *, depth: str = "repo_read") -> dict:
    return {
        "id": project_id,
        "aliases": [],
        "source": "github",
        "url": f"https://github.com/{project_id}",
        "name": project_id.split("/", 1)[1],
        "scope": "core",
        "kind": "skill",
        "primary_capability": "contracts",
        "capabilities": ["contracts"],
        "jurisdictions": ["prc"],
        "summary": "用于测试的项目。",
        "setup": {"mode": "install", "difficulty": "ready", "services": []},
        "data_path": "unknown",
        "recommendation": "indexed",
        "selection_reason": "",
        "cautions": [],
        "relationships": [],
        "source_grade": "verified",
        "review": {
            "depth": depth,
            "reviewed_at": "2026-07-19",
            "evidence": ["Repository README and tree reviewed."],
            "signals": {"skill_files": 1, "test_files": 0, "code_files": 0},
        },
    }


def documents() -> tuple[dict, dict, dict, dict]:
    projects = {"schema_version": 2, "projects": [project("one/repo"), project("two/repo")]}
    metadata = {
        "schema_version": 2,
        "refreshed_at": "2026-07-19T00:00:00Z",
        "repositories": {
            project_id: {
                "accessible": True,
                "canonical_id": project_id,
                "stars": 1,
                "pushed_at": "2026-07-19T00:00:00Z",
                "updated_at": "2026-07-19T00:00:00Z",
                "license_spdx": "MIT",
                "archived": False,
                "disabled": False,
                "fork": False,
                "parent": None,
                "default_branch": "main",
            }
            for project_id in ("one/repo", "two/repo")
        },
    }
    curation = {
        "schema_version": 2,
        "capabilities": [
            {
                "id": "contracts",
                "title": "合同审查与红线",
                "description": "合同任务。",
                "order": 1,
            }
        ],
        "slots": [
            {
                "id": "contract-review",
                "capability": "contracts",
                "title": "合同审查",
                "homepage": True,
                "decision_basis": "比较合同方法、交付物和测试。",
                "primary": {"project": "one/repo", "reason": "适合多数个人律师。"},
                "alternatives": [
                    {"project": "two/repo", "reason": "适合需要不同交付方式的用户。"}
                ],
                "gap": None,
            }
        ],
    }
    platforms = {"schema_version": 2, "resources": []}
    return projects, metadata, curation, platforms


class CatalogValidationTests(unittest.TestCase):
    def test_valid_documents_pass(self) -> None:
        catalog.validate_data(*documents())

    def test_duplicate_project_ids_fail(self) -> None:
        projects, metadata, curation, platforms = documents()
        projects["projects"].append(project("one/repo"))
        with self.assertRaisesRegex(catalog.CatalogError, "duplicate project id"):
            catalog.validate_data(projects, metadata, curation, platforms)

    def test_unsafe_project_id_fails(self) -> None:
        projects, metadata, curation, platforms = documents()
        projects["projects"][0]["id"] = "one/repo?ref=main"
        with self.assertRaisesRegex(catalog.CatalogError, "invalid project id"):
            catalog.validate_data(projects, metadata, curation, platforms)

    def test_primary_requires_repository_review(self) -> None:
        projects, metadata, curation, platforms = documents()
        projects["projects"][0]["review"]["depth"] = "metadata"
        with self.assertRaisesRegex(catalog.CatalogError, "primary project.*repo_read"):
            catalog.validate_data(projects, metadata, curation, platforms)

    def test_selected_project_must_be_available(self) -> None:
        projects, metadata, curation, platforms = documents()
        metadata["repositories"]["one/repo"]["accessible"] = False
        with self.assertRaisesRegex(catalog.CatalogError, "unavailable or retired"):
            catalog.validate_data(projects, metadata, curation, platforms)

    def test_capabilities_must_be_a_list(self) -> None:
        projects, metadata, curation, platforms = documents()
        projects["projects"][0]["capabilities"] = "contracts"
        with self.assertRaisesRegex(catalog.CatalogError, "capabilities must be a list"):
            catalog.validate_data(projects, metadata, curation, platforms)

    def test_secret_pattern_covers_fine_grained_tokens_and_generic_keys(self) -> None:
        self.assertRegex("github_pat_" + "a" * 30, catalog.SECRET_PATTERN)
        private_key_header = "-----BEGIN PRI" + "VATE KEY-----"
        self.assertRegex(private_key_header, catalog.SECRET_PATTERN)

    def test_audit_preflight_allows_unreviewed_primary(self) -> None:
        projects, metadata, curation, platforms = documents()
        projects["projects"][0]["review"]["depth"] = "metadata"
        catalog.validate_data(
            projects,
            metadata,
            curation,
            platforms,
            require_primary_review=False,
        )

    def test_slot_allows_at_most_two_alternatives(self) -> None:
        projects, metadata, curation, platforms = documents()
        projects["projects"].append(project("three/repo"))
        metadata["repositories"]["three/repo"] = metadata["repositories"]["one/repo"].copy()
        metadata["repositories"]["three/repo"]["canonical_id"] = "three/repo"
        curation["slots"][0]["alternatives"].extend(
            [
                {"project": "three/repo", "reason": "第三个。"},
                {"project": "one/repo", "reason": "重复。"},
            ]
        )
        with self.assertRaisesRegex(catalog.CatalogError, "at most two alternatives"):
            catalog.validate_data(projects, metadata, curation, platforms)

    def test_seed_output_is_sorted_and_stable(self) -> None:
        projects, *_ = documents()
        projects["projects"].reverse()
        first = catalog.render_seed(projects)
        second = catalog.render_seed(projects)
        self.assertEqual(first, second)
        self.assertLess(first.index("one/repo"), first.index("two/repo"))

    def test_generated_documents_are_deterministic(self) -> None:
        projects, metadata, curation, platforms = documents()
        first = catalog.render_documents(projects, metadata, curation, platforms)
        second = catalog.render_documents(projects, metadata, curation, platforms)
        self.assertEqual(first, second)
        self.assertIn("README.md", first)
        self.assertIn("docs/CAPABILITIES.md", first)
        self.assertIn("docs/CATALOG.md", first)

    def test_similarity_report_is_order_independent(self) -> None:
        fingerprints = [
            {"repo": "one/repo", "path": "a/SKILL.md", "normalized": "abcde " * 80},
            {"repo": "two/repo", "path": "b/SKILL.md", "normalized": "abcde " * 80},
            {"repo": "two/repo", "path": "c/SKILL.md", "normalized": "abcdf " * 80},
        ]
        capabilities = {"one/repo": "contracts", "two/repo": "contracts"}
        with mock.patch.object(catalog, "utc_now", return_value="2026-07-19T00:00:00Z"):
            first = catalog._similarity_report(fingerprints, capabilities)
            second = catalog._similarity_report(list(reversed(fingerprints)), capabilities)
        self.assertEqual(first, second)

    def test_audit_failure_does_not_mutate_or_complete_project(self) -> None:
        projects, metadata, curation, platforms = documents()
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            registry = root / "registry"
            registry.mkdir()
            for name, payload in (
                ("projects.json", projects),
                ("github-metadata.json", metadata),
                ("curation.json", curation),
                ("platform-resources.json", platforms),
            ):
                catalog.dump_json(registry / name, payload)
            with mock.patch.object(
                catalog,
                "_read_repository_readme",
                side_effect=catalog.CatalogError("network failure"),
            ):
                with self.assertRaisesRegex(catalog.CatalogError, "repositories pending"):
                    catalog.audit(root)
            persisted = json.loads((registry / "projects.json").read_text(encoding="utf-8"))
            self.assertTrue(all(item["recommendation"] == "indexed" for item in persisted["projects"]))

    def test_table_cells_escape_markdown_delimiters(self) -> None:
        self.assertEqual(catalog._cell("a | b\n<c>"), "a \\| b &lt;c&gt;")

    def test_dump_json_replaces_with_valid_document(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "registry.json"
            catalog.dump_json(path, {"value": 1})
            catalog.dump_json(path, {"value": 2})
            self.assertEqual(json.loads(path.read_text(encoding="utf-8")), {"value": 2})
            self.assertFalse(list(path.parent.glob(".registry.json.*.tmp")))

    def test_write_then_check_has_no_diff(self) -> None:
        projects, metadata, curation, platforms = documents()
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            (root / "registry").mkdir()
            (root / "assets").mkdir()
            for name in ("logo-light.svg", "logo.svg", "contact-qr.png"):
                (root / "assets" / name).write_text("fixture", encoding="utf-8")
            for name in ("CONTRIBUTING.md", "COMPLIANCE.md"):
                (root / name).write_text("fixture", encoding="utf-8")
            for name, payload in (
                ("projects.json", projects),
                ("github-metadata.json", metadata),
                ("curation.json", curation),
                ("platform-resources.json", platforms),
            ):
                (root / "registry" / name).write_text(
                    json.dumps(payload, ensure_ascii=False, indent=2) + "\n", encoding="utf-8"
                )
            catalog.build(root, check=False)
            catalog.build(root, check=True)


class RepositoryAcceptanceTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.projects = json.loads(
            (ROOT / "registry" / "projects.json").read_text(encoding="utf-8")
        )
        cls.curation = json.loads(
            (ROOT / "registry" / "curation.json").read_text(encoding="utf-8")
        )
        cls.readme = (ROOT / "README.md").read_text(encoding="utf-8")
        cls.capabilities = (ROOT / "docs" / "CAPABILITIES.md").read_text(encoding="utf-8")
        cls.catalog = (ROOT / "docs" / "CATALOG.md").read_text(encoding="utf-8")

    def test_migration_preserves_baseline_and_reviewed_additions(self) -> None:
        project_ids = [project["id"] for project in self.projects["projects"]]
        self.assertGreaterEqual(len(project_ids), 295)
        self.assertEqual(len(set(project_ids)), len(project_ids))
        self.assertIn("Youchu-lawhub/cn-litigation-toolkit", project_ids)
        self.assertIn("Youchu-lawhub/legal-kb-builder", project_ids)

    def test_five_common_paths_expose_primary_and_alternatives(self) -> None:
        slots = {slot["id"]: slot for slot in self.curation["slots"]}
        for slot_id in (
            "contract-review",
            "law-search",
            "case-search",
            "enterprise-check",
            "labor-dispute",
            "local-redaction",
        ):
            slot = slots[slot_id]
            self.assertTrue(slot["homepage"])
            self.assertIn(slot["primary"]["project"], self.readme)
            self.assertGreaterEqual(len(slot["alternatives"]), 1)
            for alternative in slot["alternatives"]:
                self.assertIn(alternative["project"], self.capabilities)
                self.assertIn(alternative["project"], self.readme)

    def test_homepage_has_broad_but_bounded_project_selection(self) -> None:
        project_ids = {project["id"] for project in self.projects["projects"]}
        readme_repos = set(catalog.URL_PATTERN.findall(self.readme)) & project_ids
        self.assertGreaterEqual(len(readme_repos), 30)
        self.assertLessEqual(len(readme_repos), 40)

    def test_public_tables_include_selection_context(self) -> None:
        for heading in ("上手", "数据路径", "外部依赖"):
            self.assertIn(heading, self.readme)
        self.assertIn("对应任务", self.catalog)
        self.assertIn("通用合同审查（当前推荐）", self.catalog)

    def test_featured_creator_series_are_visible(self) -> None:
        for project_id in (
            "Youchu-lawhub/cn-litigation-toolkit",
            "Youchu-lawhub/gutachten-civil-case",
            "Youchu-lawhub/gutachten-criminal-case",
            "Youchu-lawhub/gutachten-admin-case",
            "Youchu-lawhub/legal-kb-builder",
            "Youchu-lawhub/app-compliance-review",
            "cat-xierluo/legal-skills",
            "cat-xierluo/contract-copilot.skill",
            "cat-xierluo/SuitAgent",
            "TracyWang95/DataInfra-RedactionEverything",
            "TracyWang95/DataInftra-CrossBoardTrustedDataPace-SanctionScreening",
            "CSlawyer1985/claude-for-legal-ZH",
        ):
            self.assertIn(project_id, self.readme)


if __name__ == "__main__":
    unittest.main()
