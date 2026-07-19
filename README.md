<div align="center">

<picture><source media="(prefers-color-scheme: light)" srcset="assets/logo-light.svg"><img src="assets/logo.svg" width="96" alt="awesome-legal-ai-zh"></picture>

# awesome-legal-ai-zh · 法律 AI 选型指南

![Indexed](https://img.shields.io/badge/完整索引-295_仓-3a5a8c) ![Reviewed](https://img.shields.io/badge/仓库审阅-163-2e8b57) ![Tasks](https://img.shields.io/badge/首页任务-20-b5462f) ![Updated](https://img.shields.io/badge/快照-2026--07--19-6b7280)

**给个人律师和法务的开源法律 AI 选型入口：先看任务，再看上手门槛、数据路径、外部依赖和核验深度。**

</div>

本页只展示经过策展的法律核心入口。全部 GitHub 项目见 [完整索引](docs/CATALOG.md)，同类项目差异和能力缺口见 [能力地图](docs/CAPABILITIES.md)。

## 怎么看

- **当前推荐**是编辑判断，不是客观“最好”或综合分；每个具体任务最多一个当前推荐。
- **能力池**是已审阅且标记为该大类的法律核心项目数；具体任务只在其中比较真正可替代的项目。
- **数据路径**只描述项目公开实现：本地、自托管、外部 API、混合或未明确，不等同于安全背书。
- **核验深度**分为元数据核验、仓库审阅、Smoke 通过和测试通过；Star 不参与推荐排序。
- **测试通过**只说明指定工程测试在记录环境中运行成功，不证明法条、金额或法律结论正确。
- License 和权利限制保留在完整索引，不再占用首页主列。

## 按任务选工具

| 具体任务 | 当前推荐 | 关键备选 | 上手 | 数据路径 | 外部依赖 | 能力池 | 核验 | 选择理由 |
|---|---|---|---|---|---|---:|---|---|
| 中国律师日常套件 | [cat-xierluo/legal-skills](https://github.com/cat-xierluo/legal-skills) | [NEU-ZHA/legal-ai-skills](https://github.com/NEU-ZHA/legal-ai-skills)：中国法律任务结构完整，已有脚本级 Smoke 证据。<br>[pa1nrui1/legal-skills](https://github.com/pa1nrui1/legal-skills)：59 个中文法律 Skill，覆盖破产、刑辩、劳动和文书交付。 | 直接安装 | 本地+联网 | 元典、外部 LLM | 28 项 | 仓库审阅 | 杨卫薪律师持续维护，50 个 Skill 覆盖合同、诉讼、检索、知产和律师工作流，可单独下载。 |
| 通用合同审查 | [cat-xierluo/contract-copilot.skill](https://github.com/cat-xierluo/contract-copilot.skill) | [nwwfewx/contract-review](https://github.com/nwwfewx/contract-review)：中国合同审查路线与结构化资料完整，Smoke 通过。<br>[Xigua9xi/ai-legal-review-skillkit](https://github.com/Xigua9xi/ai-legal-review-skillkit)：适合自行扩展审查规则和测试夹具。 | 直接安装 | 本地 | 无特定平台 | 17 项 | 测试通过 | 三层分析与四步审查流程直接交付 Word 批注/修订，6 项 DOCX 回归测试通过。 |
| Word 法律文书排版 | [lilialla/legal-document-format-skill](https://github.com/lilialla/legal-document-format-skill) | - | 直接安装 | 本地 | 无特定平台 | 11 项 | 测试通过 | 面向法律 Word 模板执行、内容锁定和格式门禁，67 项测试通过。 |
| 案卷 OCR 与 PDF 解析 | [opendatalab/MinerU](https://github.com/opendatalab/MinerU) | - | 需部署 | 本地 | 无特定平台 | 11 项 | 仓库审阅 | 复杂 PDF/OCR 生态成熟，适合作为案卷解析底座。 |
| 本地法律材料脱敏 | [moyupeng0422/legal-doc-redactor](https://github.com/moyupeng0422/legal-doc-redactor) | [TracyWang95/DataInfra-RedactionEverything](https://github.com/TracyWang95/DataInfra-RedactionEverything)：多格式、OCR、视觉定位和人工复核更强，548 项后端测试通过，但部署门槛高。<br>[yangyc03/yangyc-legalai-skills](https://github.com/yangyc03/yangyc-legalai-skills)：轻量本地脱敏并有 22 项法律网络/脱敏测试。 | 直接安装 | 本地 | 无特定平台 | 14 项 | 仓库审阅 | 离线 DOCX 一致替换、还原和审阅痕迹处理，个人律师上手更轻。 |
| 中国法规检索 | [nh59yytyd5-dev/chinalaw-cli](https://github.com/nh59yytyd5-dev/chinalaw-cli) | [ZongziForu/cn-law-hub](https://github.com/ZongziForu/cn-law-hub)：法规检索与 MCP 路径轻量，33 项单元测试通过。 | 需部署 | 本地+联网 | 无特定平台 | 24 项 | 测试通过 | 本地法规 CLI/MCP、来源元数据和安装路径完整，678 项测试通过。 |
| 中国案例库检索 | [245678000000/caselaw-mcp-server](https://github.com/245678000000/caselaw-mcp-server) | [cncases/cases](https://github.com/cncases/cases)：适合作为本地离线案例数据底座。 | 需部署 | 自托管 | 无特定平台 | 24 项 | 测试通过 | 标准 MCP 与 FastAPI 接口，mock 适配器下 57 项测试通过。 |
| 本地法律知识库 | 暂无 | [Youchu-lawhub/legal-kb-builder](https://github.com/Youchu-lawhub/legal-kb-builder)：工厂化流程覆盖解析、混合检索、API 与 MCP，脚本编译通过，但尚未功能实测。<br>[leo123-tto/legal-ai](https://github.com/leo123-tto/legal-ai)：集成 MinerU、元典检索和知识库导入导出。 | - | - | - | 24 项 | - | 尚无同时完成真实法律材料入库、检索质量实测且权利边界适合个人律师/法务的当前推荐。 |
| 民商事诉讼全流程 | [Youchu-lawhub/cn-litigation-toolkit](https://github.com/Youchu-lawhub/cn-litigation-toolkit) | [cat-xierluo/SuitAgent](https://github.com/cat-xierluo/SuitAgent)：适合需要多角色 Agent 并行分析争点、证据和攻防的用户。<br>[yxk-lawyer/litigation-prep-skill-cn](https://github.com/yxk-lawyer/litigation-prep-skill-cn)：适合公司民商事案件的请求权基础和证据清单。 | 需部署 | 本地 | 无特定平台 | 18 项 | Smoke 通过 | 23 个 Skill 覆盖从立案访谈到证据、庭审和复盘，MCP 为可选增强，脚本编译通过。 |
| 民事请求权与鉴定式分析 | [Youchu-lawhub/gutachten-civil-case](https://github.com/Youchu-lawhub/gutachten-civil-case) | [lilialla/request-right-skill-reference](https://github.com/lilialla/request-right-skill-reference)：适合需要更轻量中国民事请求权分析参考实现的用户。 | 直接安装 | 未明确 | 无特定平台 | 18 项 | 仓库审阅 | 把德国鉴定式与中国民法典请求权基础检视结合，方法边界清晰。 |
| 诉讼、仲裁与执行期限 | [SimbaCD/legal-period-manager-skills](https://github.com/SimbaCD/legal-period-manager-skills) | [Youchu-lawhub/cn-litigation-toolkit](https://github.com/Youchu-lawhub/cn-litigation-toolkit)：需要期限管理与全流程案件工作结合时使用。 | 需部署 | 本地 | 无特定平台 | 18 项 | 仓库审阅 | 专门处理诉讼、仲裁、执行和待办期限，与诉讼分析套件互补。 |
| 企查查企业核查 | [duhu2000/qcc-agent-cli](https://github.com/duhu2000/qcc-agent-cli) | [zhanglunet/qcc](https://github.com/zhanglunet/qcc)：同时提供 MCP、Python/TypeScript 客户端和法律工作流 Skill。 | 需账号/API | 外部 API | 企查查 | 7 项 | 测试通过 | CLI 工具自省和配置诊断完整，98 项 Jest 测试通过。 |
| 股权转让与公司交易 | [lilialla/equity-transfer-review-skill](https://github.com/lilialla/equity-transfer-review-skill) | - | 直接安装 | 未明确 | 无特定平台 | 19 项 | 仓库审阅 | 聚焦中国股权转让、出资责任、监管闸门和交割条件。 |
| APP 个人信息保护审查 | 暂无 | [Youchu-lawhub/app-compliance-review](https://github.com/Youchu-lawhub/app-compliance-review)：方法论和 50+ 检查项有价值，但当前 material_validator.py 存在 SyntaxError，修复前不列当前推荐。<br>[allenymt/PrivacySentry](https://github.com/allenymt/PrivacySentry)：可作为 Android SDK、权限和隐私行为的技术事实提取工具，但不替代法律评价与整改意见。 | - | - | - | 14 项 | - | 法律评价候选的核心脚本有语法错误；技术检测项目只能补充 APK/SDK/权限事实。 |
| 劳动仲裁 | [f12336414-ship-it/labor-arbitration-skill](https://github.com/f12336414-ship-it/labor-arbitration-skill) | [worker-aid-ai/worker-aid-agent](https://github.com/worker-aid-ai/worker-aid-agent)：更偏劳动者自助整理材料和申请草稿。<br>[wangchangwei/arb-skill](https://github.com/wangchangwei/arb-skill)：更轻量的劳动仲裁实务 Skill。 | 直接安装 | 未明确 | 无特定平台 | 9 项 | 测试通过 | 法条、时效、金额和证据引用都有核验内核，416 项测试通过。 |
| 专利交底与起草 | [handsomestWei/patent-disclosure-skill](https://github.com/handsomestWei/patent-disclosure-skill) | [cat-xierluo/legal-skills](https://github.com/cat-xierluo/legal-skills)：套件内含 code2patent，适合从代码库提取技术证据并生成中国发明专利材料。 | 直接安装 | 本地+联网 | 国知局公开网站 | 8 项 | 测试通过 | 专利交底材料路径清晰，强调本地脱敏和查新，8 项离线测试通过。 |
| 域外法律研究 | [imchongliu/foreign-law-research](https://github.com/imchongliu/foreign-law-research) | - | 直接安装 | 本地+联网 | 公开网络法源 | 8 项 | 仓库审阅 | 面向中国律师的域外法研究路径，强调公开一手法源。 |
| 进出口制裁筛查 | [opensanctions/opensanctions](https://github.com/opensanctions/opensanctions) | [moov-io/watchman](https://github.com/moov-io/watchman)：更轻量的本地 OFAC/全球制裁筛查引擎，适合自建匹配流程。<br>[TracyWang95/DataInftra-CrossBoardTrustedDataPace-SanctionScreening](https://github.com/TracyWang95/DataInftra-CrossBoardTrustedDataPace-SanctionScreening)：更偏跨境数据空间与律师工作流，但当前只完成仓库审阅。 | 需部署 | 自托管 | 无特定平台 | 8 项 | 仓库审阅 | 337 个制裁、PEP 和监视名单源，更新与实体对齐底座完整，仓库含 104 个测试文件。 |
| 个人律师开庭提醒与卷宗看板 | [AzureTsui/GiGi](https://github.com/AzureTsui/GiGi) | - | 需账号/API | 本地+联网 | 外部 LLM | 14 项 | 仓库审阅 | 本地优先，聚焦个人律师开庭提醒、传票解析和卷宗看板。 |
| 中国税法与税务合规 | 暂无 | - | - | - | - | 4 项 | - | 尚无达到中国税法实务推荐门槛的开源项目。 |

## 重点作者与系列

这一节解决按任务导航容易隐藏优质作者的问题。单列不等于作者的所有项目都是当前推荐。

| 作者 / 系列 | 覆盖任务 | 代表项目 | 为什么单列 | 审查边界 |
|---|---|---|---|---|
| 游初 / Youchu-lawhub | 诉讼全流程、民/刑/行政鉴定式分析、本地知识库、APP 合规 | [Youchu-lawhub/cn-litigation-toolkit](https://github.com/Youchu-lawhub/cn-litigation-toolkit)<br>[Youchu-lawhub/gutachten-civil-case](https://github.com/Youchu-lawhub/gutachten-civil-case)<br>[Youchu-lawhub/gutachten-criminal-case](https://github.com/Youchu-lawhub/gutachten-criminal-case)<br>[Youchu-lawhub/gutachten-admin-case](https://github.com/Youchu-lawhub/gutachten-admin-case)<br>[Youchu-lawhub/legal-kb-builder](https://github.com/Youchu-lawhub/legal-kb-builder)<br>[Youchu-lawhub/app-compliance-review](https://github.com/Youchu-lawhub/app-compliance-review) | 诉讼、鉴定式案例分析、知识库和 APP 合规均有明确法律方法论。 | 多数项目无自动化功能测试；授权限个人非商业使用；APP 合规脚本当前有 SyntaxError。 |
| 杨卫薪律师 / cat-xierluo | 中国律师套件、合同审查、诉讼分析、专利与商标 | [cat-xierluo/legal-skills](https://github.com/cat-xierluo/legal-skills)<br>[cat-xierluo/contract-copilot.skill](https://github.com/cat-xierluo/contract-copilot.skill)<br>[cat-xierluo/SuitAgent](https://github.com/cat-xierluo/SuitAgent) | 持续更新的律师工作流套件，合同、诉讼、知产和文书交付都有可执行入口。 | 套件混合法律与通用工具；定向测试 10 项通过，听悟转写 4 项因签名漂移报错；套件未识别统一 License。 |
| Tracy / TracyWang95 | 多格式本地脱敏、标准合同填写、跨境制裁筛查 | [TracyWang95/DataInfra-RedactionEverything](https://github.com/TracyWang95/DataInfra-RedactionEverything)<br>[TracyWang95/DataInftra-CrossBoardTrustedDataPace-SanctionScreening](https://github.com/TracyWang95/DataInftra-CrossBoardTrustedDataPace-SanctionScreening) | 在多格式本地脱敏和跨境制裁工作流上有实质性工程或方法。 | 脱敏工作台 548 项测试通过，但本地部署门槛高且当前 CI/依赖清单有问题；制裁 Skill 仅完成仓库审阅。 |
| CSlawyer1985 | 大型法律 Skill 库、中国法适配 | [CSlawyer1985/claude-for-legal-ZH](https://github.com/CSlawyer1985/claude-for-legal-ZH) | 长期维护 Anthropic 法律 Skill 的中国法适配套件，是大型方法库的重要参照。 | 体量大且外部 MCP/平台依赖多，当前为仓库审阅，未完成全套功能实测。 |

## 进一步比较

- [能力地图](docs/CAPABILITIES.md)：查看每个任务的当前推荐、关键备选、比较口径和当前缺口。
- [完整索引](docs/CATALOG.md)：查看全部项目、Star、更新时间、license、审查层级和降级理由。
- [贡献指南](CONTRIBUTING.md)：推荐项目或修正审查信息。
- [合规说明](COMPLIANCE.md)：本仓只做链接、元数据和原创点评，不搬运第三方内容。

## 平台与公开线索

商业平台、公众号和社区线索不计入 GitHub 仓库数。未由 GitHub 或仓库文件交叉核验的内容明确标记为 `platform_found` 或 `unverified`。

- [法律元力 Yuanli Vault](https://yuanli.ailaw.cn) · `platform_found` · 法律 Skill 与工具包聚合平台；平台独占内容未纳入 GitHub 仓库数。
- [EttaLaw Skill 库](https://ettalawailab.com/skills) · `platform_found` · 法律 Skill 登录下载平台；只记录公开页面信息和既有包级核验结论。

## 维护与合规

所有公开页面均由结构化 registry 生成。使用 `python3 scripts/catalog.py check` 检查数据和页面是否一致；使用 `python3 scripts/catalog.py refresh` 更新 GitHub 动态元数据。

收录不构成质量、安全性或合法性背书。处理合同、证据、个人信息或客户材料前，请自行核验项目的数据流、平台条款和最新许可。

## 联系与交流

<div align="center">

**维护者：赖宁** · [GitHub Issues](https://github.com/lilialla/awesome-legal-ai-zh/issues)

<img src="assets/contact-qr.png" alt="加作者微信" width="170">

</div>
