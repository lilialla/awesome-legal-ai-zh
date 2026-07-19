# Registry V2

`registry/` 是目录的唯一数据源。公开 README、能力地图、完整索引和兼容 seed 均由 `scripts/catalog.py build` 生成。

## 文件职责

- `projects.json`：项目归类、形态、能力、法域、安装、数据路径、摘要、风险、关系和审查证据。
- `github-metadata.json`：Star、最近更新、归档、fork、重定向、默认分支和 GitHub 许可证识别结果。由 `refresh` 更新。
- `curation.json`：能力定义、具体任务槽、当前推荐、关键备选、比较口径、缺口和重点作者/系列。
- `review-overrides.json`：经本地测试或 smoke 已核实的人工证据。
- `editorial-overrides.json`：重复/包含关系、编辑降级和旧分类修正。
- `platform-resources.json`：非 GitHub 公开线索，只能使用 `platform_found` 或 `unverified`。
- `similarity-report.json`：规范化 `SKILL.md` 哈希和字符 shingle 人工复核线索，不保存第三方正文。
- `seed-repos.txt`：旧工具兼容文件，不得手工编辑。

## 维护流程

```bash
python3 scripts/catalog.py refresh
python3 scripts/catalog.py audit
python3 scripts/catalog.py validate
python3 scripts/catalog.py build
python3 scripts/catalog.py check
```

`audit` 只读公开仓库的 README、文件树和 `SKILL.md`；输出仅包含元数据、摘要、信号、哈希和审查结论。不要在本目录保存仓库镜像、账号、Cookie、Token、客户材料或平台正文。

`audit` 会重算仓库检测信号并重写 `projects.json`。需要跨审计保留的人工摘要、能力、数据路径、注意事项、关系和本地测试证据，必须写入 `editorial-overrides.json` 或 `review-overrides.json`，不要只修改生成后的 `projects.json`。

首页最多展示 40 个唯一项目。“当前推荐”是按具体任务作出的编辑判断，不是客观最优或作者总排名；作者系列只用于防止优质生态被任务分类隐藏，必须同时公开审查边界。
