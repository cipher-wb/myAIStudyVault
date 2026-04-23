---
type: meta
title: "Wiki Log"
updated: 2026-04-23
tags:
  - meta
  - log
status: evergreen
---

# Wiki Log

Append-only operation log. Newest entries at the top.

---

## [2026-04-23] rename | 源文档 → .源文档（恢复隐藏前缀）
- Operation: 把 `源文档/` 改回 `.源文档/`，使其在 Obsidian 文件树中不可见
- Reason: 用户偏好干净的文件树视图，不希望源文档目录出现在主界面
- Trade-off: Web Clipper 等 `obsidian://` URI 外部工具将无法写入 `.源文档/`（Obsidian 安全策略），需通过文件管理器拖入或命令行 ingest
- Files updated: 8 个文件的路径引用（CLAUDE.md / WIKI.md / overview.md / getting-started.md / hot.md / ingest.md / md转换.py / vault-colors.css）
- Folder renamed: `源文档/` → `.源文档/`（含 6 个子目录不变）

---

## [2026-04-23] reset | 清空测试内容，回到纯净基础设施状态
- Operation: 删除所有测试 ingest 的来源/实体/概念页面 + 清空 `源文档/文章/` 下的剪藏样本
- Deleted (源文档/文章/): Claude Managed Agents 概览 / 开始使用 Claude Managed Agents / 定义你的代理 / 工具 / 在 Console 中进行原型设计 / What is the Model Context Protocol (MCP)
- Deleted (知识库/实体): Anthropic / Claude / Claude Managed Agents / MarkItDown / ant CLI / anthropic Python SDK
- Deleted (知识库/概念): Ingest 流水线 / Managed Agents 架构
- Deleted (知识库/来源): 开始使用 Claude Managed Agents
- Reset: `知识库/index.md`（entries 清空）、`知识库/hot.md`（回到等待首次 ingest 状态）
- Infra kept: 文件夹结构、`.claude/scripts/md转换.py`、`.claude/commands/ingest.md`、`_模板/`、所有 `_index.md` 占位、CLAUDE.md/WIKI.md 文档
- Key insight: 之前的内容只是测试流水线，不代表知识库方向；从 0 开始积累。

---

## [2026-04-23] rename | 去掉源文档的点前缀（`.源文档` → `源文档`）
- Operation: 解除 Obsidian 对 `.` 前缀路径的外部写入限制
- Reason: Obsidian 禁止通过 `obsidian://` URI 写入 `.` 开头文件夹，导致 Web Clipper 等外部工具无法落地文件
- Files updated: 11 个文件路径引用 + `.obsidian/snippets/vault-colors.css`
- Folder renamed: `.源文档/` → `源文档/`（含 6 个子目录：原始/文章/文字稿/截图/数据/素材）
- Side effect: 文件夹现在在 Obsidian 文件树中可见

---

## [2026-04-23] integrate | 接入 MarkItDown 转换层
- Operation: 集成 [microsoft/markitdown](https://github.com/microsoft/markitdown) 作为 ingest 流水线的预处理器
- Install: `pip install 'markitdown[all]'` on Python 3.12 and 3.14（version 0.1.5）
- Files added:
  - `.claude/scripts/md转换.py` — 按扩展名自动分流的批量转换脚本
  - `.claude/commands/ingest.md` — `/ingest` slash 命令封装
  - `源文档/原始/` — 原件投递目录
- Key insight: **原件永远不进 wiki**，wiki 只消费转换后的 markdown。

---

## [2026-04-23] rename | vault 文件夹全面中文化
- Operation: 把所有英文文件夹名改为中文（`raw` → `源文档`、`wiki` → `知识库` 等 14 个文件夹）
- Config updated: `.obsidian/app.json`（attachmentFolderPath）、`.obsidian/snippets/vault-colors.css`
- Key insight: 保留所有 `.md` 文件名不动，让形如 `[[index]]` 的短 wikilink 无需改动。

---

## [2026-04-23] scaffold | Knowledge Base Initialization
- Operation: Full vault scaffold based on claude-obsidian architecture
- Mode: E (Research)
- Pages created: [[index]], [[overview]], [[log]], [[hot]], [[getting-started]], [[概念/_index]], [[实体/_index]], [[来源/_index]]
- Templates created: comparison, concept, entity, question, source
- Config: graph color groups, vault-colors.css, appearance snippets
- Key insight: AI learning knowledge base initialized, ready for first ingest.
