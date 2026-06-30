# 更新日志 · Changelog

本项目所有重要变更都记录在此。格式参考 [Keep a Changelog](https://keepachangelog.com/zh-CN/)，倒序排列（最新在上）。
收录数 = `registry/seed-repos.txt` 中经 `gh api` 实测的真实仓数量。

---

## 2026-06-30

### 新增
- **中国法规本地检索 CLI / MCP 补录**（+1 仓 → **269**）：`nh59yytyd5-dev/chinalaw-cli`（★1，Apache-2.0 → 商用✅）——面向 AI Agent 的中国法律法规本地检索基础设施，提供 `chinalaw` CLI、`chinalaw-mcp`、7 个 Agent Skill、来源元数据、条文级引用与官方源按需补全。实质核验：隔离安装 `scripts/install-local` 通过；`scripts/install-skills --copy` 可安装到 `.claude/.agents/opencode`；`scripts/check-public-fixtures` 通过；`python -m unittest discover -s tests -v` 通过（678 tests OK, skipped=33）；`verify-source flk_npc` 返回 `ok=true`；实测从国家法律法规数据库补全旧《合同法》第 52 条并落库。定位为“本地检索基础设施”，不是全量法律数据库；实测初始库为 49 部法规 / 7516 条条文 / 74 个版本修订，时间效力规则需另行 `sync --applicability`。→ §2.1

## 2026-06-28

### 新增
- **劳动权益 Skill 补录**（+1 仓 → **268**）：`jerry046918/labor_rights_skills`（★1，Anti-996/NOASSERTION → 商用⚠️）——大陆劳动权益法律顾问 Skill，覆盖违法解除、欠薪、未签合同、加班费、工伤等争议，含证据采集、法律意见书模板、本地录音转写脚本与测试结构；轻量技术核验 `py_compile scripts/*.py` 通过，完整 pytest 因本机缺 `pytest` 未运行。→ §1.8
- **EttaLaw 平台下载 Skill 补录**（不计入 GitHub 仓库数，仍为 **268 仓**）：用本机 Tabbit 正常登录态从 `ettalawailab.com/skills` 下载并解包核验 5 个 Skill 包；不保存账号、Cookie、Token 或包内正文到本仓。新增平台资源表 → §6.2：
  - [VIE协议生成](https://ettalawailab.com/skills/vie-assistant)（无 LICENSE → 商用❌）：杨思灿律师 VIE 协议套件生成 Skill，含 Excel/飞书信息表、5 份 DOCX 模板、字段校验、元典工商信息补全脚本和一键 DOCX + ZIP 生成器；`py_compile scripts/*.py` 通过，脱敏测试数据实测生成 4 份 DOCX + ZIP，未发现残留 `【...】` 占位符。
  - [保证合同审查](https://ettalawailab.com/skills/guarantee-contract-review)（CC BY-NC 4.0 → 商用❌）：L3 保证合同审查 Skill，541 行 `SKILL.md`，覆盖 20+ 风险点、强制性/任意性规定分层、谈判地位调整、跨境担保/融资保证场景与示例报告。
  - [中文合同审阅Skill](https://ettalawailab.com/skills/contract-review-cn)（CC BY-NC 4.0 → 商用❌）：L2 中文商事合同审阅 Skill，575 行 `SKILL.md`，覆盖结构化提问、P1/P2/P3 分级、法规标准有效性核查、合同类型 checklist 与 redline 指引；因较通用，作为低位参考。

### 暂缓 / 排除
- **`atongmuliuhong` 仓库清单实质审查**：公开仓多为 fork/镜像，`MinerU`、`FachuanHybridSystem`、`SuitAgent`、`opc-legal-counsel.skill`、`LaWGPT`、`awesome-legal-ai-zh`、`claude-howto` 均不重复收录；疑似原创仓 `case-archive`、`law-case-automation` 有一定实务价值但无独立 license 文件/非商用或律所定制明显，`case-type-guide` 与已收录 `CSlawyer1985/case-type-guide` 高度重合，`AI-Powered-LegalComplianceAssistant` 更像作品集式工程 Demo，暂不新增。

### 修正
- **许可口径校正**：`LianXU-321/china-outbound-service-dpa-bilingual` 包内 `LICENSE.txt` 为 Apache-2.0，但 `SKILL.md` / `agents/openai.yaml` metadata 标注 `CC-BY-NC-4.0`，先将 README 商用列从 ✅ 改为 ⚠️，待作者/仓库许可口径澄清。
- **重复项处理**：EttaLaw 下载包中的 `merger control assessment` 已确认对应 `ettajingruyang/PRC-merger-control-assessment`（包内 `.git/config` origin 指向该仓），不重复新增；出海 DPA 也不重复新增。

## 2026-06-27

### 新增
- **法律 AI / Skill 增量扫描 · 实质审查后收录**（+6 仓 → **267**）：先经 GitHub API、仓库文件、README 可运行性、license 与同类项目对比核验，再低位或正式收录：
  - `yuandian-ailaw/yuandian-mcp-server`（★3，MIT → 商用✅）：**元典官方 MCP Server**，动态注册元典开放平台法规/案例/企业等 API；需用户自备 `YUANDIAN_API_KEY`，使用仍受元典平台条款约束 → §2.1。
  - `katejianglaw/refine-legal-chinese`（★5，MIT → 商用✅）：**法言法语**法律中文改写/审校 Skill，真实 `SKILL.md` + 参考文件，聚焦语言表达层，不替代法律判断 → §1.2。
  - `Xigua9xi/ai-legal-review-skillkit`（★2，MIT → 商用✅）：中文合同审查 workflow 模板基座，含 `SKILL.md`、公开规则、profiles、schema、fixtures 与 tests；低位收录为可 fork 基座，不标成律师实战审查成品 → §1.2。
  - `worker-aid-ai/worker-aid-agent`（★1，AGPL-3.0-or-later → 商用⚠️）：劳动者权益自助 Agent/Skill，本地 Web + CLI + 多个劳动争议子 skill，覆盖欠薪、未签合同、违法解除、加班费、证据整理与仲裁申请草稿 → §1.8。
  - `moyupeng0422/legal-doc-redactor`（★94，MIT → 商用✅）：彭雨诗律师·离线法律文档脱敏/还原工具，支持 docx 批量一致替换、白黑名单、自定义类型、脱敏后外部审阅痕迹还原 → §1.7。
  - `THUIR/LegalOne-R1`（★11，Apache-2.0 → 商用✅）：LegalOne-R1 法律推理模型系列发布页，提供 1.7B/4B/8B Hugging Face 权重链接；仓库本体以 README/图表为主，低位收录 → §2.4。

### 暂缓 / 排除
- 经子镜头抽样审查，暂缓 `FAYANHUIYING/claude-for-legal-HoriZon`：插件骨架真实，但多处核心法条库/经验资产仍为 placeholder，先不与成熟中国法套件并列。
- 暂缓 `moyupeng0422/legal-tools`：人民法院案例库 MCP 与国家法律法规数据库 MCP 均有真实入口，但顶层为 CC-BY-NC，README 明示非商用，且案例库部分要求用户自行提取登录 token；待拆分收录或补充合规说明。
- 暂缓 `GaaZeon-Hui/legal-text-splitter-mcp`：有包结构和测试，但 README 默认 `uvx` 安装路径与实际发布状态不一致，且更偏法律文本预处理而非检索。
- 暂缓 `ZongziForu/npc-law-db`：国家法律法规数据库 Skill 技术上成立且测试可跑，但无 license 且 README 明示学习研究用途，不进入本轮收录。
- 排除 `wesky820/china-law-case-analysis-skills`：虽有大量 `SKILL.md`，但抽样发现主题错配和批量生成污染，且无 license。
- 排除 `YONHKAN11/witness-cross-examination-skills`：CC0 但无真实 Skill/应用入口，更像个人文章页；暂缓 `winterliu6/law-audit-skill`，因 README 启动说明不完整且根目录无 license 文件。

## 2026-06-25

### 新增
- **潘睿律师 Legal Skills**（+1 仓 → **239**）：`pa1nrui1/legal-skills`（★19，MIT → 商用✅）——面向中国法律工作的 AI Agent Skills 集合，GitHub API 核验 59 个 `SKILL.md`，覆盖咨询、诉讼、刑辩、劳动争议、破产、合同、合规、法律检索与文书交付。→ §1.1
- **Lawyance 中文法律 AI 助手原型**（+1 仓 → **240**）：`Hill-1024/Lawyance`（★1，AGPL-3.0 → 商用⚠️）——FastAPI + React/Vite 的中文法律 AI 应用原型，集成法条/案例检索、企业信息、PDF/Word 处理、对话记忆、模拟法庭和前端工作区。低位收录，不作重点推荐。→ §1.1
- **法律元力（yuanli.ailaw.cn）全量复扫**（+6 仓 → **247**）：经公开 API 全量核验（65 skill / 13 工具包）与 GitHub API/仓库文件交叉核验，新增国内法律 AI / 法律 Skill / 律所工具：
  - `leo123-tto/legal-ai`（★0，MIT → 商用✅）：刘成律师·本地法律知识库增强包，legal-kb + 元典检索 + MinerU OCR + ZIP 导入导出 → §1.1。
  - `hisnontright/jiandawang-jicui-consultation`（★0，MIT → 商用✅）：检答网集萃第 1–140 批本地检索技能，面向检察业务/最高检答疑可溯源检索 → §2.1。
  - `yuhudie598-dev/legal-case-analysis-plus`（★0，无 license → 商用❌）：龚家勇律师·案件分析报告（法律关系分析法 Plus），依赖华宇元典 MCP 检索法规/案例/法答网 → §1.4。
  - `yuhudie598-dev/online-store-webpage-and-other-e-commerce-information-ai-proofreading-plus`（★0，无 license → 商用❌）：电商信息 AI 校对 Plus，辅助法务/合规核对网店页面与权威资料差异 → §1.7。
  - `yuhudie598-dev/workbuddy-calendar`（★1，无 license → 商用❌）：WorkBuddy 侧边栏日历，适合法律日程/开庭/截止日期管理 → §3.1。
  - `cyontheway/pdf-watermark-tool`（★0，MIT → 商用✅）：离线 PDF 水印工具，纯前端本地处理、不上传文件；作为法律文档处理辅助工具低位收录 → §5.1。
- **OCR / 文档解析底座补录**（+3 仓 → **250**）：按律师案卷、扫描件、批量 PDF 处理场景补入通用 OCR 基础设施：
  - `PaddlePaddle/PaddleOCR`（★83734，Apache-2.0 → 商用✅）：百度飞桨 OCR 主项目，PP-OCR/PP-Structure/文档解析/表格与版面识别，覆盖 100+ 语言 → §5.1。
  - `baidu/Unlimited-OCR`（★6667，MIT → 商用✅）：百度最新开源长文档 one-shot OCR，面向 40+ 页连续解析，模型/代码/Hugging Face 同步公开 → §5.1。
  - `deepseek-ai/DeepSeek-OCR`（★23379，MIT → 商用✅）：视觉文本压缩 OCR，作为长文档解析与小模型 OCR 方案的技术底座 → §5.1。
- **本地知识库 / GraphRAG / Agent 记忆补录**（+11 仓 → **261**）：按截图线索与 GitHub 搜索补入通用知识库底座，作为法律案卷、合同库、判例资料库的技术选型参考：
  - 截图线索：`Zleap-AI/SAG`（★1606，MIT → 商用✅）、`VectifyAI/PageIndex`（★33391，MIT → 商用✅）、`nashsu/llm_wiki`（★12750，GPL-3.0 → 商用⚠️）。
  - 本地/第二大脑：`SamurAIGPT/llm-wiki-agent`（★3030，MIT → 商用✅）、`khoj-ai/khoj`（★35289，AGPL-3.0 → 商用⚠️）。
  - GraphRAG/记忆：`microsoft/graphrag`（★33979，MIT → 商用✅）、`HKUDS/LightRAG`（★36941，MIT → 商用✅）、`getzep/graphiti`（★27847，Apache-2.0 → 商用✅）、`mem0ai/mem0`（★59393，Apache-2.0 → 商用✅）、`neo4j/neo4j-graphrag-python`（★1196，Apache/Python license → 商用✅）。
  - 生产级检索：`SciPhi-AI/R2R`（★7894，MIT → 商用✅）。

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
