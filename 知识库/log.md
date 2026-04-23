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

## [2026-04-23] ingest | 开始使用 Claude Managed Agents（首次实战 ingest）
- Operation: Ingest Anthropic 官方 quickstart 文档
- Source: [[开始使用 Claude Managed Agents]]（Web Clipper 剪藏到 `源文档/文章/`）
- URL: https://platform.claude.com/docs/zh-CN/managed-agents/quickstart
- Pages created (7):
  - 来源：[[开始使用 Claude Managed Agents]]
  - 实体：[[Claude Managed Agents]], [[Anthropic]], [[Claude]], [[ant CLI]], [[anthropic Python SDK]]
  - 概念：[[Managed Agents 架构]]
- Pages updated: [[index]], [[hot]]
- Key insights:
  - Managed Agents 是 Anthropic 推出的**托管 agent 运行时**，对标 OpenAI Assistants + Code Interpreter，以 [[Claude]] 为大脑
  - 架构本质上是**四件套**：Agent（配置模板） × Environment（容器模板） → Session（运行实例），通过 Events 双向流通信
  - 当前处于 beta，请求头 `managed-agents-2026-04-01`
  - `agent_toolset_20260401` 是一键启用预置工具集的语法糖
- Pipeline milestone: **流水线完整跑通**（Web Clipper → 源文档/文章/ → Claude 提炼为 wiki 页面），Ingest 流水线从"设计"升级为"实战验证"。

---

## [2026-04-23] rename | 去掉源文档的点前缀（`.源文档` → `源文档`）
- Operation: 解除 Obsidian 对 `.` 前缀路径的外部写入限制
- Reason: Obsidian 禁止通过 `obsidian://` URI 写入 `.` 开头文件夹，导致 Web Clipper 等外部工具无法落地文件
- Files updated: 11 个 —— CLAUDE.md / WIKI.md / 4 个 知识库/*.md / 2 个 知识库/{实体,概念}/ 页 / 2 个 .claude/ 配置 / 1 个 .obsidian/snippets/vault-colors.css
- Folder renamed: `.源文档/` → `源文档/`（含 6 个子目录：原始/文章/文字稿/截图/数据/素材）
- Side effect: 文件夹现在在 Obsidian 文件树中可见（这反而方便手动查看剪藏落地结果）
- Key insight: dot-prefix 目录有"永不让用户触碰"的语义，但我们需要往里写东西，二者冲突 → 舍弃隐藏性。

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
