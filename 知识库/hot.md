---
type: meta
title: "Hot Cache"
updated: 2026-04-23
tags:
  - meta
  - hot-cache
status: evergreen
---

# Recent Context

## Last Updated
2026-04-23 — 完成首次 ingest：Anthropic [[Claude Managed Agents]] quickstart（Web Clipper → 源文档/文章 → 7 个 wiki 页面）

## Key Recent Facts
- 基于 Andrej Karpathy 的 LLM Wiki 模式构建 AI 学习知识库，使用 Mode E (Research)
- **[[Claude Managed Agents]]**：Anthropic 推出的托管智能体服务（beta），对标 OpenAI Assistants + Code Interpreter
- **[[Managed Agents 架构]]**：Agent（配置） + Environment（容器） + Session（实例） + Events（双向流）四件套
- 调用 Managed Agents 必须带 `managed-agents-2026-04-01` beta 请求头（SDK 自动处理）
- `agent_toolset_20260401` 工具集一键启用 bash/文件/网络搜索等预置工具
- 源文档 → wiki 的摄取流水线已实战跑通：Web Clipper → `源文档/文章/` → `/ingest` → `知识库/来源/ + 实体/ + 概念/`
- **关键限制**：Obsidian 禁止通过 `obsidian://` URI 写入 `.` 开头文件夹，所以存源文档的目录必须是 `源文档/` 而非 `.源文档/`

## Recent Changes
- Ingested: [[开始使用 Claude Managed Agents]]
- Created (entities): [[Claude Managed Agents]], [[Anthropic]], [[Claude]], [[ant CLI]], [[anthropic Python SDK]]
- Created (concepts): [[Managed Agents 架构]]
- Updated: [[index]]（首次填入实际 entries）

## Active Threads
- 可深入：Managed Agents 的工具列表详解、events 完整事件类型、环境网络配置 —— 需 ingest 更多文档
- Gap：[[Claude]] 模型家族完整版本矩阵未覆盖（目前只知道 `claude-opus-4-7`）
- 可选增强：配置 ffmpeg（音频转录）、Azure Document Intelligence（高保真 PDF）
