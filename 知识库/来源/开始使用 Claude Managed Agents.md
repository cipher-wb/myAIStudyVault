---
type: source
title: "开始使用 Claude Managed Agents"
source_type: documentation
author: Anthropic
date_published:
url: "https://platform.claude.com/docs/zh-CN/managed-agents/quickstart"
created: 2026-04-23
updated: 2026-04-23
confidence: high
tags:
  - source/docs
  - domain/llm-tooling
  - vendor/anthropic
status: developing
related:
  - "[[Claude Managed Agents]]"
  - "[[Managed Agents 架构]]"
  - "[[Anthropic]]"
  - "[[ant CLI]]"
  - "[[anthropic Python SDK]]"
sources:
  - "[[源文档/文章/开始使用 Claude Managed Agents.md]]"
key_claims:
  - "Managed Agents 是由 Anthropic 托管的智能体运行服务，容器化环境 + 流式事件"
  - "四大核心概念：Agent、Environment、Session、Events"
  - "所有 API 调用需带 `managed-agents-2026-04-01` beta 请求头（SDK 自动处理）"
  - "`agent_toolset_20260401` 工具类型一键启用预置工具集（bash、file、web 搜索等）"
  - "工作流：创建 Agent → 创建 Environment → 创建 Session → 发送 events 并 stream 响应"
---

# 开始使用 Claude Managed Agents

> **来源**：Anthropic 官方文档 — [platform.claude.com/docs/zh-CN/managed-agents/quickstart](https://platform.claude.com/docs/zh-CN/managed-agents/quickstart)
> **原件**：[[源文档/文章/开始使用 Claude Managed Agents.md]]（Web Clipper 剪藏）

## TL;DR

Anthropic 的 [[Claude Managed Agents]] 快速入门文档。讲清了**四大对象模型**、**安装 CLI/SDK**、**创建首个 session 并流式接收响应**的完整 Hello World。

## 核心概念（四件套）

详见 [[Managed Agents 架构]]。

| 对象 | 本质 |
|---|---|
| **Agent** | 模型 + system prompt + tools + MCP servers + skills 的捆绑配置 |
| **Environment** | 容器模板：包、网络访问等 |
| **Session** | Agent 在某个 Environment 中的运行实例，执行具体任务 |
| **Events** | 应用 ↔ agent 之间的消息（user.message / agent.message / agent.tool_use / session.status_idle …） |

## 关键 API/工具

- [[ant CLI]] — `brew install anthropics/tap/ant` 安装，用于 agent/environment 的 CRUD
- [[anthropic Python SDK]] — `pip install anthropic`，用于创建 session + stream events
- **Beta 请求头**：`managed-agents-2026-04-01`（SDK 自动加，手搓 HTTP 时别忘）
- **工具集**：`agent_toolset_20260401` → 开箱即用的 bash / file / web 搜索 等

## 最小工作流

```
1. ant beta:agents create ...             → 得到 agent.id
2. ant beta:environments create ...       → 得到 environment.id
3. client.beta.sessions.create(agent, env) → 得到 session
4. client.beta.sessions.events.stream(session.id):
      send user event
      for event in stream: match event.type { agent.message | agent.tool_use | session.status_idle ... }
```

## 示例 Agent 配置要点

```text
--name   "Coding Assistant"
--model  '{id: claude-opus-4-7}'
--system "..."
--tool   '{type: agent_toolset_20260401}'
```

## 事件生命周期（文档描述）

当用户发 event，服务端会：

1. **配置容器**（按 environment 定义）
2. **运行 agent 循环**（Claude 决定用哪些工具）
3. **执行工具**（在容器内运行）
4. **流式推送 events**
5. **进入空闲**（发出 `session.status_idle`）

## 未覆盖（待后续 ingest 补齐）

> [!gap] 本来源是 quickstart，以下主题需要更深文档来补齐：
> - Agent 版本管理与复用（文档末尾链接 *"定义您的智能体"*）
> - Environment 的详细网络/安全配置
> - 工具列表与每个工具的配置项
> - Events & Streaming 的高级用法（引导、中断、重试等）

## 与知识库其他页面的关联

- 工具生态：对比 [[MarkItDown]]（本库另一个 Anthropic 生态外的工具），这是 Anthropic 的**第一方 agent 运行时**
- 流水线位置：Managed Agents 是"让 Claude 可以真正执行任务"的层；[[Ingest 流水线]] 是"让本地知识库积累信息"的层，两者互补
