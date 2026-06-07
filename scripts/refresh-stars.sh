#!/usr/bin/env bash
# 用 gh api 刷新种子清单的真实 star / 更新 / license，输出 Markdown 表，按 star 降序。
# 用法：bash scripts/refresh-stars.sh [registry/seed-repos.txt]  （需 gh 已登录）
set -euo pipefail
SEED="${1:-$(dirname "$0")/../registry/seed-repos.txt}"

command -v gh >/dev/null || { echo "需要 gh CLI（gh auth login）"; exit 1; }

printf '| ★ | 更新 | License | 商用 | 分类 | 项目 |\n|--:|---|---|:-:|---|---|\n' > /tmp/scale_table.md

while IFS=$'\t' read -r repo cat; do
  [[ "$repo" =~ ^#|^$ ]] && continue
  json=$(gh api "repos/$repo" --jq '{s:.stargazers_count,p:.pushed_at,l:.license.spdx_id}' 2>/dev/null) || { echo "  [跳过/404] $repo"; continue; }
  echo "$json $repo $cat"
done < "$SEED" | python3 -c '
import sys,json,re
rows=[]
ok={"MIT","Apache-2.0","BSD-2-Clause","BSD-3-Clause","MPL-2.0","CC0-1.0"}
warn={"GPL-3.0","AGPL-3.0","GPL-2.0","LGPL-3.0"}
for line in sys.stdin:
    line=line.strip()
    if not line or line.startswith("  ["): print(line); continue
    m=re.match(r"(\{.*\})\s+(\S+)\s+(\S+)$",line)
    if not m: continue
    d=json.loads(m.group(1)); repo=m.group(2); cat=m.group(3)
    lic=d.get("l") or "无"
    com="✅" if lic in ok else ("⚠️" if lic in warn else "❌")
    rows.append((d.get("s",0),(d.get("p") or "")[:7],lic,com,cat,repo))
rows.sort(key=lambda x:-x[0])
with open("/tmp/scale_table.md","a") as f:
    for s,p,lic,com,cat,repo in rows:
        f.write(f"| {s} | {p} | {lic} | {com} | {cat} | [{repo}](https://github.com/{repo}) |\n")
print(f"刷新 {len(rows)} 个仓 -> /tmp/scale_table.md")
'
echo "表已写入 /tmp/scale_table.md"
