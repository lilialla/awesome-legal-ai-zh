# 法律 AI 能力地图

> 快照 2026-07-19。当前推荐是编辑判断，不是客观“最好”或综合分；相似度检测只用于产生人工复核线索；工程测试通过不等于法律内容正确。

## 覆盖总览

| 能力 | 有当前推荐的任务 | 备选项目 | 明确缺口 |
|---|---:|---:|---:|
| [综合套件](#starter-suites) | 2 | 4 | 0 |
| [合同审查与红线](#contracts) | 3 | 3 | 0 |
| [法律文书与 OCR](#legal-documents) | 4 | 0 | 1 |
| [法规与案例检索](#legal-research) | 3 | 5 | 1 |
| [诉讼、证据与期限](#litigation) | 3 | 6 | 2 |
| [企业核查与尽调](#enterprise-dd) | 1 | 1 | 0 |
| [公司、投融资与并购](#corporate-ma) | 2 | 1 | 2 |
| [数据合规与脱敏](#data-compliance) | 1 | 4 | 1 |
| [劳动、家事与个人权益](#labor-family) | 1 | 2 | 1 |
| [知识产权与竞争法](#ip-competition) | 5 | 2 | 2 |
| [涉外与仲裁](#cross-border-arbitration) | 2 | 2 | 1 |
| [律所与案件运营](#law-firm-operations) | 2 | 1 | 0 |
| [税务、破产与房地产](#tax-bankruptcy-realestate) | 0 | 2 | 3 |

<a id="starter-suites"></a>

## 综合套件

从覆盖面、中文适配和可验证性选择入门套件。

### 中国律师日常套件

**比较口径**：比较中文法律任务覆盖、单 Skill 安装、更新机制、交付物和可验证代码，不以 Star 排序。  ·  **大类能力池**：28 项

| 定位 | 项目 | 适用差异 | 上手 | 数据路径 | 依赖 | 核验 | 注意事项 |
|---|---|---|---|---|---|---|---|
| 当前推荐 | [cat-xierluo/legal-skills](https://github.com/cat-xierluo/legal-skills) | 杨卫薪律师持续维护，50 个 Skill 覆盖合同、诉讼、检索、知产和律师工作流，可单独下载。 | 直接安装 | 本地+联网 | 元典、外部 LLM | 仓库审阅 | 定向实测中同库合同和可视化 10 项通过，听悟转写 4 项因测试与实现签名漂移而报错；GitHub 未识别许可证，复制、修改或分发前需另行核验 |
| 关键备选 | [NEU-ZHA/legal-ai-skills](https://github.com/NEU-ZHA/legal-ai-skills) | 中国法律任务结构完整，已有脚本级 Smoke 证据。 | 需账号/API | 本地+联网 | 北大法宝 | Smoke 通过 | 涉及登录态或访问令牌，使用前核验获取方式与平台条款 |
| 关键备选 | [pa1nrui1/legal-skills](https://github.com/pa1nrui1/legal-skills) | 59 个中文法律 Skill，覆盖破产、刑辩、劳动和文书交付。 | 需账号/API | 本地+联网 | 北大法宝、外部 LLM | 仓库审阅 | 无特别提示 |

[查看该能力的完整索引](CATALOG.md#starter-suites)

### 大型法律 Skill 库

**比较口径**：比较 Skill 数量、路由结构、测试框架、中国法适配和上游关系。  ·  **大类能力池**：28 项

| 定位 | 项目 | 适用差异 | 上手 | 数据路径 | 依赖 | 核验 | 注意事项 |
|---|---|---|---|---|---|---|---|
| 当前推荐 | [zgbrenner/agentcounsel](https://github.com/zgbrenner/agentcounsel) | 221 个 Skill 并有仓库验证脚本和核心单元测试。 | 直接安装 | 未明确 | 无特定平台 | 测试通过 | 无特别提示 |
| 关键备选 | [CSlawyer1985/claude-for-legal-ZH](https://github.com/CSlawyer1985/claude-for-legal-ZH) | Anthropic 法律套件的中国法适配版，内容覆盖广。 | 需账号/API | 本地+联网 | 元典、北大法宝、SEC/EDGAR | 仓库审阅 | Fork：上游为 anthropics/claude-for-legal |
| 关键备选 | [anthropics/claude-for-legal](https://github.com/anthropics/claude-for-legal) | 适合需要上游通用法律方法库的用户。 | 需账号/API | 外部 API | 外部 LLM | 仓库审阅 | 无特别提示 |

[查看该能力的完整索引](CATALOG.md#starter-suites)


<a id="contracts"></a>

## 合同审查与红线

区分通用审查、专项审查和红线交付。

### 通用合同审查

**比较口径**：比较中国合同法方法、风险分层、Word 批注/修订交付、脚本和测试。  ·  **大类能力池**：17 项

| 定位 | 项目 | 适用差异 | 上手 | 数据路径 | 依赖 | 核验 | 注意事项 |
|---|---|---|---|---|---|---|---|
| 当前推荐 | [cat-xierluo/contract-copilot.skill](https://github.com/cat-xierluo/contract-copilot.skill) | 三层分析与四步审查流程直接交付 Word 批注/修订，6 项 DOCX 回归测试通过。 | 直接安装 | 本地 | 无特定平台 | 测试通过 | 已被 cat-xierluo/legal-skills 套件收录，独立仓适合单独安装；GitHub 未识别许可证，复制、修改或分发前需另行核验 |
| 关键备选 | [nwwfewx/contract-review](https://github.com/nwwfewx/contract-review) | 中国合同审查路线与结构化资料完整，Smoke 通过。 | 直接安装 | 本地 | 无特定平台 | Smoke 通过 | 无特别提示 |
| 关键备选 | [Xigua9xi/ai-legal-review-skillkit](https://github.com/Xigua9xi/ai-legal-review-skillkit) | 适合自行扩展审查规则和测试夹具。 | 直接安装 | 未明确 | 无特定平台 | 仓库审阅 | 无特别提示 |

[查看该能力的完整索引](CATALOG.md#contracts)

### Word 红线与审查交付

**比较口径**：只比较能把审查结果写回 DOCX、保留批注或修订痕迹的项目。  ·  **大类能力池**：17 项

| 定位 | 项目 | 适用差异 | 上手 | 数据路径 | 依赖 | 核验 | 注意事项 |
|---|---|---|---|---|---|---|---|
| 当前推荐 | [evolsb/legal-redline-tools](https://github.com/evolsb/legal-redline-tools) | 专门面向 Word 红线、批注和 PDF 交付。 | 直接安装 | 未明确 | 无特定平台 | 仓库审阅 | 无特别提示 |
| 关键备选 | [cat-xierluo/contract-copilot.skill](https://github.com/cat-xierluo/contract-copilot.skill) | 将法律审查方法和 DOCX 交付合在一个 Skill 中。 | 直接安装 | 本地 | 无特定平台 | 测试通过 | 已被 cat-xierluo/legal-skills 套件收录，独立仓适合单独安装；GitHub 未识别许可证，复制、修改或分发前需另行核验 |

[查看该能力的完整索引](CATALOG.md#contracts)

### 标准合同自动填写

**比较口径**：区分合同审查与基于固定模板、事实字段的自动填写。  ·  **大类能力池**：17 项

| 定位 | 项目 | 适用差异 | 上手 | 数据路径 | 依赖 | 核验 | 注意事项 |
|---|---|---|---|---|---|---|---|
| 当前推荐 | [TracyWang95/DataInfra-Agentic-Contract-Filler-Skill](https://github.com/TracyWang95/DataInfra-Agentic-Contract-Filler-Skill) | 面向国家数据局合同模板的专项填写 Skill，任务边界清晰。 | 直接安装 | 未明确 | 无特定平台 | 仓库审阅 | GitHub 未识别许可证，复制、修改或分发前需另行核验 |

[查看该能力的完整索引](CATALOG.md#contracts)


<a id="legal-documents"></a>

## 法律文书与 OCR

文书格式、OCR、转换和本地脱敏。

### Word 法律文书排版

**比较口径**：比较模板执行、格式锁定、批处理、渲染验收和自动化测试。  ·  **大类能力池**：11 项

| 定位 | 项目 | 适用差异 | 上手 | 数据路径 | 依赖 | 核验 | 注意事项 |
|---|---|---|---|---|---|---|---|
| 当前推荐 | [lilialla/legal-document-format-skill](https://github.com/lilialla/legal-document-format-skill) | 面向法律 Word 模板执行、内容锁定和格式门禁，67 项测试通过。 | 直接安装 | 本地 | 无特定平台 | 测试通过 | Python 3.14 下按文档执行 editable install 会因多个顶层目录导致包发现失败；单独安装测试依赖后 67 项 pytest 通过 |

[查看该能力的完整索引](CATALOG.md#legal-documents)

### 诉讼文书与法律意见书起草

**比较口径**：比较事实询问、请求/抗辩结构、法源引用、法律意见书与可交付文档。  ·  **大类能力池**：11 项

> **缺口**：当前只完成仓库审阅，尚无文书内容正确性或 DOCX 交付回归测试。

| 定位 | 项目 | 适用差异 | 上手 | 数据路径 | 依赖 | 核验 | 注意事项 |
|---|---|---|---|---|---|---|---|
| 当前推荐 | [fayayy888/legal-document-assistant](https://github.com/fayayy888/legal-document-assistant) | 13 个 Skill 覆盖答辩状、法律意见书、代理前案件分析和常年法律服务。 | 需账号/API | 本地+联网 | 北大法宝、外部 LLM | 仓库审阅 | GitHub 未识别许可证，复制、修改或分发前需另行核验 |

[查看该能力的完整索引](CATALOG.md#legal-documents)

### 案卷 OCR 与 PDF 解析

**比较口径**：比较扫描件、表格、复杂 PDF、本地处理和后续法律切分接口。  ·  **大类能力池**：11 项

| 定位 | 项目 | 适用差异 | 上手 | 数据路径 | 依赖 | 核验 | 注意事项 |
|---|---|---|---|---|---|---|---|
| 当前推荐 | [opendatalab/MinerU](https://github.com/opendatalab/MinerU) | 复杂 PDF/OCR 生态成熟，适合作为案卷解析底座。 | 需部署 | 本地 | 无特定平台 | 仓库审阅 | GitHub 未识别许可证，复制、修改或分发前需另行核验 |

[查看该能力的完整索引](CATALOG.md#legal-documents)

### 法规文本条款切分

**比较口径**：只比较 OCR/文本提取后的条、款、项结构化切分和 MCP 接入，不与 OCR 引擎作平替比较。  ·  **大类能力池**：11 项

| 定位 | 项目 | 适用差异 | 上手 | 数据路径 | 依赖 | 核验 | 注意事项 |
|---|---|---|---|---|---|---|---|
| 当前推荐 | [GaaZeon-Hui/legal-text-splitter-mcp](https://github.com/GaaZeon-Hui/legal-text-splitter-mcp) | 专门处理中文法规条/款/项切分，包结构化接口并已完成编译级 Smoke。 | 需账号/API | 本地+联网 | 北大法宝 | Smoke 通过 | 无特别提示 |

[查看该能力的完整索引](CATALOG.md#legal-documents)


<a id="legal-research"></a>

## 法规与案例检索

区分本地法规、案例库、商业数据库接口和现行性核验。

### 中国法规检索

**比较口径**：比较法规数据来源、本地可用性、CLI/MCP 接口、来源元数据和回归测试。  ·  **大类能力池**：24 项

| 定位 | 项目 | 适用差异 | 上手 | 数据路径 | 依赖 | 核验 | 注意事项 |
|---|---|---|---|---|---|---|---|
| 当前推荐 | [nh59yytyd5-dev/chinalaw-cli](https://github.com/nh59yytyd5-dev/chinalaw-cli) | 本地法规 CLI/MCP、来源元数据和安装路径完整，678 项测试通过。 | 需部署 | 本地+联网 | 无特定平台 | 测试通过 | 无特别提示 |
| 关键备选 | [ZongziForu/cn-law-hub](https://github.com/ZongziForu/cn-law-hub) | 法规检索与 MCP 路径轻量，33 项单元测试通过。 | 直接安装 | 本地 | 无特定平台 | 测试通过 | GitHub 未识别许可证，复制、修改或分发前需另行核验 |

[查看该能力的完整索引](CATALOG.md#legal-research)

### 中国案例库检索

**比较口径**：只比较真实提供案例数据底座或可调用检索接口的项目。  ·  **大类能力池**：24 项

| 定位 | 项目 | 适用差异 | 上手 | 数据路径 | 依赖 | 核验 | 注意事项 |
|---|---|---|---|---|---|---|---|
| 当前推荐 | [245678000000/caselaw-mcp-server](https://github.com/245678000000/caselaw-mcp-server) | 标准 MCP 与 FastAPI 接口，mock 适配器下 57 项测试通过。 | 需部署 | 自托管 | 无特定平台 | 测试通过 | 57 项 pytest 在 mock 适配器下通过；真实案例数据源仍需用户自行配置和验证 |
| 关键备选 | [cncases/cases](https://github.com/cncases/cases) | 适合作为本地离线案例数据底座。 | 需部署 | 本地 | 无特定平台 | 仓库审阅 | 无特别提示 |

[查看该能力的完整索引](CATALOG.md#legal-research)

### 法规现行性核验

**比较口径**：比较是否在法律输出前独立核验法规版本、正文和时效。  ·  **大类能力池**：24 项

| 定位 | 项目 | 适用差异 | 上手 | 数据路径 | 依赖 | 核验 | 注意事项 |
|---|---|---|---|---|---|---|---|
| 当前推荐 | [bangchuiLee/yuandian-current-law-verifier](https://github.com/bangchuiLee/yuandian-current-law-verifier) | 把现行性核验做成独立门禁，7 项单元测试通过。 | 需账号/API | 外部 API | 元典 | 测试通过 | 无特别提示 |
| 关键备选 | [yuandian-ailaw/yuandian-mcp-server](https://github.com/yuandian-ailaw/yuandian-mcp-server) | 适合同时需要法规、案例和企业数据 API 的用户。 | 需账号/API | 外部 API | 元典、外部 LLM | 仓库审阅 | 无特别提示 |

[查看该能力的完整索引](CATALOG.md#legal-research)

### 本地法律知识库

**比较口径**：比较材料解析、切分、检索、质量门禁、MCP/API 服务和本地数据路径。  ·  **大类能力池**：24 项

> **缺口**：尚无同时完成真实法律材料入库、检索质量实测且权利边界适合个人律师/法务的当前推荐。

| 定位 | 项目 | 适用差异 | 上手 | 数据路径 | 依赖 | 核验 | 注意事项 |
|---|---|---|---|---|---|---|---|
| 关键备选 | [Youchu-lawhub/legal-kb-builder](https://github.com/Youchu-lawhub/legal-kb-builder) | 工厂化流程覆盖解析、混合检索、API 与 MCP，脚本编译通过，但尚未功能实测。 | 需部署 | 自托管 | 无特定平台 | Smoke 通过 | CC BY-NC-ND 4.0 并附加禁止 AI 训练、企业/政府使用等限制，使用前需阅读完整 LICENSE；34 个 Python 入口编译通过；未使用真实解析后端和法律材料进行功能测试 |
| 关键备选 | [leo123-tto/legal-ai](https://github.com/leo123-tto/legal-ai) | 集成 MinerU、元典检索和知识库导入导出。 | 需账号/API | 本地+联网 | 元典 | 仓库审阅 | 无特别提示 |

[查看该能力的完整索引](CATALOG.md#legal-research)


<a id="litigation"></a>

## 诉讼、证据与期限

案件分析、请求权基础、证据和程序期限。

### 民商事诉讼全流程

**比较口径**：比较案情建模、请求权/要件、证据、文书、庭审、质控和外部检索解耦。  ·  **大类能力池**：18 项

| 定位 | 项目 | 适用差异 | 上手 | 数据路径 | 依赖 | 核验 | 注意事项 |
|---|---|---|---|---|---|---|---|
| 当前推荐 | [Youchu-lawhub/cn-litigation-toolkit](https://github.com/Youchu-lawhub/cn-litigation-toolkit) | 23 个 Skill 覆盖从立案访谈到证据、庭审和复盘，MCP 为可选增强，脚本编译通过。 | 需部署 | 本地 | 无特定平台 | Smoke 通过 | CC BY-NC-ND 4.0 及附加条款；个人学习可用，执业交付、企业使用和公开改编前需核对授权边界；Python 脚本编译通过；仓库未提供自动化功能测试 |
| 关键备选 | [cat-xierluo/SuitAgent](https://github.com/cat-xierluo/SuitAgent) | 适合需要多角色 Agent 并行分析争点、证据和攻防的用户。 | 直接安装 | 未明确 | 无特定平台 | 仓库审阅 | 同版本 Skill 也在 cat-xierluo/legal-skills 套件中；独立仓保留为诉讼任务入口 |
| 关键备选 | [yxk-lawyer/litigation-prep-skill-cn](https://github.com/yxk-lawyer/litigation-prep-skill-cn) | 适合公司民商事案件的请求权基础和证据清单。 | 直接安装 | 未明确 | 无特定平台 | 仓库审阅 | GitHub 未识别许可证，复制、修改或分发前需另行核验 |

[查看该能力的完整索引](CATALOG.md#litigation)

### 民事请求权与鉴定式分析

**比较口径**：比较请求权基础检视、要件涵摄、反论结构、法条校验和输出可复核性。  ·  **大类能力池**：18 项

| 定位 | 项目 | 适用差异 | 上手 | 数据路径 | 依赖 | 核验 | 注意事项 |
|---|---|---|---|---|---|---|---|
| 当前推荐 | [Youchu-lawhub/gutachten-civil-case](https://github.com/Youchu-lawhub/gutachten-civil-case) | 把德国鉴定式与中国民法典请求权基础检视结合，方法边界清晰。 | 直接安装 | 未明确 | 无特定平台 | 仓库审阅 | GitHub 未识别许可证，复制、修改或分发前需另行核验 |
| 关键备选 | [lilialla/request-right-skill-reference](https://github.com/lilialla/request-right-skill-reference) | 适合需要更轻量中国民事请求权分析参考实现的用户。 | 需账号/API | 本地+联网 | 外部 LLM | 仓库审阅 | GitHub 未识别许可证，复制、修改或分发前需另行核验 |

[查看该能力的完整索引](CATALOG.md#litigation)

### 刑事三阶层鉴定式分析

**比较口径**：聚焦罪名发现、三阶层犯罪论、双闸确认、法条核验和 Word 交付。  ·  **大类能力池**：18 项

> **缺口**：只有单一方法型候选，尚不足以作出当前推荐。

| 定位 | 项目 | 适用差异 | 上手 | 数据路径 | 依赖 | 核验 | 注意事项 |
|---|---|---|---|---|---|---|---|
| 关键备选 | [Youchu-lawhub/gutachten-criminal-case](https://github.com/Youchu-lawhub/gutachten-criminal-case) | 覆盖案情解析、罪名预选、并行写作和三维核验；当前仅有仓库审阅且无同类候选对比。 | 直接安装 | 未明确 | 无特定平台 | 仓库审阅 | GitHub 未识别许可证，复制、修改或分发前需另行核验 |

[查看该能力的完整索引](CATALOG.md#litigation)

### 行政行为合法性与鉴定式分析

**比较口径**：聚焦可受理性、行政行为类型、合法性六要素、比例原则和裁量审查。  ·  **大类能力池**：18 项

> **缺口**：只有单一方法型候选，尚不足以作出当前推荐。

| 定位 | 项目 | 适用差异 | 上手 | 数据路径 | 依赖 | 核验 | 注意事项 |
|---|---|---|---|---|---|---|---|
| 关键备选 | [Youchu-lawhub/gutachten-admin-case](https://github.com/Youchu-lawhub/gutachten-admin-case) | 行政法专项路由和审查框架完整；当前仅有仓库审阅且无同类候选对比。 | 直接安装 | 未明确 | 无特定平台 | 仓库审阅 | GitHub 未识别许可证，复制、修改或分发前需另行核验 |

[查看该能力的完整索引](CATALOG.md#litigation)

### 诉讼、仲裁与执行期限

**比较口径**：只比较程序日期识别、期限计算、提醒和复核记录。  ·  **大类能力池**：18 项

| 定位 | 项目 | 适用差异 | 上手 | 数据路径 | 依赖 | 核验 | 注意事项 |
|---|---|---|---|---|---|---|---|
| 当前推荐 | [SimbaCD/legal-period-manager-skills](https://github.com/SimbaCD/legal-period-manager-skills) | 专门处理诉讼、仲裁、执行和待办期限，与诉讼分析套件互补。 | 需部署 | 本地 | 无特定平台 | 仓库审阅 | 无特别提示 |
| 关键备选 | [Youchu-lawhub/cn-litigation-toolkit](https://github.com/Youchu-lawhub/cn-litigation-toolkit) | 需要期限管理与全流程案件工作结合时使用。 | 需部署 | 本地 | 无特定平台 | Smoke 通过 | CC BY-NC-ND 4.0 及附加条款；个人学习可用，执业交付、企业使用和公开改编前需核对授权边界；Python 脚本编译通过；仓库未提供自动化功能测试 |

[查看该能力的完整索引](CATALOG.md#litigation)


<a id="enterprise-dd"></a>

## 企业核查与尽调

企业数据入口、批量核查和尽调工作流。

### 企查查企业核查

**比较口径**：比较官方 API 依赖、CLI/MCP 接口、配置诊断、批量查询和测试，不对“官方产品”宣称背书。  ·  **大类能力池**：7 项

| 定位 | 项目 | 适用差异 | 上手 | 数据路径 | 依赖 | 核验 | 注意事项 |
|---|---|---|---|---|---|---|---|
| 当前推荐 | [duhu2000/qcc-agent-cli](https://github.com/duhu2000/qcc-agent-cli) | CLI 工具自省和配置诊断完整，98 项 Jest 测试通过。 | 需账号/API | 外部 API | 企查查 | 测试通过 | 仓库的“官方产品”表述未独立核验，本索引不对该身份背书 |
| 关键备选 | [zhanglunet/qcc](https://github.com/zhanglunet/qcc) | 同时提供 MCP、Python/TypeScript 客户端和法律工作流 Skill。 | 需账号/API | 本地+联网 | 企查查、外部 LLM | 仓库审阅 | 无特别提示 |

[查看该能力的完整索引](CATALOG.md#enterprise-dd)


<a id="corporate-ma"></a>

## 公司、投融资与并购

股权交易、公司治理、投融资和并购尽调。

### 股权转让与公司交易

**比较口径**：先按股权转让、融资、并购尽调拆开；首页只给已有明确中国法闸门和交割逻辑的单点项目。  ·  **大类能力池**：19 项

> **缺口**：股权转让之外的法律尽调和创业融资已拆分为独立任务，不用本项目代表。

| 定位 | 项目 | 适用差异 | 上手 | 数据路径 | 依赖 | 核验 | 注意事项 |
|---|---|---|---|---|---|---|---|
| 当前推荐 | [lilialla/equity-transfer-review-skill](https://github.com/lilialla/equity-transfer-review-skill) | 聚焦中国股权转让、出资责任、监管闸门和交割条件。 | 直接安装 | 未明确 | 无特定平台 | 仓库审阅 | 无特别提示 |

[查看该能力的完整索引](CATALOG.md#corporate-ma)

### 中国法律尽职调查

**比较口径**：比较尽调清单、材料缺口、风险分级、引证和数据室材料路径。  ·  **大类能力池**：19 项

> **缺口**：中国法候选尚无自动化功能测试。

| 定位 | 项目 | 适用差异 | 上手 | 数据路径 | 依赖 | 核验 | 注意事项 |
|---|---|---|---|---|---|---|---|
| 当前推荐 | [malnlda/legal-due-diligence](https://github.com/malnlda/legal-due-diligence) | 面向中国法律尽调的专项 Skill，任务范围和交付结构明确。 | 需账号/API | 外部 API | 元典 | 仓库审阅 | GitHub 未识别许可证，复制、修改或分发前需另行核验 |
| 关键备选 | [zoharbabin/due-diligence-agents](https://github.com/zoharbabin/due-diligence-agents) | 更适合复杂 M&amp;A 数据室的多 Agent 交叉引证，但需复核外部模型的材料上传路径。 | 需账号/API | 本地+联网 | 外部 LLM | 仓库审阅 | 发现自动上传或遥测描述，处理客户材料前需复核数据流 |

[查看该能力的完整索引](CATALOG.md#corporate-ma)


<a id="data-compliance"></a>

## 数据合规与脱敏

数据合规检查、隐私文书和材料脱敏。

### 本地法律材料脱敏

**比较口径**：分别比较轻量 DOCX 脱敏和多格式本地 AI 工作台，重点看材料是否出本机、部署门槛和实测证据。  ·  **大类能力池**：14 项

| 定位 | 项目 | 适用差异 | 上手 | 数据路径 | 依赖 | 核验 | 注意事项 |
|---|---|---|---|---|---|---|---|
| 当前推荐 | [moyupeng0422/legal-doc-redactor](https://github.com/moyupeng0422/legal-doc-redactor) | 离线 DOCX 一致替换、还原和审阅痕迹处理，个人律师上手更轻。 | 直接安装 | 本地 | 无特定平台 | 仓库审阅 | 无特别提示 |
| 关键备选 | [TracyWang95/DataInfra-RedactionEverything](https://github.com/TracyWang95/DataInfra-RedactionEverything) | 多格式、OCR、视觉定位和人工复核更强，548 项后端测试通过，但部署门槛高。 | 需部署 | 自托管 | 无特定平台 | 测试通过 | 默认本地/内网处理，但完整模型链对 GPU、WSL 和部署能力要求较高；仓库 CI 连续失败；实测时 requirements-ci.txt 缺少代码实际导入的 scipy，补充后 548 项测试通过 |
| 关键备选 | [yangyc03/yangyc-legalai-skills](https://github.com/yangyc03/yangyc-legalai-skills) | 轻量本地脱敏并有 22 项法律网络/脱敏测试。 | 直接安装 | 本地 | 无特定平台 | 测试通过 | 无特别提示 |

[查看该能力的完整索引](CATALOG.md#data-compliance)

### APP 个人信息保护审查

**比较口径**：比较 APK 事实提取、隐私政策一致性、SDK/权限、法规锚定和整改清单；可运行性是当前硬门槛。  ·  **大类能力池**：14 项

> **缺口**：法律评价候选的核心脚本有语法错误；技术检测项目只能补充 APK/SDK/权限事实。

| 定位 | 项目 | 适用差异 | 上手 | 数据路径 | 依赖 | 核验 | 注意事项 |
|---|---|---|---|---|---|---|---|
| 关键备选 | [Youchu-lawhub/app-compliance-review](https://github.com/Youchu-lawhub/app-compliance-review) | 方法论和 50+ 检查项有价值，但当前 material_validator.py 存在 SyntaxError，修复前不列当前推荐。 | 需账号/API | 外部 API | 元典、外部 LLM | 仓库审阅 | scripts/material_validator.py 当前存在括号不匹配的 SyntaxError，修复前不建议作为可运行首选；GitHub 未识别许可证，复制、修改或分发前需另行核验 |
| 关键备选 | [allenymt/PrivacySentry](https://github.com/allenymt/PrivacySentry) | 可作为 Android SDK、权限和隐私行为的技术事实提取工具，但不替代法律评价与整改意见。 | 需部署 | 本地 | 无特定平台 | 仓库审阅 | 无特别提示 |

[查看该能力的完整索引](CATALOG.md#data-compliance)


<a id="labor-family"></a>

## 劳动、家事与个人权益

劳动争议优先；家事与个人权益仍有明显缺口。

### 劳动仲裁

**比较口径**：比较法条时效、金额计算、证据引用、仲裁文书和自动化测试。  ·  **大类能力池**：9 项

| 定位 | 项目 | 适用差异 | 上手 | 数据路径 | 依赖 | 核验 | 注意事项 |
|---|---|---|---|---|---|---|---|
| 当前推荐 | [f12336414-ship-it/labor-arbitration-skill](https://github.com/f12336414-ship-it/labor-arbitration-skill) | 法条、时效、金额和证据引用都有核验内核，416 项测试通过。 | 直接安装 | 未明确 | 无特定平台 | 测试通过 | 无特别提示 |
| 关键备选 | [worker-aid-ai/worker-aid-agent](https://github.com/worker-aid-ai/worker-aid-agent) | 更偏劳动者自助整理材料和申请草稿。 | 需账号/API | 本地+联网 | 外部 LLM | 仓库审阅 | GitHub 未识别许可证，复制、修改或分发前需另行核验 |
| 关键备选 | [wangchangwei/arb-skill](https://github.com/wangchangwei/arb-skill) | 更轻量的劳动仲裁实务 Skill。 | 直接安装 | 自托管 | 无特定平台 | 仓库审阅 | GitHub 未识别许可证，复制、修改或分发前需另行核验 |

[查看该能力的完整索引](CATALOG.md#labor-family)

### 婚姻、继承与家事

**比较口径**：分开处理劳动与家事，不再因劳动项目成熟就宣称家事能力已覆盖。  ·  **大类能力池**：9 项

> **缺口**：离婚财产分割、抚养、继承份额等中国家事工具仍缺成熟开源项目。

当前没有达到推荐或关键备选门槛的项目。


<a id="ip-competition"></a>

## 知识产权与竞争法

软著、专利、商标和经营者集中。

### 专利交底与起草

**比较口径**：比较技术证据提取、交底书结构、查新、本地脱敏和离线测试。  ·  **大类能力池**：8 项

| 定位 | 项目 | 适用差异 | 上手 | 数据路径 | 依赖 | 核验 | 注意事项 |
|---|---|---|---|---|---|---|---|
| 当前推荐 | [handsomestWei/patent-disclosure-skill](https://github.com/handsomestWei/patent-disclosure-skill) | 专利交底材料路径清晰，强调本地脱敏和查新，8 项离线测试通过。 | 直接安装 | 本地+联网 | 国知局公开网站 | 测试通过 | 8 项离线测试通过；未运行需访问国知局网站的 Playwright 联调链路 |
| 关键备选 | [cat-xierluo/legal-skills](https://github.com/cat-xierluo/legal-skills) | 套件内含 code2patent，适合从代码库提取技术证据并生成中国发明专利材料。 | 直接安装 | 本地+联网 | 元典、外部 LLM | 仓库审阅 | 定向实测中同库合同和可视化 10 项通过，听悟转写 4 项因测试与实现签名漂移而报错；GitHub 未识别许可证，复制、修改或分发前需另行核验 |

[查看该能力的完整索引](CATALOG.md#ip-competition)

### 专利侵权、无效与 FTO

**比较口径**：不与专利起草混合，只比较权利要求拆解、侵权比对、稳定性、FTO 和规避设计。  ·  **大类能力池**：8 项

| 定位 | 项目 | 适用差异 | 上手 | 数据路径 | 依赖 | 核验 | 注意事项 |
|---|---|---|---|---|---|---|---|
| 当前推荐 | [yuc16/PatentRadar](https://github.com/yuc16/PatentRadar) | 权利要求拆解和竞品侵权分析路径明确，52 项回归测试通过。 | 需账号/API | 本地+联网 | 外部 LLM | 测试通过 | 涉及登录态或访问令牌，使用前核验获取方式与平台条款；GitHub 未识别许可证，复制、修改或分发前需另行核验 |
| 关键备选 | [cat-xierluo/patent-analysis.skill](https://github.com/cat-xierluo/patent-analysis.skill) | 覆盖侵权、无效、FTO、规避设计和价值评估七类场景。 | 直接安装 | 未明确 | 无特定平台 | 仓库审阅 | GitHub 未识别许可证，复制、修改或分发前需另行核验 |

[查看该能力的完整索引](CATALOG.md#ip-competition)

### 商标申请与可注册性初筛

**比较口径**：单独比较商标类别规划、可注册性初筛和申请材料准备。  ·  **大类能力池**：8 项

| 定位 | 项目 | 适用差异 | 上手 | 数据路径 | 依赖 | 核验 | 注意事项 |
|---|---|---|---|---|---|---|---|
| 当前推荐 | [cat-xierluo/trademark-assistant.skill](https://github.com/cat-xierluo/trademark-assistant.skill) | 中国商标申请任务边界明确，与专利工具分开展示。 | 直接安装 | 未明确 | 无特定平台 | 仓库审阅 | 已被 cat-xierluo/legal-skills 套件收录，独立仓适合单独安装；GitHub 未识别许可证，复制、修改或分发前需另行核验 |

[查看该能力的完整索引](CATALOG.md#ip-competition)

### 软件著作权申请材料

**比较口径**：比较源码与说明文档取样、申请表字段、材料排版和本地处理。  ·  **大类能力池**：8 项

> **缺口**：当前仅有仓库审阅，未使用脱敏项目验收申请材料。

| 定位 | 项目 | 适用差异 | 上手 | 数据路径 | 依赖 | 核验 | 注意事项 |
|---|---|---|---|---|---|---|---|
| 当前推荐 | [Fokkyp/SoftwareCopyright-Skill](https://github.com/Fokkyp/SoftwareCopyright-Skill) | 专门生成软著申请所需的源码和文档材料，执行入口明确。 | 直接安装 | 未明确 | 无特定平台 | 仓库审阅 | 无特别提示 |

[查看该能力的完整索引](CATALOG.md#ip-competition)

### 经营者集中申报评估

**比较口径**：单独比较控制权、营业额门槛、相关市场、申报程序和风险输出。  ·  **大类能力池**：8 项

> **缺口**：当前仅有仓库审阅，无案例夹具或自动化门槛测试。

| 定位 | 项目 | 适用差异 | 上手 | 数据路径 | 依赖 | 核验 | 注意事项 |
|---|---|---|---|---|---|---|---|
| 当前推荐 | [ettajingruyang/PRC-merger-control-assessment](https://github.com/ettajingruyang/PRC-merger-control-assessment) | 聚焦中国经营者集中申报评估，不与专利或商标工具混作一类。 | 直接安装 | 未明确 | 无特定平台 | 仓库审阅 | GitHub 未识别许可证，复制、修改或分发前需另行核验 |

[查看该能力的完整索引](CATALOG.md#ip-competition)


<a id="cross-border-arbitration"></a>

## 涉外与仲裁

域外研究、制裁筛查和跨境合同；国际仲裁仍是缺口。

### 域外法律研究

**比较口径**：比较问题分解、法域识别、一手法源、引用可回溯性和面向中国律师的交付。  ·  **大类能力池**：8 项

| 定位 | 项目 | 适用差异 | 上手 | 数据路径 | 依赖 | 核验 | 注意事项 |
|---|---|---|---|---|---|---|---|
| 当前推荐 | [imchongliu/foreign-law-research](https://github.com/imchongliu/foreign-law-research) | 面向中国律师的域外法研究路径，强调公开一手法源。 | 直接安装 | 本地+联网 | 公开网络法源 | 仓库审阅 | 无特别提示 |

[查看该能力的完整索引](CATALOG.md#cross-border-arbitration)

### 进出口制裁筛查

**比较口径**：比较名单覆盖和更新、模糊匹配、误报复核、部署门槛与面向律师的工作流。  ·  **大类能力池**：8 项

| 定位 | 项目 | 适用差异 | 上手 | 数据路径 | 依赖 | 核验 | 注意事项 |
|---|---|---|---|---|---|---|---|
| 当前推荐 | [opensanctions/opensanctions](https://github.com/opensanctions/opensanctions) | 337 个制裁、PEP 和监视名单源，更新与实体对齐底座完整，仓库含 104 个测试文件。 | 需部署 | 自托管 | 无特定平台 | 仓库审阅 | 无特别提示 |
| 关键备选 | [moov-io/watchman](https://github.com/moov-io/watchman) | 更轻量的本地 OFAC/全球制裁筛查引擎，适合自建匹配流程。 | 直接安装 | 本地 | 无特定平台 | 仓库审阅 | 无特别提示 |
| 关键备选 | [TracyWang95/DataInftra-CrossBoardTrustedDataPace-SanctionScreening](https://github.com/TracyWang95/DataInftra-CrossBoardTrustedDataPace-SanctionScreening) | 更偏跨境数据空间与律师工作流，但当前只完成仓库审阅。 | 直接安装 | 本地 | 无特定平台 | 仓库审阅 | 无特别提示 |

[查看该能力的完整索引](CATALOG.md#cross-border-arbitration)

### 国际商事仲裁

**比较口径**：要求至少覆盖程序管理、书状、证据、庭审或裁决书工作流，不用域外法检索项目代替。  ·  **大类能力池**：8 项

> **缺口**：当前索引只有域外法、制裁和跨境合同最近邻，缺成熟中文开源国际仲裁全流程。

当前没有达到推荐或关键备选门槛的项目。


<a id="law-firm-operations"></a>

## 律所与案件运营

个人案件提醒、案件管理和律所工作流。

### 个人律师开庭提醒与卷宗看板

**比较口径**：只比较个人律师的开庭/期限提醒、传票解析、卷宗看板和本地数据路径。  ·  **大类能力池**：14 项

| 定位 | 项目 | 适用差异 | 上手 | 数据路径 | 依赖 | 核验 | 注意事项 |
|---|---|---|---|---|---|---|---|
| 当前推荐 | [AzureTsui/GiGi](https://github.com/AzureTsui/GiGi) | 本地优先，聚焦个人律师开庭提醒、传票解析和卷宗看板。 | 需账号/API | 本地+联网 | 外部 LLM | 仓库审阅 | 无特别提示 |

[查看该能力的完整索引](CATALOG.md#law-firm-operations)

### 中小律所案件与执业管理

**比较口径**：比较收案、冲突检索、案件跟进、财务、结案归档、委托/立案材料和部署成本。  ·  **大类能力池**：14 项

| 定位 | 项目 | 适用差异 | 上手 | 数据路径 | 依赖 | 核验 | 注意事项 |
|---|---|---|---|---|---|---|---|
| 当前推荐 | [lawflow-boop/LawLink](https://github.com/lawflow-boop/LawLink) | 自部署案件和执业管理功能完整，仓库含 18 个测试文件。 | 需账号/API | 本地+联网 | 元典 | 仓库审阅 | 无特别提示 |
| 关键备选 | [Lawyer-ray/FachuanHybridSystem](https://github.com/Lawyer-ray/FachuanHybridSystem) | 更大型的一体化律师工作台，覆盖送达、立案、委托材料和知识库，但数据流更复杂。 | 需账号/API | 本地+联网 | 企查查、天眼查、外部 LLM | 仓库审阅 | 涉及登录态或访问令牌，使用前核验获取方式与平台条款；发现自动上传或遥测描述，处理客户材料前需复核数据流 |

[查看该能力的完整索引](CATALOG.md#law-firm-operations)


<a id="tax-bankruptcy-realestate"></a>

## 税务、破产与房地产

中国法专用成熟项目仍然稀缺。

### 中国税法与税务合规

**比较口径**：只比较中国税法研究、税务合规、争议与申报工作流，不用发票 API 或多法域税务库代表。  ·  **大类能力池**：4 项

> **缺口**：尚无达到中国税法实务推荐门槛的开源项目。

当前没有达到推荐或关键备选门槛的项目。

### 破产申报、重整与清算

**比较口径**：比较债权申报、审查、重整计划、管理人工作和清算流程。  ·  **大类能力池**：4 项

> **缺口**：完整索引中尚无达到推荐门槛的中国破产实务项目。

当前没有达到推荐或关键备选门槛的项目。

### 房地产与建设工程

**比较口径**：比较不动产交易、租赁、建设工程合同、结算和索赔工作流。  ·  **大类能力池**：4 项

> **缺口**：完整索引中尚无达到推荐门槛的中国房地产/工程法项目。

当前没有达到推荐或关键备选门槛的项目。

### 税务与发票技术参考

**比较口径**：只作邻近资源，不上调为中国税法实务推荐。  ·  **大类能力池**：4 项

| 定位 | 项目 | 适用差异 | 上手 | 数据路径 | 依赖 | 核验 | 注意事项 |
|---|---|---|---|---|---|---|---|
| 关键备选 | [openaccountants/openaccountants](https://github.com/openaccountants/openaccountants) | 多法域税务 Skill 参考库。 | 直接安装 | 自托管 | 无特定平台 | 仓库审阅 | 无特别提示 |
| 关键备选 | [fapiaoapi/invoice](https://github.com/fapiaoapi/invoice) | 中国发票接口技术底座，不是税务法律工作流。 | 需部署 | 未明确 | 无特定平台 | 仓库审阅 | 涉及登录态或访问令牌，使用前核验获取方式与平台条款；GitHub 未识别许可证，复制、修改或分发前需另行核验 |

[查看该能力的完整索引](CATALOG.md#tax-bankruptcy-realestate)
