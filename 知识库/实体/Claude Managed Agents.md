---
type: entity
title: "Claude Managed Agents"
entity_type: product
role: "Anthropic 托管的智能体运行时（容器化环境 + 流式事件）"
created: 2026-04-23
updated: 2026-04-23
tags:
  - product/agent-runtime
  - vendor/anthropic
  - domain/llm-tooling
  - beta
status: developing
related:
  - "[[Anthropic]]"
  - "[[Claude]]"
  - "[[Managed Agents 架构]]"
  - "[[ant CLI]]"
  - "[[anthropic Python SDK]]"
sources:
  - "[[开始使用 Claude Managed Agents]]"
first_mentioned: 2026-04-23
---

# Claude Managed Agents

由 [[Anthropic]] 提供的**托管智能体服务**。你把 agent 配置和任务提交上去，Anthropic 负责跑容器、执行工具、流式推送执行过程。相比自己手搓 agent loop + 工具沙箱，省掉了运维那一半。

当前处于 **beta** 阶段，所有 API 调用需带请求头：`anthropic-beta: managed-agents-2026-04-01`（SDK 自动处理）。

---

## 定位

| 对比维度 | Claude Managed Agents | 自建 agent loop |
|---|---|---|
| 模型调度 | 托管 | 自己写 |
| 工具执行环境 | 托管容器 | 自己搭 Docker / vm |
| 流式事件 | 开箱即用 | 自己设计协议 |
| 工具集 | `agent_toolset_20260401` 一把抓 | 逐个接 |
| 部署复杂度 | 几条 CLI | 几百行代码 + 运维 |
| 控制粒度 | 配置化 | 代码级全控 |

**一句话**：对标 OpenAI Assistants API + Code Interpreter 的组合，但以 [[Claude]] 为大脑。

---

## 四大对象模型

详见 [[Managed Agents 架构]]。简言之：

```
Agent  (配置模板)  +  Environment  (容器模板)  →  Session  (运行实例)
                                                     ↕
                                                  Events
                                                  (双向)
```

---

## 入门路径

1. 装 [[ant CLI]]：`brew install anthropics/tap/ant`
2. 装 [[anthropic Python SDK]]：`pip install anthropic`
3. 设 `ANTHROPIC_API_KEY` 环境变量
4. 依次创建 Agent / Environment / Session
5. `client.beta.sessions.events.stream(session.id)` 开流、发 event、处理响应

完整可跑的 quickstart 见 [[开始使用 Claude Managed Agents]]。

---

## 工具集

- `agent_toolset_20260401` —— 预置工具集类型，包含 bash / 文件操作 / 网络搜索等。完整列表见官方 *工具* 文档（本库尚未 ingest）。
- 也可以选择性启用单个工具或接 MCP server。

---

## 关键事件类型

- `user.message` —— 你发给 agent 的文本/多模态输入
- `agent.message` —— agent 回复
- `agent.tool_use` —— agent 调用了某个工具
- `session.status_idle` —— agent 完成任务进入空闲（break 流的信号）

还有更多事件类型（错误、中断、status 变化等），待后续文档 ingest 补齐。

---

## 价格/限制

> [!gap] 本来源（quickstart）未涵盖。需 ingest 定价文档。

---

## 相关页面

- [[Anthropic]] — 提供方
- [[Claude]] — 大脑（默认 `claude-opus-4-7`）
- [[Managed Agents 架构]] — 对象模型详解
- [[ant CLI]]、[[anthropic Python SDK]] — 主要 SDK
- [[开始使用 Claude Managed Agents]] — 来源文档
