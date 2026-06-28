<div align="center">

<picture>
  <source media="(prefers-color-scheme: light)" srcset="assets/logo-light.svg">
  <img src="assets/logo.svg" width="96" alt="awesome-legal-ai-zh">
</picture>

# ⚖️ awesome-legal-ai-zh · 法律人开源工具箱

[![Awesome](https://awesome.re/badge.svg)](https://awesome.re)
![Resources](https://img.shields.io/badge/已收录-268_仓-3a5a8c)
![Verified](https://img.shields.io/badge/数据-gh_api_实测-2e8b57)
![License](https://img.shields.io/badge/本清单-CC0--1.0-9aa0ab)
![Updated](https://img.shields.io/badge/快照-2026--06--28-b5462f)

**给中国律师 / 法务的一站式开源 AI 工具地图——按你的工作场景，找到能直接装、能直接用的东西。**

办合同、打官司、做尽调、查企业、写文书、运营公众号……每个环节有哪些现成开源 Skill / 工具，这里都帮你找好、标好、验好。

🧑‍⚖️ **本仓维护者也开源了**：[文格 · 法律文书模板执行](https://github.com/lilialla/legal-document-format-skill) · [请求权基础分析](https://github.com/lilialla/request-right-skill-reference) · [股权转让审核](https://github.com/lilialla/equity-transfer-review-skill)（见 [1.2](#12-合同--交易--文书)、[1.6](#16-公司--投融资--并购--尽调--证券)）

</div>

---

## 🚀 怎么用这个仓

1. **按场景找**：在下面[目录](#-目录)里点你当下要做的事（如「合同」「尽调」「公众号」），直接跳到对应清单。
2. **看懂一行**：每条标了 `类型 · ★热度 · 能否商用 · 干嘛的`，30 秒判断要不要用。
3. **拿来用**：
   - 标 `🧩Skill` 的——进到它 GitHub 仓，按 README 把 skill 包放进 Claude Code / 龙虾(OpenClaw) / Codex 的 skills 目录即可调用；
   - 标 `🔌MCP` 的——按仓库说明配到你的 MCP 客户端；
   - 标 `🛠️工具 / 🏛️平台` 的——多为可自部署的应用，照仓库部署文档跑起来。
4. **能不能商用**先看 `能否商用` 列：✅ 可商用 ｜ ⚠️ 有传染性(GPL/AGPL，独立用可，混进闭源产品不行) ｜ ❌ 仅个人/仅链接(无 license 或非商用协议)。

> 📖 **类型图例**：🏛️平台/套件（功能全、规模大） · 🧩Skill/Agent（单点能力，即装即用） · 🔌MCP（数据/工具接口） · 🛠️工具/应用 · 📊数据/语料/评测 · 🧠模型 · 📚清单/范本/资源。
> 其它标记：⭐头部 · 💎小众精品 · 🧑‍⚖️维护者出品 · 🔒脱敏/合规 · ❄️已停更（但范本/数据/字体类停更仍可用） · 🗄️已归档。
> 所有 `★ / license / 能否商用` 由 `gh api` 实测，可用 [`scripts/refresh-stars.sh`](scripts/refresh-stars.sh) 一键刷新；**本仓只做链接索引、不搬运任何代码或文章正文**（[合规说明](COMPLIANCE.md)）。

## 🗂️ 目录

- **一、按法律业务找 Skill**<br/>[综合套件](#11-综合套件与平台) · [合同·文书](#12-合同--交易--文书) · [知产·软著·专利·竞争法](#13-知识产权--软著--专利--竞争法) · [诉讼·刑事·行政·执行](#14-诉讼--刑事--行政--执行) · [涉外·国际仲裁](#15-涉外--国际仲裁) · [公司·投融资·并购·尽调·证券](#16-公司--投融资--并购--尽调--证券) · [数据合规·脱敏](#17-数据合规--隐私--脱敏) · [劳动·家事·个人](#18-劳动--家事--个人-c-端) · [税务·破产·房地产](#19-税务--破产--房地产)
- **二、法律检索与数据**<br/>[检索·案例·MCP](#21-法规--案例检索--mcp) · [企业核查](#22-企业核查企查查--天眼查--网核) · [数据集·评测](#23-数据集--评测--语料) · [法律大模型](#24-中文法律大模型)
- **三、律所运营**<br/>[案件管理·计费·CRM](#31-案件管理--计费--crm)
- **四、内容与个人 IP**<br/>[自媒体全流程](#41-自媒体全流程) · [PPT·演示](#42-ppt--演示) · [配图·插画·图标·设计](#43-配图--插画--图标--设计) · [图表·可视化](#44-图表--可视化) · [字体](#45-字体)
- **五、技术基础（AI 上手）**<br/>[RAG·框架](#51-rag--框架) · [提示词·Skill 编写](#52-提示词--skill-编写) · [通用 Skill 合集](#53-通用-skill-合集) · [中文 LLM 入门](#54-中文-llm-入门--ai-导航)
- **六、资源导航**<br/>[Awesome 清单](#61-awesome-清单) · [平台](#62-平台) · [微信公众号长尾源](#63-微信公众号长尾源)

---

# 一、按法律业务找 Skill

## 1.1 综合套件与平台

> 一套装好、覆盖多业务的"全家桶"，新手从这里入门最快。

| 项目 | 类型 | ★ | 商用 | 干嘛的 |
|---|--|--|:--:|--|
| [anthropics/claude-for-legal](https://github.com/anthropics/claude-for-legal) | 🏛️平台 | 8486 | ✅ | ⭐Anthropic 官方法律套件，80+ agent / 12 plugin / ~20 MCP |
| [anthropics/knowledge-work-plugins](https://github.com/anthropics/knowledge-work-plugins) | 🏛️平台 | 21908 | ✅ | ⭐官方知识工作插件集（含 legal 工作流） |
| [zubair-trabzada/ai-legal-claude](https://github.com/zubair-trabzada/ai-legal-claude) | 🏛️套件 | 1481 | ❌ | 14 skill + 5 agent：合同/NDA/合规/谈判/PDF |
| [CSlawyer1985/claude-for-legal-ZH](https://github.com/CSlawyer1985/claude-for-legal-ZH) | 🏛️套件 | 497 | ✅ | ⭐官方版的中国法适配 + 元典 MCP，覆盖 12 法域 |
| [zhou210712/claude-for-legal-ZH](https://github.com/zhou210712/claude-for-legal-ZH) | 🏛️套件 | 108 | ✅ | 另一作者的中国法 Claude 工作层（公司/商事/IP/劳动/AI治理多域插件） |
| [yuandian-ailaw/Agent-for-legal-cn](https://github.com/yuandian-ailaw/Agent-for-legal-cn) | 🏛️套件 | 10 | ⚠️ | ⭐**元典官方**：claude-for-legal 中国法本地化套件（Apache） |
| [leo123-tto/legal-ai](https://github.com/leo123-tto/legal-ai) | 🏛️套件 | 0 | ✅ | 💎刘成律师·本地法律知识库增强包：legal-kb + 元典检索 + MinerU OCR + ZIP 导入导出，共享给法律人使用（MIT，法律元力工具包） |
| [cat-xierluo/legal-skills](https://github.com/cat-xierluo/legal-skills) | 🏛️套件 | 398 | ❌ | 💎杨卫薪律师，47 个面向法律人的 Skills |
| [pa1nrui1/legal-skills](https://github.com/pa1nrui1/legal-skills) | 🏛️套件 | 19 | ✅ | 💎潘睿律师·中文法律工作 Skill 集合：59 个 SKILL.md，覆盖咨询/诉讼/刑辩/劳动/破产/合同/合规/检索/文书交付 |
| [THUYRan/Legal-Skills-Chinese](https://github.com/THUYRan/Legal-Skills-Chinese) | 🏛️套件 | 321 | ❌ | 清华系 38 个律师手验的法律推理 skill（非商用协议） |
| [evolsb/claude-legal-skill](https://github.com/evolsb/claude-legal-skill) | 🧩Skill | 340 | ✅ | CUAD 风险检测合同审查，兼容 26+ 工具 |
| [cat-xierluo/SuitAgent](https://github.com/cat-xierluo/SuitAgent) | 🧩Agent | 186 | ⚠️ | 诉讼分析 10-SubAgent 系统 |
| [TracyWang95/legal-prompts-for-gpt](https://github.com/TracyWang95/legal-prompts-for-gpt) | 📚提示词 | 381 | ✅ | 💎律师开源的法律提示词集 |
| [TracyWang95/AnythingButLaw](https://github.com/TracyWang95/AnythingButLaw) | 🧩Skill | 36 | ✅ | 给律师的非法律商业分析（博弈/估值/财报） |
| [legalskill/legalskill](https://github.com/legalskill/legalskill) | 📚社区 | 6 | ✅ | 律锥·legalskill 社区组织 |
| [cat-xierluo/opc-legal-counsel.skill](https://github.com/cat-xierluo/opc-legal-counsel.skill) | 🧩Skill | 10 | ⚠️ | 一人公司/小微企业开源法律顾问 |
| [MAXXXXXLI/workbuddy-cn-legal-skills](https://github.com/MAXXXXXLI/workbuddy-cn-legal-skills) | 🏛️套件 | 4 | ✅ | WorkBuddy 中国法适配（合同/数据/劳动/IP/争议） |
| [gcheng001/legal-skills](https://github.com/gcheng001/legal-skills) | 🏛️套件 | 1 | ✅ | 💎27 个 skill：民诉九步法 + 刑辩 + 文书自动化 |
| [choosemoon/legal-skills](https://github.com/choosemoon/legal-skills) | 🏛️套件 | 3 | ✅ | 💎四大法学名家 832 篇论文蒸馏的法学 AI 技能库 |
| [zeweihan/aiworkdeck](https://github.com/zeweihan/aiworkdeck) | 🏛️平台 | 54 | ⚠️ | 💎AI 原生「律师版 VS Code」工作台：案件/文件树 + Agent + 插件 + WPS 在线编辑 + OCR + 证据链（AGPLv3 可私有化） |
| [sunyifeisb-art/legalwork](https://github.com/sunyifeisb-art/legalwork) | 🏛️套件 | 6 | ❌ | LegalWork 本地优先法律 AI 工作台：70+ 法律技能 + 智能 OCR + 文件脱敏 + 案件管理（bytelegal.cn） |
| [abaiar/-LexAI](https://github.com/abaiar/-LexAI) | 🛠️平台 | 21 | ❌ | 小理智法 AI 法律咨询平台：咨询/合同审查/起草/对比/文书解读，LangChain Agent + 得理法律数据库检索 |
| [Hill-1024/Lawyance](https://github.com/Hill-1024/Lawyance) | 🛠️平台 | 1 | ⚠️ | 中文法律 AI 助手原型：法条/案例检索、企业信息、PDF/Word 处理、对话记忆、模拟法庭与 React/FastAPI 工作区（AGPLv3） |

## 1.2 合同 · 交易 · 文书

> 审合同、改合同、生成文书、出裁判文书。

| 项目 | 类型 | ★ | 商用 | 干嘛的 |
|---|--|--|:--:|--|
| [lilialla/legal-document-format-skill](https://github.com/lilialla/legal-document-format-skill) | 🧩Skill | 9 | ✅ | 🧑‍⚖️**维护者出品**·「文格」：按 Word 模板生成/批处理/校验法律文书，含格式门禁 |
| [lilialla/request-right-skill-reference](https://github.com/lilialla/request-right-skill-reference) | 🧩Skill | 8 | ⚠️ | 🧑‍⚖️**维护者出品**·请求权基础（鉴定式案例分析）：谁向谁请求什么→要件→抗辩→证据 |
| [katejianglaw/refine-legal-chinese](https://github.com/katejianglaw/refine-legal-chinese) | 🧩Skill | 5 | ✅ | 💎「法言法语」法律中文改写/审校：保留事实、立场与法律效果，术语辨析 + 质量清单 |
| [he-yufeng/ContractGuard](https://github.com/he-yufeng/ContractGuard) | 🧩工具 | 172 | ✅ | 中文合同 red flag + 公平度评分（A+~F） |
| [CSlawyer1985/contract-review-pro](https://github.com/CSlawyer1985/contract-review-pro) | 🧩Skill | 169 | ❌ | 律师做的合同审查 |
| [zh-xx/legal-assistant-skills](https://github.com/zh-xx/legal-assistant-skills) | 🧩Skill | 139 | ✅ | 合同 + 广告合规 + 请求权可视化 |
| [xiaodingfeng/contract-review](https://github.com/xiaodingfeng/contract-review) | 🛠️应用 | 101 | ✅ | 合同审查（Vue 全栈） |
| [Xigua9xi/ai-legal-review-skillkit](https://github.com/Xigua9xi/ai-legal-review-skillkit) | 🧩Skill | 2 | ✅ | 中文合同审查 workflow 模板基座：SKILL.md + 公开规则/profiles/schema/fixtures/tests，适合私有 fork 二次开发 |
| [CSlawyer1985/excellent-judgment-doc-skill](https://github.com/CSlawyer1985/excellent-judgment-doc-skill) | 🧩Skill | 25 | ❌ | 裁判文书生成 / 质量评判 |
| [Daknniel-0881/qulv-china-legal-counsel-skill](https://github.com/Daknniel-0881/qulv-china-legal-counsel-skill) | 🧩Skill | 5 | ✅ | 💎内置 2189 条法规知识库的法律顾问 |
| [MarvinLann/contract-cleaner](https://github.com/MarvinLann/contract-cleaner) | 🧩Skill | 4 | ✅ | 中文合同文本清洗/格式化（术语·语法纠正） |
| [brucecbi/nda-review-skill](https://github.com/brucecbi/nda-review-skill) | 🧩Skill | 0 | ✅ | NDA 保密协议审查 |
| [cat-xierluo/contract-copilot.skill](https://github.com/cat-xierluo/contract-copilot.skill) | 🧩Skill | 17 | ⚠️ | 合同起草审查（三层分析+四步，杨卫薪律师） |
| [evolsb/legal-redline-tools](https://github.com/evolsb/legal-redline-tools) | 🧩工具 | 38 | ✅ | 💎合同红线交付：生成 tracked-changes Word + 红线 PDF |
| [TracyWang95/DataInfra-Agentic-Contract-Filler-Skill](https://github.com/TracyWang95/DataInfra-Agentic-Contract-Filler-Skill) | 🧩Skill | 7 | ❌ | 国家数据局合同自动填写（Tracy） |

## 1.3 知识产权 · 软著 · 专利 · 竞争法

| 项目 | 类型 | ★ | 商用 | 干嘛的 |
|---|--|--|:--:|--|
| [Fokkyp/SoftwareCopyright-Skill](https://github.com/Fokkyp/SoftwareCopyright-Skill) | 🧩Skill | 4013 | ✅ | 💎软件著作权申请材料生成 |
| [handsomestWei/patent-disclosure-skill](https://github.com/handsomestWei/patent-disclosure-skill) | 🧩Skill | 2859 | ✅ | 💎专利技术交底书（含🔒脱敏 + 国知局查新） |
| [cat-xierluo/trademark-assistant.skill](https://github.com/cat-xierluo/trademark-assistant.skill) | 🧩Skill | 1 | ❌ | 商标申请类别规划与可注册性初筛 |
| [ettajingruyang/PRC-merger-control-assessment](https://github.com/ettajingruyang/PRC-merger-control-assessment) | 🧩Skill | 0 | ❌ | 💎**反垄断/竞争法**：经营者集中申报评估（艾塔法律AI实验室·Etta/Jingru Yang） |
| [cat-xierluo/code2patent.skill](https://github.com/cat-xierluo/code2patent.skill) | 🧩Skill | 1 | ⚠️ | 代码仓库转发明专利交底材料 |
| [cat-xierluo/patent-analysis.skill](https://github.com/cat-xierluo/patent-analysis.skill) | 🧩Skill | 3 | ⚠️ | 专利侵权评估/权利要求比对（7 场景） |
| [CNIPA/PatentDatabases](https://github.com/CNIPA/PatentDatabases) | 📚清单 | 412 | ⚠️ | 个人整理的全球专利数据库 URL 清单（账户名 CNIPA，非官方机构） |
## 1.4 诉讼 · 刑事 · 行政 · 执行

> ℹ️ 这块开源**以「判决/量刑预测」学术数据集为主**；面向律师的刑辩辩护词、行政诉讼、执行成品 skill 目前较少，下面是可复用的数据底座。

| 项目 | 类型 | ★ | 商用 | 干嘛的 |
|---|--|--|:--:|--|
| [thunlp/CAIL](https://github.com/thunlp/CAIL) | 📊数据 | 511 | ✅ | 法研杯·量刑预测数据集（268 万刑事文书） |
| [Dai-shen/LAiW](https://github.com/Dai-shen/LAiW) | 📊数据 | 91 | ✅ | 中文法律 LLM 14 任务基准 + 指令微调数据 |
| [PolarisRisingWar/LJP_Collection](https://github.com/PolarisRisingWar/LJP_Collection) | 📊数据 | 64 | ❌ | 判决/刑期预测模型可复现合集 |
| [lololo-xiao/MultiJustice-MPMCP](https://github.com/lololo-xiao/MultiJustice-MPMCP) | 📊数据 | 5 | ✅ | 💎多被告多罪名判决预测数据集 |
| [SimbaCD/legal-period-manager-skills](https://github.com/SimbaCD/legal-period-manager-skills) | 🧩Skill | 9 | ✅ | 💎杜思敏律师·诉讼/劳动仲裁/**执行**/待办 期限管家 |
| [xtgmf/minfadian](https://github.com/xtgmf/minfadian) | 🧩Skill | 1 | ✅ | 民法典 Skills（数字法务专家） |
| [Youchu-lawhub/gutachten-civil-case](https://github.com/Youchu-lawhub/gutachten-civil-case) | 🧩Skill | 36 | ❌ | 💎民法典请求权基础·德国鉴定式案例研习报告（留空白能力槽接自配 MCP/知识库，游初） |
| [Youchu-lawhub/gutachten-criminal-case](https://github.com/Youchu-lawhub/gutachten-criminal-case) | 🧩Skill | 10 | ✅ | 💎鉴定式刑法案例研习：三阶层犯罪论、罪名发现、双闸确认、并行写作、法条校验与 Word 输出（Apache 文本，GitHub 未自动识别） |
| [yuhudie598-dev/legal-case-analysis-plus](https://github.com/yuhudie598-dev/legal-case-analysis-plus) | 🧩Skill | 0 | ❌ | 💎龚家勇律师·案件分析报告（法律关系分析法 Plus）：接华宇元典 MCP 检索法规/案例/法答网，按法律关系分析法输出结构化报告（无 license） |
| [CSlawyer1985/case-type-guide](https://github.com/CSlawyer1985/case-type-guide) | 🧩Skill | 12 | ❌ | 💎类案办案要件指南（案件类型识别+要件式清单） |
| [yxk-lawyer/litigation-prep-skill-cn](https://github.com/yxk-lawyer/litigation-prep-skill-cn) | 🧩Skill | 10 | ❌ | 💎CorpClaim CN·公司民商事诉讼指导：案由→请求权基础→构成要件→证据清单→诉讼策略（执业律师，无 license） |
## 1.5 涉外 · 国际仲裁

> 中文涉外/国际商事仲裁的成熟开源**还很少**；这里收可复用的「最近邻」——制裁筛查、多法域法源、跨境数据。

| 项目 | 类型 | ★ | 商用 | 干嘛的 |
|---|--|--|:--:|--|
| [opensanctions/opensanctions](https://github.com/opensanctions/opensanctions) | 📊数据 | 753 | ✅ | 跨境制裁/PEP/监视名单（337 源），涉外尽调底座 |
| [moov-io/watchman](https://github.com/moov-io/watchman) | 🛠️工具 | 475 | ✅ | OFAC/全球制裁筛查引擎（生产级） |
| [worldwidelaw/legal-sources](https://github.com/worldwidelaw/legal-sources) | 🛠️工具 | 285 | ⚠️ | 110+ 国政府法源抓取脚本 |
| [TracyWang95/DataInftra-CrossBoardTrustedDataPace-SanctionScreening](https://github.com/TracyWang95/DataInftra-CrossBoardTrustedDataPace-SanctionScreening) | 🧩Skill | 15 | ✅ | 💎律师做的跨境可信数据空间 + 进出口制裁筛查 |
| [Sociovestix/lenu](https://github.com/Sociovestix/lenu) | 🛠️工具 | 22 | ✅ | ISO 20275 跨 200+ 法域实体法律形式识别 |
| [spartypkp/open-source-legislation](https://github.com/spartypkp/open-source-legislation) | 📊数据 | 17 | ❌ | 50+ 法域立法统一成 SQL 知识图谱 |
| [imchongliu/foreign-law-research](https://github.com/imchongliu/foreign-law-research) | 🧩Skill | 8 | ✅ | 💎域外法律研究 skill（刘冲律师·涉外） |
## 1.6 公司 · 投融资 · 并购 · 尽调 · 证券

> 资源分散在 GitHub 英文、GitHub 中文、微信公众号三层，这里尽量汇齐。**仍较少**：中国境内股权设计/对赌/ESOP 专用 skill。

| 项目 | 类型 | ★ | 商用 | 干嘛的 |
|---|--|--|:--:|--|
| [anthropics/financial-services](https://github.com/anthropics/financial-services) | 🏛️平台 | 32450 | ✅ | ⭐官方金融插件，PE 含 dd-checklist / dd-meeting-prep |
| [papermark/papermark](https://github.com/papermark/papermark) | 🛠️应用 | 8646 | ⚠️ | 💎开源数据室（DocSend 替代，水印/密码/逐页分析） |
| [AI4Finance-Foundation/FinRobot](https://github.com/AI4Finance-Foundation/FinRobot) | 🛠️Agent | 7380 | ✅ | 金融/财报分析多 agent 平台 |
| [dgunning/edgartools](https://github.com/dgunning/edgartools) | 🛠️工具 | 2394 | ✅ | SEC 申报分析（10-K/8-K/XBRL/Form 3-4-5） |
| [captableinc/captable](https://github.com/captableinc/captable) | 🛠️应用 | 816 | ⚠️ | 股权表 + 数据室（Carta/Pulley 替代） |
| [stefanoamorelli/sec-edgar-mcp](https://github.com/stefanoamorelli/sec-edgar-mcp) | 🔌MCP | 326 | ⚠️ | SEC EDGAR 的 MCP server |
| [SEC-API-io/sec-api-python](https://github.com/SEC-API-io/sec-api-python) | 🛠️工具 | 309 | ✅ | SEC 数据 SDK（2000万+ 申报、招股书） |
| [LLMQuant/awesome-trading-agents](https://github.com/LLMQuant/awesome-trading-agents) | 📚清单 | 317 | ✅ | LLM 金融 agent/MCP 清单 |
| [Open-Cap-Table-Coalition/Open-Cap-Format-OCF](https://github.com/Open-Cap-Table-Coalition/Open-Cap-Format-OCF) | 📊标准 | 181 | ❌ | 开源股权结构数据标准 |
| [Ro5s/Startup-Starter-Pack](https://github.com/Ro5s/Startup-Starter-Pack) | 📚范本 | 112 | ❌ | ❄️融资范本集（YC SAFE/term sheet/期权，范本不过时） |
| [LLMQuant/skills](https://github.com/LLMQuant/skills) | 🧩Skill | 139 | ✅ | 华尔街金融投资 Skills 库（财报/估值/监管） |
| [Azure-Samples/ally-legal-assistant](https://github.com/Azure-Samples/ally-legal-assistant) | 🛠️工具 | 78 | ❌ | 合同分析/自动批注 Word 插件 |
| [zoharbabin/due-diligence-agents](https://github.com/zoharbabin/due-diligence-agents) | 🧩Agent | 52 | ✅ | 💎M&A 尽调 13 agent（读数据室、交叉引证、定位页码） |
| [skala-io/legal-skills](https://github.com/skala-io/legal-skills) | 🧩Skill | 41 | ✅ | 💎Skala（skala.io）创业法 11 skill：SAFE/SAFT/term sheet 审查·Reg S 离岸发行·startup 尽调·辖区选择（Delaware/Cayman/BVI/新加坡） |
| [sboghossian/master-claude-for-legal](https://github.com/sboghossian/master-claude-for-legal) | 🧩Skill | 40 | ⚠️ | M&A 尽调 tabular-review + 多方版本 diff |
| [lilialla/equity-transfer-review-skill](https://github.com/lilialla/equity-transfer-review-skill) | 🧩Skill | 0 | ✅ | 🧑‍⚖️**维护者出品**·股权/股份/持股平台份额转让审查：交易类型分流 + 出资责任 + 税务/外汇 + 监管闸门 + 交割条件 |
| [chaunsin/go-qcc-sdk](https://github.com/chaunsin/go-qcc-sdk) | 🛠️工具 | 1 | ✅ | 企查查 SDK（失信/被执行核查） |
| [malnlda/legal-due-diligence](https://github.com/malnlda/legal-due-diligence) | 🧩Skill | 2 | ❌ | 💎中国法律尽职调查 skill（莫成哲） |
> 💡 中国语境的决议/尽调表/披露清单，[claude-for-legal-ZH](https://github.com/CSlawyer1985/claude-for-legal-ZH) 的 corporate-legal 插件最对口；VIE 协议生成 Skill 由艾塔法律AI实验室经微信发放（见 [6.3 微信长尾源](#63-微信公众号长尾源)）。Anthropic 官方知识工作插件见 [1.1](#11-综合套件与平台)，企业网核 ENScan_GO 见 [2.2](#22-企业核查企查查--天眼查--网核)。
> ⚠️ 本表 SEC/EDGAR/华尔街金融多为**美国证券/海外金融**工具，属涉外参考；中国境内股权设计/公司治理资源仍较少。

## 1.7 数据合规 · 隐私 · 脱敏

| 项目 | 类型 | ★ | 商用 | 干嘛的 |
|---|--|--|:--:|--|
| [microsoft/presidio](https://github.com/microsoft/presidio) | 🛠️框架 | 9618 | ✅ | ⭐🔒PII 检测/脱敏/匿名化框架，行业标准 |
| [allenymt/PrivacySentry](https://github.com/allenymt/PrivacySentry) | 🛠️工具 | 2278 | ✅ | Android 隐私合规整改检测 |
| [TongchengOpenSource/AppScan](https://github.com/TongchengOpenSource/AppScan) | 🛠️工具 | 1112 | ✅ | 企业级 App 隐私合规检测 |
| [TracyWang95/DataInfra-RedactionEverything](https://github.com/TracyWang95/DataInfra-RedactionEverything) | 🧩Skill | 888 | ❌ | 💎🔒律师做的「脱敏一切」（本地 LLM 脱敏） |
| [ethyca/fides](https://github.com/ethyca/fides) | 🛠️平台 | 465 | ✅ | GDPR/CCPA/LGPD 数据主体请求(DSAR)编排 |
| [philterd/phileas](https://github.com/philterd/phileas) | 🛠️工具 | 97 | ✅ | PII/PHI 去标识（HIPAA/GDPR/CCPA） |
| [moyupeng0422/legal-doc-redactor](https://github.com/moyupeng0422/legal-doc-redactor) | 🛠️工具 | 94 | ✅ | 💎🔒彭雨诗律师·离线法律文档脱敏/还原：docx 批量一致替换、白黑名单、自定义类型、保留外部审阅痕迹 |
| [youdianzhineng-ailaw/privacy-policy-self-service-generator-mvp](https://github.com/youdianzhineng-ailaw/privacy-policy-self-service-generator-mvp) | 🧩Skill | 12 | ⚠️ | 💎隐私协议 MVP 生成器（面向 OPC/founder，事实采集→合规校验→生成复查；于泽辉律师·有点智能事务所，已预告 v2/v3） |
| [yuhudie598-dev/online-store-webpage-and-other-e-commerce-information-ai-proofreading-plus](https://github.com/yuhudie598-dev/online-store-webpage-and-other-e-commerce-information-ai-proofreading-plus) | 🧩Skill | 0 | ❌ | 龚家勇律师·电商信息 AI 校对 Plus：营业执照/商标/产品资料与网店/网页逐项差异比对，辅助法务/合规核查（无 license） |
| [LianXU-321/china-outbound-service-dpa-bilingual](https://github.com/LianXU-321/china-outbound-service-dpa-bilingual) | 🧩Skill | 0 | ⚠️ | 💎艾塔法律AI实验室·徐莲（LianXU）·出海数据处理协议：中英双语 DPA，覆盖 GDPR/UK/CCPA/PIPL 四套规则（包内 LICENSE 与 metadata 许可口径需复核） |

## 1.8 劳动 · 家事 · 个人 C 端

> ⚠️ 多为法条数据库/计算器，**离婚分割、继承份额、债务测算等成品 skill 还缺**（可基于 LawRefBook/Laws 自建）。

| 项目 | 类型 | ★ | 商用 | 干嘛的 |
|---|--|--|:--:|--|
| [996icu/996.ICU](https://github.com/996icu/996.ICU) | 📚资源 | 276319 | ❌ | 劳动维权标志项目（加班违法论证/法条引用） |
| [wangchangwei/arb-skill](https://github.com/wangchangwei/arb-skill) | 🧩Skill | 25 | ⚠️ | 💎劳动仲裁 skill（劳动争议实务） |
| [worker-aid-ai/worker-aid-agent](https://github.com/worker-aid-ai/worker-aid-agent) | 🛠️Agent | 1 | ⚠️ | 💎劳动者权益自助 Agent/Skill：本地 Web + CLI，欠薪/未签合同/违法解除/加班费材料整理与仲裁申请草稿 |
| [jerry046918/labor_rights_skills](https://github.com/jerry046918/labor_rights_skills) | 🧩Skill | 1 | ⚠️ | 💎劳动权益法律顾问 Skill：大陆劳动争议结构化调查、证据采集、法条/类案检索与法律意见书生成，含录音本地 FunASR 处理（Anti-996 条件许可） |
| [RanKKI/LawRefBook](https://github.com/RanKKI/LawRefBook) | 🛠️App | 2434 | ❌ | 法律快查 App（含婚姻/继承编） |
| [hellodigua/code996](https://github.com/hellodigua/code996) | 🛠️工具 | 1995 | ✅ | 💎量化加班证据（commit 时间反推工时） |
| [LawRefBook/Laws](https://github.com/LawRefBook/Laws) | 📊数据 | 1818 | ❌ | 💎法律法规 MD 数据库（民法典婚姻/继承编），计算器底座 |
## 1.9 税务 · 破产 · 房地产

> ⚠️ **严重偏美国法**；中国税务 GitHub 只有个税计算器 + 发票 SDK，无法律级税务 skill。房建可看 [claude-for-legal-ZH](https://github.com/CSlawyer1985/claude-for-legal-ZH)（作者是房建资深合伙人）。

| 项目 | 类型 | ★ | 商用 | 干嘛的 |
|---|--|--|:--:|--|
| [openaccountants/openaccountants](https://github.com/openaccountants/openaccountants) | 🧩Skill | 209 | ⚠️ | 💎371 个税务 skill 覆盖 134 国（中国可扩展） |
| [fapiaoapi/invoice](https://github.com/fapiaoapi/invoice) | 🛠️工具 | 73 | ❌ | 数电/全电发票 SDK（金税·开票接口） |
| [CSOAI-ORG/tax-calculator-ai-mcp](https://github.com/CSOAI-ORG/tax-calculator-ai-mcp) | 🔌MCP | 0 | ✅ | 税额计算 MCP（英/美/欧） |

---

# 二、法律检索与数据

## 2.1 法规 · 案例检索 / MCP

| 项目 | 类型 | ★ | 商用 | 干嘛的 |
|---|--|--|:--:|--|
| [cncases/cases](https://github.com/cncases/cases) | 🛠️工具 | 1031 | ✅ | 💎中国裁判文书本地离线检索 |
| [aa0101181514/tw-legal-rag](https://github.com/aa0101181514/tw-legal-rag) | 🛠️应用 | 175 | ✅ | 台湾法律 RAG |
| [lawchat-oss/mcp-taiwan-legal-db](https://github.com/lawchat-oss/mcp-taiwan-legal-db) | 🔌MCP | 145 | ✅ | 台湾司法院判决 + 法规 MCP |
| [Golden2002/legal-research-skill](https://github.com/Golden2002/legal-research-skill) | 🧩Skill | 116 | ✅ | 法律检索 skill（劳动/合同/侵权/家事/行政/刑事） |
| [yuandian-ailaw/yuandian-mcp-server](https://github.com/yuandian-ailaw/yuandian-mcp-server) | 🔌MCP | 3 | ✅ | **元典官方 MCP Server**：动态注册法规/案例/企业等开放平台 API，需自备 `YUANDIAN_API_KEY` |
| [hisnontright/jiandawang-jicui-consultation](https://github.com/hisnontright/jiandawang-jicui-consultation) | 🧩Skill | 0 | ✅ | 💎检答网集萃第 1–140 批本地检索技能：检察业务/最高检答疑 Markdown 内置，强调可溯源检索与免责声明（MIT） |
| [liuhuanyong/CrimeKgAssitant](https://github.com/liuhuanyong/CrimeKgAssitant) | 📊数据 | 1581 | ❌ | ❄️罪名预测+法律知识图谱+20w 问答（经典） |
| [billvsme/law_ai](https://github.com/billvsme/law_ai) | 🛠️应用 | 226 | ❌ | ❄️LangChain 法律 RAG（200+ 手册+网搜，给出处） |
| [malnlda/legal-research](https://github.com/malnlda/legal-research) | 🧩Skill | 2 | ✅ | 元典法规+案例+分析师组合研究序列 |
| [chouenchieh/china-law](https://github.com/chouenchieh/china-law) | 🧩Skill | 7 | ❌ | 💎中国法律实务 Claude 插件·45 技能·**集成北大法宝** |
| [Liu8Can/pkulaw-mcp-router](https://github.com/Liu8Can/pkulaw-mcp-router) | 🔌MCP | 1 | ✅ | **北大法宝** MCP 多子服务路由 |
| [malnlda/yd-law-search](https://github.com/malnlda/yd-law-search) | 🧩Skill | 1 | ❌ | 元典法规检索 Copilot Skill（调元典 API） |
| [JamesANZ/us-legal-mcp](https://github.com/JamesANZ/us-legal-mcp) | 🔌MCP | 32 | ✅ | 美国立法/判例 MCP |
| [freelawproject/courtlistener-api-client](https://github.com/freelawproject/courtlistener-api-client) | 🔌MCP | 18 | ✅ | 美国 CourtListener 官方 MCP |

## 2.2 企业核查（企查查 / 天眼查 / 网核）

| 项目 | 类型 | ★ | 商用 | 干嘛的 |
|---|--|--|:--:|--|
| [wgpsec/ENScan_GO](https://github.com/wgpsec/ENScan_GO) | 🛠️工具 | 4470 | ✅ | 💎一键聚合企业工商/控股/对外投资/公众号，支持 MCP |
| [tyc-tech/mcp-skills](https://github.com/tyc-tech/mcp-skills) | 🔌MCP | 13 | ❌ | **天眼查 MCP** Skills |
| [duhu2000/vibe-lawyering-qcc](https://github.com/duhu2000/vibe-lawyering-qcc) | 🔌MCP | 6 | ✅ | **企查查 MCP** 增强版·法律人 AI 工具箱 |
| [Ace-Kelly/qcc-mcp-batch](https://github.com/Ace-Kelly/qcc-mcp-batch) | 🔌MCP | 2 | ✅ | **企查查 MCP** 批量抓取（工商/风险/知产 67 字段） |
| [malnlda/yd-enterprise-info](https://github.com/malnlda/yd-enterprise-info) | 🧩Skill | 1 | ❌ | 元典开放平台企业信息查询（22 子命令） |

## 2.3 数据集 · 评测 · 语料

| 项目 | 类型 | ★ | 商用 | 干嘛的 |
|---|--|--|:--:|--|
| [jhpyle/docassemble](https://github.com/jhpyle/docassemble) | 🛠️平台 | 960 | ✅ | 💎法律文书自动化老牌平台 |
| [freelawproject/courtlistener](https://github.com/freelawproject/courtlistener) | 🛠️平台 | 957 | ⚠️ | 美国判例数据库平台 |
| [Liquid-Legal-Institute/Legal-Text-Analytics](https://github.com/Liquid-Legal-Institute/Legal-Text-Analytics) | 📚资源 | 725 | ⚠️ | ❄️法律文本分析方法库 |
| [HazyResearch/legalbench](https://github.com/HazyResearch/legalbench) | 📊评测 | 599 | ❌ | 法律 LLM 评测基准（斯坦福 HazyResearch） |
| [harveyai/biglaw-bench](https://github.com/harveyai/biglaw-bench) | 📊评测 | 165 | ❌ | 💎Harvey AI 官方 BigLaw Bench：律所级真实法律任务评测基准（无明确协议，仅参考/引用） |
| [open-compass/LawBench](https://github.com/open-compass/LawBench) | 📊评测 | 434 | ✅ | 💎中文法律能力评测基准（司法部系+多机构，引用最广） |
| [SKYLENAGE-AI/PLawBench](https://github.com/SKYLENAGE-AI/PLawBench) | 📊评测 | 25 | ❌ | 💎法律实务评测基准（Qwen×阿里AIData×晓天衡宇·13 场景 850 题 12500 条 rubric，模拟真实咨询而非考题） |
| [thunlp/LegalPLMs](https://github.com/thunlp/LegalPLMs) | 🧠模型 | 194 | ❌ | 清华 Lawformer 等长文书法律预训练模型 |
| [THUIR/LeCaRDv2](https://github.com/THUIR/LeCaRDv2) | 📊数据 | 92 | ✅ | 清华大规模中文法律案例检索数据集 v2 |
| [neelguha/legal-ml-datasets](https://github.com/neelguha/legal-ml-datasets) | 📊数据 | 438 | ❌ | 法律 ML 数据集合集 |
| [freelawproject/eyecite](https://github.com/freelawproject/eyecite) | 🛠️工具 | 251 | ✅ | 💎判例引证解析 |
## 2.4 中文法律大模型

| 项目 | 类型 | ★ | 商用 | 干嘛的 |
|---|--|--|:--:|--|
| [CSHaitao/LexiLaw](https://github.com/CSHaitao/LexiLaw) | 🧠模型 | 1024 | ✅ | 清华 THUIR，ChatGLM-6B 基座法律大模型 |
| [zhihaiLLM/wisdomInterrogatory](https://github.com/zhihaiLLM/wisdomInterrogatory) | 🧠模型 | 547 | ✅ | 🔒智海-录问（浙大） |
| [CSHaitao/LegalOne](https://github.com/CSHaitao/LegalOne) | 🧠模型 | 64 | ✅ | 💎法律推理基座（1.7B/4B/8B） |
| [THUIR/LegalOne-R1](https://github.com/THUIR/LegalOne-R1) | 🧠模型 | 11 | ✅ | LegalOne-R1 法律推理模型系列发布页（1.7B/4B/8B HF 权重；仓库本体以 README/图表为主，低位收录） |
| [PKU-YuanGroup/ChatLaw](https://github.com/PKU-YuanGroup/ChatLaw) | 🧠模型 | 7533 | ⚠️ | ❄️北大袁粒团队，中文法律 LLM 里最出圈的一个 |
| [pengxiao-song/LaWGPT](https://github.com/pengxiao-song/LaWGPT) | 🧠模型 | 6053 | ⚠️ | ❄️中文法律知识微调 LLM（法律语料预训练） |
| [FudanDISC/DISC-LawLLM](https://github.com/FudanDISC/DISC-LawLLM) | 🧠模型 | 932 | ✅ | 复旦 DISC 中文法律大模型 |
| [davidpig/lychee_law](https://github.com/davidpig/lychee_law) | 🧠模型 | 41 | ✅ | ❄️「律知」法律咨询大模型 |
| [siat-nlp/HanFei](https://github.com/siat-nlp/HanFei) | 🧠模型 | 131 | ✅ | ❄️韩非·国内首个全参数训练法律大模型（中科院深圳） |
| [AndrewZhe/lawyer-llama](https://github.com/AndrewZhe/lawyer-llama) | 🧠模型 | 994 | ✅ | ❄️中文法律 LLaMA（律师 llama，经典） |
---

# 三、律所运营

## 3.1 案件管理 · 计费 · CRM

| 项目 | 类型 | ★ | 商用 | 干嘛的 |
|---|--|--|:--:|--|
| [Lawyer-ray/FachuanHybridSystem](https://github.com/Lawyer-ray/FachuanHybridSystem) | 🛠️平台 | 192 | ⚠️ | ⭐💎一线律师自研「法穿 AI Copilot」：法院短信自动解析归档 + 一次生成全套委托材料 + OA/一张网立案 + 本地知识库，Django 6 + React 19 + MCP（127 模型/483 API/35 模块；Elastic 2.0：自用可商用，禁转售为托管服务） |
| [jlawyerorg/j-lawyer-org](https://github.com/jlawyerorg/j-lawyer-org) | 🛠️平台 | 82 | ⚠️ | 德国开源律所管理系统（案件/文档/归档） |
| [createrivabu/Iuris-Soft](https://github.com/createrivabu/Iuris-Soft) | 🛠️平台 | 20 | ❌ | 案件全生命周期 + 开庭管理 + 文档库 |
| [imchongliu/law-firm-worklog](https://github.com/imchongliu/law-firm-worklog) | 🧩Skill | 2 | ✅ | 💎律所工时月报生成（任务→Excel/CSV，刘冲律师） |
| [imchongliu/lpm-skills-zh](https://github.com/imchongliu/lpm-skills-zh) | 🧩Skill | 0 | ✅ | LPM 法律项目管理 14 skill 中文版 |
| [brucecbi/directory-index](https://github.com/brucecbi/directory-index) | 🧩Skill | 1 | ✅ | 本地目录索引器（案卷目录→Markdown） |
| [yuhudie598-dev/workbuddy-calendar](https://github.com/yuhudie598-dev/workbuddy-calendar) | 🧩Skill | 1 | ❌ | 龚家勇律师·WorkBuddy 侧边栏日历：开庭/会议/截止日期等日程增删改查，支持从对话同步事件（无 license） |
| [TracyWang95/awesome-law-firm-design-md](https://github.com/TracyWang95/awesome-law-firm-design-md) | 📚清单 | 4 | ❌ | 律所 DESIGN.md 合集（律所设计规范） |
| [lawflow-boop/LawLink](https://github.com/lawflow-boop/LawLink) | 🛠️平台 | 40 | ✅ | 💎开源自部署中小律所案件与执业管理系统：收案登记、冲突检索、正式案件、持续跟进、财务记录、结案归档、数据导出 |
| [leo123-tto/case-board](https://github.com/leo123-tto/case-board) | 🛠️工具 | 13 | ❌ | 💎律师个人案件可视化看板（macOS 桌面端，Tauri+React；已正式公开源码 v0.3.9，可丢给 AI 自行编译 Windows 版；PolyForm 非商业免费） |

> 小型管理项目还有 `sochetlaw/legalninja`(计费+CRM)、`Oluwablin/law-crm`、`derekgan08/CaseAce`，按需取用。

---

# 四、内容与个人 IP

> 律师做公众号 / 视频号 / 小红书、立个人 IP 用得到的整套工具。两位头部作者撑起这块：**卡兹克（数字生命卡兹克）** 与 **op7418（归藏）**。
> ℹ️ 4.2–4.4 多为**通用**设计/视频/出图工具（非法律专用），按需借用即可。

## 4.1 自媒体全流程

**头部作者 Skill 合集**：[KKKKhazix/khazix-skills](https://github.com/KKKKhazix/khazix-skills)`🧩`(15920·✅·卡兹克 AI Skills 合集) · [KKKKhazix/wechat-article-exporter](https://github.com/KKKKhazix/wechat-article-exporter)`🛠️`(38·❌·公众号文章批量导出)

| op7418（归藏）的 skill | 类型 | ★ | 商用 | 干嘛的 |
|---|--|--|:--:|--|
| [guizang-ppt-skill](https://github.com/op7418/guizang-ppt-skill) | 🧩Skill | 18848 | ⚠️ | AI 生成 HTML 幻灯片 |
| [Humanizer-zh](https://github.com/op7418/Humanizer-zh) | 🧩Skill | 11494 | ✅ | 去 AI 味（汉化版） |
| [CodePilot](https://github.com/op7418/CodePilot) | 🛠️应用 | 6040 | ❌ | 多模型 AI agent 桌面端 |
| [guizang-social-card-skill](https://github.com/op7418/guizang-social-card-skill) | 🧩Skill | 4011 | ⚠️ | 小红书 3:4 配图卡片 |
| [NanoBanana-PPT-Skills](https://github.com/op7418/NanoBanana-PPT-Skills) | 🧩Skill | 3023 | ❌ | AI PPT 图片/视频 |
| [Claude-to-IM-skill](https://github.com/op7418/Claude-to-IM-skill) | 🧩Skill | 2758 | ✅ | Claude 接 IM 平台 |
| [Youtube-clipper-skill](https://github.com/op7418/Youtube-clipper-skill) | 🧩Skill | 2008 | ✅ | YouTube 视频切片 |
| [logo-generator-skill](https://github.com/op7418/logo-generator-skill) | 🧩Skill | 1313 | ❌ | Logo 生成 |
| [Document-illustrator-skill](https://github.com/op7418/Document-illustrator-skill) | 🧩Skill | 557 | ✅ | 文档自动配图（16:9/3:4） |
**排版 / 多平台发布**`🛠️`：[doocs/md](https://github.com/doocs/md)(12896·公众号 MD 编辑器) · [dreammis/social-auto-upload](https://github.com/dreammis/social-auto-upload)(12846·抖音/小红书/视频号自动发) · [wechatsync/Wechatsync](https://github.com/wechatsync/Wechatsync)(5830·⚠️·同步 29+ 平台) · [geekjourneyx/md2wechat-skill](https://github.com/geekjourneyx/md2wechat-skill)(2940)

**视频 / 字幕 / 配音 / 数字人**`🛠️`：[2noise/ChatTTS](https://github.com/2noise/ChatTTS)(39511·⚠️·对话 TTS) · [fishaudio/fish-speech](https://github.com/fishaudio/fish-speech)(30955·TTS 声音克隆) · [FunAudioLLM/CosyVoice](https://github.com/FunAudioLLM/CosyVoice)(21831·阿里多语言 TTS) · [jianchang512/pyvideotrans](https://github.com/jianchang512/pyvideotrans)(18089·⚠️·视频翻译配音) · [WEIFENG2333/VideoCaptioner](https://github.com/WEIFENG2333/VideoCaptioner)(15121·⚠️·智能字幕) · [lipku/LiveTalking](https://github.com/lipku/LiveTalking)(8057·实时数字人) · [WyattBlue/auto-editor](https://github.com/WyattBlue/auto-editor)(4470·自动剪辑) · [SamurAIGPT/AI-Youtube-Shorts-Generator](https://github.com/SamurAIGPT/AI-Youtube-Shorts-Generator)(3997·长视频切爆款)

**SEO**`🧩`：[aaron-he-zhu/seo-geo-claude-skills](https://github.com/aaron-he-zhu/seo-geo-claude-skills)(2254·20 个 SEO/GEO skill) · [TheCraigHewitt/seomachine](https://github.com/TheCraigHewitt/seomachine)(7177)

## 4.2 PPT · 演示

`🛠️/🧩`：[slidevjs/slidev](https://github.com/slidevjs/slidev)(47369·MD 演示) · [hakimel/reveal.js](https://github.com/hakimel/reveal.js)(71809·HTML 演示) · [pipipi-pikachu/PPTist](https://github.com/pipipi-pikachu/PPTist)(9103·⚠️·在线 PPT 编辑) · [presenton/presenton](https://github.com/presenton/presenton)(8517·AI 生成演示) · [gitbrent/PptxGenJS](https://github.com/gitbrent/PptxGenJS)(5746·JS 生成 PPTX) · [icip-cas/PPTAgent](https://github.com/icip-cas/PPTAgent)(4718·Agent 化 PPT) · [marp-team/marp-cli](https://github.com/marp-team/marp-cli)(3661·MD→PPTX) · [scanny/python-pptx](https://github.com/scanny/python-pptx)(3429·Python 生成 PPTX) · [GongRzhe/Office-PowerPoint-MCP-Server](https://github.com/GongRzhe/Office-PowerPoint-MCP-Server)(1809·🔌MCP·🗄️已归档但可用) · [SimbaCD/html-slides-studio](https://github.com/SimbaCD/html-slides-studio)(1·✅·HTML 幻灯片)

## 4.3 配图 · 插画 · 图标 · 设计

**设计工具/平台**`🛠️`：[nexu-io/open-design](https://github.com/nexu-io/open-design)(70747·✅·⭐💎**Open Design**——本地优先的开源 Claude Design 替代) · [penpot/penpot](https://github.com/penpot/penpot)(53537·✅·开源 Figma，设计协作) · [onlook-dev/onlook](https://github.com/onlook-dev/onlook)(26040·✅·「设计师版 Cursor」，AI 可视化设计转代码) · [gridaco/grida](https://github.com/gridaco/grida)(2531·✅·Grida Open Design)

**AI 出图 / 封面**`🛠️`：[Comfy-Org/ComfyUI](https://github.com/Comfy-Org/ComfyUI)(118245·⚠️·节点式出图) · [black-forest-labs/flux](https://github.com/black-forest-labs/flux)(25662·FLUX 文生图) · [vercel/satori](https://github.com/vercel/satori)(13568·HTML→封面图) · [xcollantes/free-stock-images-mcp](https://github.com/xcollantes/free-stock-images-mcp)(3·🔌免费图库 MCP)

**图标 / emoji**`📚`：[tailwindlabs/heroicons](https://github.com/tailwindlabs/heroicons)(23618) · [lucide-icons/lucide](https://github.com/lucide-icons/lucide)(23139) · [tabler/tabler-icons](https://github.com/tabler/tabler-icons)(20990) · [iconoir-icons/iconoir](https://github.com/iconoir-icons/iconoir)(4476) · [jdecked/twemoji](https://github.com/jdecked/twemoji)(1702·emoji)

## 4.4 图表 · 可视化

> 画证据链 / 时间线 / 争点树 / 股权结构图。

`🛠️`：[excalidraw/excalidraw](https://github.com/excalidraw/excalidraw)(126146·手绘白板) · [d3/d3](https://github.com/d3/d3)(113129) · [mermaid-js/mermaid](https://github.com/mermaid-js/mermaid)(88857·文本生成流程图/时序图) · [chartjs/Chart.js](https://github.com/chartjs/Chart.js)(67528) · [apache/echarts](https://github.com/apache/echarts)(66648)

## 4.5 字体

> 法律文书排版常用（仿宋/黑体/宋体）。

`📚`：[google/fonts](https://github.com/google/fonts)(20179) · [adobe-fonts/source-han-sans](https://github.com/adobe-fonts/source-han-sans)(16838·思源黑体) · [adobe-fonts/source-han-serif](https://github.com/adobe-fonts/source-han-serif)(9484·❄️思源宋体) · [notofonts/noto-cjk](https://github.com/notofonts/noto-cjk)(3923) · [kevchentw/awesome-chinese-fonts](https://github.com/kevchentw/awesome-chinese-fonts)(48·中文字体清单)

---

# 五、技术基础（AI 上手）

> 不懂技术也想用好 AI？从这里补基础：怎么写提示词、怎么写/装 skill、怎么入门大模型。

## 5.1 RAG / 框架

**RAG / Agent 数据底座**：[HKUDS/RAG-Anything](https://github.com/HKUDS/RAG-Anything)`🛠️`(21568·✅·港大 all-in-one RAG 框架) · [Zleap-AI/SAG](https://github.com/Zleap-AI/SAG)(1606·✅·面向 Agent 的增量写入/多跳检索数据底座) · [VectifyAI/PageIndex](https://github.com/VectifyAI/PageIndex)(33391·✅·Vectorless reasoning-based RAG 文档索引) · [SciPhi-AI/R2R](https://github.com/SciPhi-AI/R2R)(7894·✅·生产级 Agentic RAG / REST API)

**文档解析 / OCR / PDF**（律师案卷/扫描件转文字）：[opendatalab/MinerU](https://github.com/opendatalab/MinerU)`🛠️`(68913·⚠️·PDF→Markdown/OCR，中文案卷首选) · [PaddlePaddle/PaddleOCR](https://github.com/PaddlePaddle/PaddleOCR)(83734·✅·PP-OCR/文档解析/表格与版面识别，100+ 语言) · [baidu/Unlimited-OCR](https://github.com/baidu/Unlimited-OCR)(6667·✅·长文档 one-shot OCR，OmniDocBench SOTA，模型/代码已开源) · [deepseek-ai/DeepSeek-OCR](https://github.com/deepseek-ai/DeepSeek-OCR)(23379·✅·视觉文本压缩 OCR，长文档解析底座) · [microsoft/markitdown](https://github.com/microsoft/markitdown)(158829·✅·各类文档→Markdown) · [handsomestWei/red-seal-ocr](https://github.com/handsomestWei/red-seal-ocr)(1·✅·🔒印章/红章文字识别) · [cyontheway/word-replacer](https://github.com/cyontheway/word-replacer)(0·✅·🔒Word 号码/字段批量脱敏替换) · [cyontheway/pdf-watermark-tool](https://github.com/cyontheway/pdf-watermark-tool)(0·✅·离线 PDF 水印，纯前端不上传)

**自建本地知识库 / 第二大脑**（喂合同/判决书做私有问答）：[infiniflow/ragflow](https://github.com/infiniflow/ragflow)`🛠️`(83566·✅·深度文档理解 RAG) · [Mintplex-Labs/anything-llm](https://github.com/Mintplex-Labs/anything-llm)(62055·✅·开箱即用本地知识库) · [nashsu/llm_wiki](https://github.com/nashsu/llm_wiki)(12750·⚠️·本地文档自动维护互链 Wiki，GPLv3) · [SamurAIGPT/llm-wiki-agent](https://github.com/SamurAIGPT/llm-wiki-agent)(3030·✅·Claude/Codex/Gemini 维护 Markdown Wiki 知识库) · [khoj-ai/khoj](https://github.com/khoj-ai/khoj)(35289·⚠️·自托管 AI second brain / 本地文档问答，AGPLv3)

**GraphRAG / 知识图谱 / Agent 记忆**：[microsoft/graphrag](https://github.com/microsoft/graphrag)(33979·✅·微软模块化 GraphRAG) · [HKUDS/LightRAG](https://github.com/HKUDS/LightRAG)(36941·✅·轻量知识图谱 RAG) · [getzep/graphiti](https://github.com/getzep/graphiti)(27847·✅·实时知识图谱记忆，面向 AI Agent) · [mem0ai/mem0](https://github.com/mem0ai/mem0)(59393·✅·AI Agent 通用长期记忆层) · [neo4j/neo4j-graphrag-python](https://github.com/neo4j/neo4j-graphrag-python)(1196·✅·Neo4j Python GraphRAG SDK)

## 5.2 提示词 · Skill 编写

`📚`：[f/prompts.chat](https://github.com/f/prompts.chat)(164293) · [dair-ai/Prompt-Engineering-Guide](https://github.com/dair-ai/Prompt-Engineering-Guide)(75957) · [ComposioHQ/awesome-claude-skills](https://github.com/ComposioHQ/awesome-claude-skills)(65803) · [PlexPt/awesome-chatgpt-prompts-zh](https://github.com/PlexPt/awesome-chatgpt-prompts-zh)(60769·中文) · [anthropics/prompt-eng-interactive-tutorial](https://github.com/anthropics/prompt-eng-interactive-tutorial)(36681·官方互动教程) · [anthropics/courses](https://github.com/anthropics/courses)(21990·官方课程) · [langgptai/wonderful-prompts](https://github.com/langgptai/wonderful-prompts)(6101·中文) · [anthropics/skills](https://github.com/anthropics/skills)(154854·官方 Agent Skills：docx/pdf/pptx/xlsx/skill-creator)

## 5.3 通用 Skill 合集

> 非法律专用，但能挑出合规/财务/办公的子集给律师用。

`🏛️`：[alirezarezvani/claude-skills](https://github.com/alirezarezvani/claude-skills)(18998·330+ skills 含 compliance/finance) · [jnMetaCode/agency-agents-zh](https://github.com/jnMetaCode/agency-agents-zh)(15544·211 中文专家角色) · [laolaoshiren/claude-code-skills-zh](https://github.com/laolaoshiren/claude-code-skills-zh)(450·中文 Claude skills 100+) · [MarvinLann/rightclick-creator](https://github.com/MarvinLann/rightclick-creator)(4·macOS Finder 右键神器) · [cyontheway/mac-clipboard-to-md](https://github.com/cyontheway/mac-clipboard-to-md)(0·剪贴板转 MD)

## 5.4 中文 LLM 入门 · AI 导航

`📚`：[datawhalechina/happy-llm](https://github.com/datawhalechina/happy-llm)(31539) · [datawhalechina/llm-cookbook](https://github.com/datawhalechina/llm-cookbook)(24305) · [AiHubCN/Awesome-Chinese-LLM](https://github.com/AiHubCN/Awesome-Chinese-LLM)(22638) · [liyupi/ai-guide](https://github.com/liyupi/ai-guide)(16301·鱼皮 AI 上手) · [ikaijua/Awesome-AITools](https://github.com/ikaijua/Awesome-AITools)(6040·AI 工具导航)

---

# 六、资源导航

## 6.1 Awesome 清单

> 想自己继续挖？从这些清单顺藤摸瓜。

`📚`：[pengxiao-song/awesome-chinese-legal-resources](https://github.com/pengxiao-song/awesome-chinese-legal-resources)(987·中文法律资源总集) · [international-explore/awesome-privacy-chinese](https://github.com/international-explore/awesome-privacy-chinese)(473·🔒隐私合规) · [lawve-ai/awesome-legal-skills](https://github.com/lawve-ai/awesome-legal-skills)(486·法律 Skill 索引) · [maastrichtlawtech/awesome-legal-nlp](https://github.com/maastrichtlawtech/awesome-legal-nlp)(330·国际法律 NLP) · [openlegaldata/awesome-legal-data](https://github.com/openlegaldata/awesome-legal-data)(258) · [Vaquill-AI/awesome-legaltech](https://github.com/Vaquill-AI/awesome-legaltech)(136) · [thunlp/LegalPapers](https://github.com/thunlp/LegalPapers)(498·清华 NLP·法律智能必读论文)

## 6.2 平台

- **法律元力 Yuanli Vault**（华宇元典）→ https://yuanli.ailaw.cn —— 法律 skill / 工具包聚合平台（应用商店式，2026-06-25 API 实测 65 个 skill / 13 个工具包）。其中**有公开 GitHub 源仓的已收进本仓各区**（元典官方套件、刘成/龚家勇/刘冲/杜思敏/积成等律师的 skill）；部分平台独占（无公开 GitHub），需去平台下载。
- **EttaLaw Skill 库**（艾塔法律AI实验室）→ https://ettalawailab.com/skills —— 法律 Skill 登录下载平台。2026-06-28 已用正常登录态下载并核验 5 个包；其中出海 DPA、经营者集中申报有 GitHub 源仓并已列入上文，平台独占/暂未公开 GitHub 源的实质包如下：

| 平台资源 | 类型 | 商用 | 核验状态 | 干嘛的 |
|---|---|:--:|---|---|
| [VIE协议生成](https://ettalawailab.com/skills/vie-assistant) | 🧩Skill | ❌ | ✅ 包内实测 | 💎杨思灿律师·VIE 协议套件生成：Excel/飞书信息表、5 份 DOCX 模板、字段校验、元典工商信息补全、一键生成 DOCX + ZIP；当前无 LICENSE，需按平台/作者授权使用 |
| [保证合同审查](https://ettalawailab.com/skills/guarantee-contract-review) | 🧩Skill | ❌ | ✅ 包内实测 | 💎保证合同审查 L3 Skill：20+ 风险点、强制性/任意性规定分层、谈判地位调整、跨境担保/融资保证场景与示例报告（CC BY-NC 4.0） |
| [中文合同审阅Skill](https://ettalawailab.com/skills/contract-review-cn) | 🧩Skill | ❌ | ✅ 包内实测 | 中文商事合同审阅 L2 Skill：结构化提问、P1/P2/P3 分级、法规标准有效性核查、合同类型 checklist 与 redline 指引（CC BY-NC 4.0，通用型低位参考） |

## 6.3 微信公众号长尾源

> 很多好 skill 只在公众号 / 微信群发，GitHub 搜不到。这些账号值得关注（部分已开源到 GitHub，链接见上文各区）：

| 公众号 / 社区 | 方向 | 代表产物 |
|---|---|---|
| 艾塔法律AI实验室 EttaLaw（Etta/Jingru Yang + 徐莲） | 🔒数据合规/出海/竞争法/投融资/担保 | 出海 DPA、经营者集中申报（已开源）；VIE 协议生成、保证合同审阅、中文合同审阅（见 [EttaLaw Skill 库](#62-平台)，登录下载） |
| 律见法度 | 尽调 | 同花顺快查 MCP（一句话企业尽调） |
| LLMQuant | 金融/投融资/证券 | 华尔街金融 Skills 库（[已开源](https://github.com/LLMQuant/skills)） |
| 律锥·legalskill（孙律师） | skill 社区 | legalskill org |
| 那一片数据星辰 | 数据合规/隐私 | 隐私协议生成器 |
| 有点智能事务所（于泽辉律师·北京星也） | AI 合规/数据合规 | 隐私协议 MVP 生成器（[已开源](https://github.com/youdianzhineng-ailaw/privacy-policy-self-service-generator-mvp)，预告 v2 深度版/v3 持续扩充） |
| 不允法典 | 民法 | 请求权基础 Skill |
| 智法AI · 策略律师 · 知识产权与竞争法 | 综合/竞争法 | （多在公众号，持续跟进） |

---

## 🤝 贡献 & 合规

- 想推荐新资源？收录标准与提交模板见 [CONTRIBUTING.md](CONTRIBUTING.md)。
- 更新历史见 [CHANGELOG.md](CHANGELOG.md)；每次收录变更都会记一条。
- 本仓只做链接索引、不复制任何项目代码或文章正文；收录不代表质量/合法性背书，商用前请自行核验各项目 license。详见 [COMPLIANCE.md](COMPLIANCE.md)。
- 数据随生态变化，可用 [`scripts/refresh-stars.sh`](scripts/refresh-stars.sh) 重新核验最新 `★ / license`。

---

## 📮 联系 & 交流

<div align="center">

**作者：赖宁** —— 做法律 AI、开源 skill，也在公众号分享法律人怎么用 AI 干活。

扫码加微信，一起交流法律 AI、共建这份清单 👇

<img src="assets/contact-qr.png" alt="加作者微信" width="170">

> 这份清单对你有用的话，欢迎点 ⭐ **Star** 支持，或转给身边的同行。
> 发现好资源 / 想收录你自己的项目 → 提 [Issue / PR](https://github.com/lilialla/awesome-legal-ai-zh/issues)，或直接加微信聊。

</div>

---

*快照 2026-06-24 · 238 个条目经 `gh api` 实测（404=0）。*
