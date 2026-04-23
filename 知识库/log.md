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

## [2026-04-23] integrate | 接入 MarkItDown 转换层
- Operation: 集成 [microsoft/markitdown](https://github.com/microsoft/markitdown) 作为 ingest 流水线的预处理器
- Pages created: [[MarkItDown]], [[Ingest 流水线]]
- Pages updated: [[index]], [[hot]], [[CLAUDE]]（工作流扩展）
- Files added:
  - `.claude/scripts/md转换.py` — 按扩展名自动分流的批量转换脚本
  - `.claude/commands/ingest.md` — `/ingest` slash 命令封装
  - `源文档/原始/` — 原件投递目录
- Install: `pip install 'markitdown[all]'` on Python 3.12 and 3.14（version 0.1.5）
- Key insight: **原件永远不进 wiki**，wiki 只消费转换后的 markdown。markitdown 把文档统一成 LLM 友好的 md，让 wiki 构建与源格式解耦。

---

## [2026-04-23] rename | vault 文件夹全面中文化
- Operation: 把所有英文文件夹名改为中文（`.raw` → `源文档`、`wiki` → `知识库` 等 14 个文件夹）
- Pages updated: [[CLAUDE]], [[WIKI]], [[Wiki Map.canvas]], [[元数据/dashboard]]（Dataview 查询路径）, [[overview]], [[getting-started]], [[index]], [[hot]], [[log]]
- Config updated: `.obsidian/app.json`（attachmentFolderPath）、`.obsidian/graph.json`、`.obsidian/snippets/vault-colors.css`
- Key insight: 保留所有 `.md` 文件名不动，让形如 `[[index]]` 的短 wikilink 无需改动；只更新**带路径的** wikilinks（`[[概念/_index]]` 等）。

---

## [2026-04-23] scaffold | Knowledge Base Initialization
- Operation: Full vault scaffold based on claude-obsidian architecture
- Mode: E (Research)
- Pages created: [[index]], [[overview]], [[log]], [[hot]], [[getting-started]], [[概念/_index]], [[实体/_index]], [[来源/_index]]
- Templates created: comparison, concept, entity, question, source
- Config: graph color groups, vault-colors.css, appearance snippets
- Key insight: AI learning knowledge base initialized, ready for first ingest.
