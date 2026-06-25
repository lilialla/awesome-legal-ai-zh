# 更新日志 · Changelog

本项目所有重要变更都记录在此。格式参考 [Keep a Changelog](https://keepachangelog.com/zh-CN/)，倒序排列（最新在上）。
收录数 = `registry/seed-repos.txt` 中经 `gh api` 实测的真实仓数量。

---

## 2026-06-25

### 新增
- **潘睿律师 Legal Skills**（+1 仓 → **239**）：`pa1nrui1/legal-skills`（★19，MIT → 商用✅）——面向中国法律工作的 AI Agent Skills 集合，GitHub API 核验 59 个 `SKILL.md`，覆盖咨询、诉讼、刑辩、劳动争议、破产、合同、合规、法律检索与文书交付。→ §1.1
- **Lawyance 中文法律 AI 助手原型**（+1 仓 → **240**）：`Hill-1024/Lawyance`（★1，AGPL-3.0 → 商用⚠️）——FastAPI + React/Vite 的中文法律 AI 应用原型，集成法条/案例检索、企业信息、PDF/Word 处理、对话记忆、模拟法庭和前端工作区。低位收录，不作重点推荐。→ §1.1
- **法律元力（yuanli.ailaw.cn）全量复扫**（+5 仓 → **246**）：经公开 API 全量核验（65 skill / 13 工具包）与 GitHub API/仓库文件交叉核验，新增国内法律 AI / 法律 Skill / 律所工具：
  - `leo123-tto/legal-ai`（★0，MIT → 商用✅）：刘成律师·本地法律知识库增强包，legal-kb + 元典检索 + MinerU OCR + ZIP 导入导出 → §1.1。
  - `hisnontright/jiandawang-jicui-consultation`（★0，MIT → 商用✅）：检答网集萃第 1–140 批本地检索技能，面向检察业务/最高检答疑可溯源检索 → §2.1。
  - `yuhudie598-dev/legal-case-analysis-plus`（★0，无 license → 商用❌）：龚家勇律师·案件分析报告（法律关系分析法 Plus），依赖华宇元典 MCP 检索法规/案例/法答网 → §1.4。
  - `yuhudie598-dev/online-store-webpage-and-other-e-commerce-information-ai-proofreading-plus`（★0，无 license → 商用❌）：电商信息 AI 校对 Plus，辅助法务/合规核对网店页面与权威资料差异 → §1.7。
  - `yuhudie598-dev/workbuddy-calendar`（★1，无 license → 商用❌）：WorkBuddy 侧边栏日历，适合法律日程/开庭/截止日期管理 → §3.1。
  - 扫到但暂缓：`cyontheway/pdf-watermark-tool`（MIT）是离线 PDF 水印工具，法律场景可用但非法律 AI / Skill 主线，本次不进主清单。

### 修正
- **全量 GitHub 元数据回扫**：用 GitHub GraphQL/API 复核 registry 全部仓库，批量更新 README 所有表格与行内 star；同步修正 `gcheng001/legal-skills`、`f/prompts.chat`、`Open-Source-Legal/OpenContracts` 等重定向后的规范仓名。
- **控制面补齐**：`kevchentw/awesome-chinese-fonts` 已在 README 字体区展示但漏入 registry，本次补入 `ppt-assets`，收录数同步为 **241**。
- **商用标记校正**：按 GitHub license 识别，将 `legalskill/legalskill`（Apache-2.0）、`hellodigua/code996`（MIT）、`THUIR/LeCaRDv2`（MIT）从 ❌ 修正为 ✅。
- §3.1 `lawflow-boop/LawLink` 已确认早已收录；按 GitHub API 更新 star 3 → 39，并将描述改为“开源自部署中小律所案件与执业管理系统”，避免误写成 AI 项目。
- 维护口径更新：近期增量扫描优先盯国内法律 AI / 法律 Skill / 律所工具；国外纯法域项目暂不推进，除非与中国律师涉外业务直接相关。

## 2026-06-24

### 新增
- **游初 · 鉴定式刑法案例研习 Skill**（+1 仓 → **238**）：`Youchu-lawhub/gutachten-criminal-case`（★10，Apache 文本但 GitHub 识别为 NOASSERTION → 商用✅/需保留署名）——三阶层犯罪论 + 鉴定式写作，覆盖案情解析、罪名发现、双闸确认、并行写作、三维核验、法条校验与 Word 输出。→ §1.4
- **股权转让审核 Skill**（+1 仓 → **237**）：`lilialla/equity-transfer-review-skill`（★0，MIT → 商用✅）——维护者出品，基于公开小红书线索抽象重写为独立 Skill：股权转让协议审查、交易尽调红旗、资料缺口、条款修改建议、交割条件和证据引用规则。原始小红书图片仅作离线分析，不入库。→ §1.6

### 完善
- **股权转让审核 Skill**：多 agent 复核后补强交易类型分流、无材料 intake、出资责任、税务/外汇、国资/上市/外资/监管行业闸门、硬阻断事项和 evidence-grade 标签口径；主清单描述同步更新。→ §1.6

## 2026-06-22

### 新增
- **法穿 AI Copilot**（+1 仓 → **233**）：`Lawyer-ray/FachuanHybridSystem`（★191，Elastic License 2.0 → 商用⚠️：自用可商用，禁转售为托管服务）——一线执业律师自研的律所一体化系统，由司法局比赛作品演化而来。核心：法院短信自动解析/下载/归档（6 种送达平台，飞书/Telegram/企微通知）+ 一次生成全套委托材料（合同/授权委托书/法代身份证明，结构化模型按规则生成，无需人工再改）+ OA 立案与一张网立案统一入口 + 本地知识库。Django 6 + React 19 + MCP，127 模型 / 483 API / 35 模块。→ §3.1
  - 线索来源：抓取「不折腾的刘律」案件看板开源公告（`mp.weixin.qq.com/s/GeY_ZS-uuwnqeMP3Yp5Ldw`），文末致敬法穿项目顺藤收录。
- **多平台扫描收割**（+3 仓 → **236**）：扫 GitHub 近期更新 + 公众号/小红书/知乎/V2EX 线索，去重核验后新增——
  - `zeweihan/aiworkdeck`（★54，AGPL-3.0 → 商用⚠️）：AI 原生「律师版 VS Code」工作台，案件/文件树 + Agent + 插件 + WPS 在线编辑 + OCR + 证据链，可私有化 → §1.1。
  - `sunyifeisb-art/legalwork`（★6，无 license → 商用❌）：LegalWork 本地优先法律 AI 工作台，70+ 技能 + OCR + 脱敏 + 案件管理（bytelegal.cn）→ §1.1。
  - `abaiar/-LexAI`（★19，无 license → 商用❌）：小理智法 AI 法律咨询平台，LangChain Agent + 得理法律数据库检索 → §1.1。
- **扫到但暂未收录**（待维护者定夺）：`qingyun1022/smart_contract_reviewer`（★80 但停更 >1 年、无 license）、`Materialism-1/Contract-Review-Judgment-Summary-prompt`（★45 提示词集，2024 停更）、知乎 ContractGuard（仓库地址待查）、以及一批 GitHub 0–2★ 新 demo（学生/课程项目为主）。小红书对搜索引擎封闭、公众号正文 GitHub 链接不被索引，两渠道 WebSearch 基本挖不动。

### 修正
- §3.1 `leo123-tto/case-board` star 4 → 13，描述补「已正式公开源码 v0.3.9，可丢给 AI 自行编译 Windows 版」（同篇公告确认正式开源）。
- 公告另提及「鲸鱼兄弟 CodeWhale」（`Hmbown/CodeWhale`，通用 Agent harness ★38k）——属通用开发工具，非法律垂直项目，按收录口径不录。

## 2026-06-14

### 新增
- **CorpClaim CN**（+1 仓 → **232**）：`yxk-lawyer/litigation-prep-skill-cn`（★3，无 license → 商用❌）——执业律师做的公司民商事诉讼指导 skill，请求权基础理论 + 民事案由规定，输出「案由→请求权基础→构成要件→证据清单→诉讼策略」→ §1.4。
- **公众号线索深挖**（+1 仓 → **231**）：追查艾塔「保证合同审阅 Skill」公众号文章时，确认该 skill 未上 GitHub（仅微信群发放），但顺藤挖到 `skala-io/legal-skills`（★37，Apache-2.0）——Skala（skala.io）律师团队的英文创业法 11 skill：SAFE/SAFT/term sheet 审查、Reg S 离岸发行、startup 尽调、董事会决议、网红/承包商协议、辖区选择、开源 license → §1.6。填「涉外/美国创业融资法」空白。
- 旁证：艾塔真身 = Jingru Yang（`ettajingruyang`），`LianXU-321`（徐莲）为合作者；技术合作者 `xhqing`（许华清）。保证合同 / VIE skill 走微信群独家，GitHub 无源仓。

### 修正
- 署名校正（gh commit 作者实测）：§1.3 经营者集中申报归 Etta/Jingru Yang（非"艾塔/徐莲律师"统称）；§1.7 出海 DPA 归徐莲（LianXU）；§6.3 艾塔实验室行改为「Etta/Jingru Yang + 徐莲」，代表产物补保证合同审阅并标明微信群独家。

## 2026-06-11

### 新增
- **法律元力（yuanli.ailaw.cn）增量回扫**（+2 仓 → **229**）：经站点 sitemap + 公开 API 全量比对（59 skill / 13 工具包），绝大部分源仓 06-08 已收录，本次新增：
  - `leo123-tto/case-board`（律师个人案件可视化看板，macOS·Tauri；PolyForm 非商业 → 商用❌）→ §3.1
  - `Youchu-lawhub/gutachten-civil-case`（民法典请求权基础·德国鉴定式案例研习报告，游初；无 license → 商用❌）→ §1.4
- 元力站上另有 10 个**平台独占** skill（潘淑燕 4 个、华宇元典 2 个、龚家勇 2 个、李伯阳、闫逸寒）无 GitHub 源仓，按「只索引 GitHub 可核验仓」口径不收录。
- **公众号线索回扫**（+1 仓 → **230**）：`SKYLENAGE-AI/PLawBench`（Qwen×阿里 AIData×晓天衡宇·法律实务评测基准，13 场景 850 题 12500 条 rubric；无 license → 商用❌）→ §2.3。

### 修正
- §1.7 隐私协议 MVP 生成器补作者署名（于泽辉律师·有点智能事务所）与 v2/v3 预告；§6.3 公众号长尾源新增「有点智能事务所」。

## 2026-06-08

### 新增
- **平台/社区/作者全扫**（+23 仓 → **227**）：
  - 法律大模型补全：`AndrewZhe/lawyer-llama`、`siat-nlp/HanFei`（韩非）、`davidpig/lychee_law`（律知）、`thunlp/LegalPLMs`（Lawformer）
  - 数据/检索：`THUIR/LeCaRDv2`、`liuhuanyong/CrimeKgAssitant`、`billvsme/law_ai`
  - 社区套件：`choosemoon/legal-skills`（832 篇法学论文蒸馏）、`gcheng001/legal-skills`（27 skill·含刑辩）、`MAXXXXXLI/workbuddy-cn-legal-skills`
  - 实务 skill：`evolsb/legal-redline-tools`（合同红线交付）、`CSlawyer1985/case-type-guide`（类案要件）、`xtgmf/minfadian`（民法典）、`wangchangwei/arb-skill`（劳动仲裁）、`imchongliu/lpm-skills-zh`（法律项目管理）、cat-xierluo 4 个单点 skill
  - 工具：`handsomestWei/red-seal-ocr`（印章识别）、`cyontheway/word-replacer`（文书脱敏替换）
- **法律元力（yuanli.ailaw.cn）API 收割**（+14 仓 → 204）：经 Playwright 拦截平台 API 提取全部 58 skill 的 GitHub 源仓，去重后新增 `yuandian-ailaw/Agent-for-legal-cn`（元典官方）、`anthropics/skills`、`malnlda/legal-due-diligence`（尽调）、`SimbaCD/legal-period-manager-skills`（执行/期限管家）、`imchongliu/law-firm-worklog`（律所工时）、`imchongliu/foreign-law-research`（涉外）、隐私协议生成器等。

### 修正
- **对抗式多 agent 评审**后批量修正：8 处「能否商用」标注与真实 license 不符（如 `LLMQuant/skills` MIT 误标 ⚠️→✅、多个无 license 项 ⚠️→❌）；`refresh-stars.sh` 增加 NOASSERTION→⚠️ 判定。
- 目录 §2.2 中文锚点失效已修；`CNIPA/PatentDatabases` 描述纠错（非国知局官方）；去除 `knowledge-work-plugins`/`ENScan_GO` 重复展示。

## 2026-06-07

### 新增（首发 → ~190 仓）
- 创建公开仓 **awesome-legal-ai-zh**（CC0，本清单自身）。
- **两级目录**（6 大类 / 26 子类），每条标 `类型 · ★ · 能否商用 · 用途`，全部 `gh api` 实测。
- 覆盖：法律 Skill 套件、合同/文书/IP、诉讼/刑事、涉外、公司投融资尽调、数据合规脱敏、劳动家事、税务、检索/案例/MCP（含**企查查/北大法宝/天眼查** MCP）、法律大模型、数据集评测（含 **Harvey BigLaw Bench**、`open-compass/LawBench`）、律所运营、自媒体 IP（卡兹克/op7418）、PPT/配图/设计（含 `nexu-io/open-design`）、技术基础（RAG/文档解析 MinerU）。
- 收录**维护者自有** skill：`lilialla/legal-document-format-skill`、`lilialla/request-right-skill-reference`（🧑‍⚖️维护者出品）。
- 收录艾塔出海 DPA、元典检索、清华系/中文法律大模型等。

### 质量
- **可用性审计**：全量 `gh api` 实测，404 = 0；清理 8 个停更且依赖现行法律的死项目（过时法条/税率计算器等）。
- 视觉：极简白色天平 logo（深浅自适应）+ 徽章。
- 配套：`CONTRIBUTING.md`（收录标准）、`COMPLIANCE.md`（索引非搬运 + license 红线）、`scripts/refresh-stars.sh`（一键刷新 star/license）。
- 引流：底部「联系 & 交流」区（作者微信）。

---

> 维护约定：**每次新增/删除/修正条目，都在本文件顶部对应日期下补一条**。
