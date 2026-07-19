#!/usr/bin/env bash
# Backward-compatible wrapper for the V2 catalog refresh and build commands.
set -euo pipefail

ROOT="$(cd "$(dirname "$0")/.." && pwd)"

command -v gh >/dev/null || {
  echo "需要 gh CLI 且已完成 gh auth login" >&2
  exit 1
}

python3 "$ROOT/scripts/catalog.py" --root "$ROOT" refresh
python3 "$ROOT/scripts/catalog.py" --root "$ROOT" build
echo "已刷新 GitHub 元数据并重新生成公开页面。"
