# 合规声明 · License Notice

## 核心原则：索引指向，不搬运

Scale **只收录指向第三方资源的链接 + 元数据 + 一句话点评**，**不复制**任何被收录项目的源代码、README 全文，也**不存储**任何微信公众号文章正文。被收录项目的著作权归原作者所有。

## 为什么必须这样

本仓库收录的多个头部项目带有限制性许可，**整体搬运/改写会侵权**：

| 项目 | License | 限制 |
|---|---|---|
| `THUYRan/Legal-Skills-Chinese` | CC BY-NC-ND 4.0 | **非商用 + 禁改编 + 必须署名** → 只能链接 |
| `cat-xierluo/legal-skills`、`ai-legal-claude`、`contract-review-pro` 等 | 无 License | 默认保留所有权利 → 只能链接 |
| `ChatLaw`、`LaWGPT`、`SuitAgent`、`worldwidelaw/legal-sources`、`j-lawyer` | (A)GPL | 强 copyleft → 链接无碍；**不可 fork 进闭源/商用产物** |
| 微信公众号文章 | 著作权法 | 正文受保护 → 只存链接 + 摘要 + 标签 |

## 「能否商用」标注规则

- ✅ **可商用**：MIT / Apache-2.0 / BSD / MPL / CC0
- ⚠️ **谨慎**：GPL / AGPL（传染性，链接/独立使用可，混入产物需开源）
- ❌ **不可商用 / 仅链接**：CC BY-NC-* / 无 license / NOASSERTION

## 抓取素材处理

仓库构建过程中用 Playwright 抓取的公众号原文仅作**离线分析提取链接之用**，存于 `_wechat_raw/`（已 `.gitignore`，**不入库、不公开**）。最终公开物只有链接与摘要。

## 免责

收录不构成对项目质量、安全性、合法性的背书。使用前请自行核验最新 license 与合规边界。本索引内容随生态变化，不保证时效。
