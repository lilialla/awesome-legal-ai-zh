# 贡献指南

awesome-legal-ai-zh 是面向个人律师和法务的选型指南。首页是精选入口，不追求收录数量；符合范围的真实开源项目可进入完整索引。

## 收录范围

优先收录直接服务于法律、合规、司法或律所工作流的 Skill、MCP、工具、应用、数据集、模型和导航资源。通用技术、PPT、字体、自媒体等只进入“辅助与相邻资源”。

不接受：

- 不可访问、伪造或与法律工作无实质关系的项目。
- 批量生成且无可辨识方法、执行入口或用户价值的内容。
- 第三方代码、README 全文、平台文章正文、图片或需要登录才能获得的内容副本。

Fork 和同质项目可保留在完整索引，但默认引用上游或标记重复关系。只有具备明确的中国法适配或独特功能时，才可进入关键备选。

## 推荐状态

- `当前推荐`：适合该具体任务的多数个人律师或法务，至少完成 `repo_read`。这是编辑判断，不是客观最优。
- `关键备选`：为特定对象、交付方式或技术路线提供明确差异。
- `已索引`：真实、相关，但未达到公开推荐门槛。
- `观察`：存在重复来源、数据流、构建、权利或宣传口径等待核验问题。
- `退役`：归档或已无法作为当前可用项目，仅保留历史索引。

每个具体任务最多一个当前推荐、两个备选，并必须记录比较口径。Star 不参与推荐排序；License 是权利边界信息，不是个人用户价值排名。

## 提交信息

推荐新项目时，请提供：

```text
- 项目 URL：
- 主要法律任务：
- 项目形态（Skill / MCP / 工具 / 应用 / 数据 / 资源）：
- 适用法域：
- 安装或启动入口：
- 外部账号、API 或平台依赖：
- 客户材料的数据路径：
- 与已收录同类项目的差异：
- 已完成的核验或测试：
- 需要提示的风险：
```

Star、更新时间、fork、归档和 GitHub 许可证识别结果由 `refresh` 生成，不要在公开页面中手工维护。

## 本地校验

```bash
python3 -m unittest discover -s tests -v
python3 scripts/catalog.py validate
python3 scripts/catalog.py build
python3 scripts/catalog.py check
```

`registry/projects.json` 是人工审查与结构化信息的主表，`registry/github-metadata.json` 保存动态 GitHub 信号，`registry/curation.json` 保存任务槽、当前推荐、比较口径和作者系列，`registry/seed-repos.txt` 只是自动生成的兼容文件。请不要手工编辑生成的 README、能力页、完整索引或 seed。

## 审查与合规

核验等级分为 `metadata`、`repo_read`、`smoke`、`tested`。不把 `compileall` 单独等同于功能可用，不在测试中使用真实账号、API Key 或客户材料。任何 PR 都不得加入 Cookie、Token、LocalStorage、验证码、第三方仓库内容或平台正文。详见 [COMPLIANCE.md](COMPLIANCE.md)。

`tested` 只表示已记录的工程测试通过，不得据此宣称法条、金额计算或法律结论正确。新增测试证据应尽量记录 revision、命令、环境、fixture、通过/跳过数、mock/live 范围和法律内容校验边界。

对公开呈现、当前推荐、数据结构或收录数造成变化时，在 [CHANGELOG.md](CHANGELOG.md) 顶部记录。
