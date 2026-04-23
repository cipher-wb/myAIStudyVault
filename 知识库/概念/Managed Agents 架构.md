---
type: concept
title: "Managed Agents 架构"
complexity: intermediate
domain: llm-tooling
aliases:
  - "Claude Managed Agents 四件套"
  - "Agent/Environment/Session/Events 模型"
created: 2026-04-23
updated: 2026-04-23
tags:
  - concept/architecture
  - domain/llm-tooling
  - vendor/anthropic
status: developing
related:
  - "[[Claude Managed Agents]]"
  - "[[Anthropic]]"
  - "[[开始使用 Claude Managed Agents]]"
---

# Managed Agents 架构

[[Claude Managed Agents]] 围绕**四个对象**构建。理解它们的职责分工是用好服务的前提。

```
┌────────────────────────────────────────────────────────────────┐
│                     Agent  (配置模板)                          │
│   ┌───────┐ ┌──────────────┐ ┌───────┐ ┌──────────┐ ┌────────┐ │
│   │ Model │ │ SystemPrompt │ │ Tools │ │ MCP srv  │ │ Skills │ │
│   └───────┘ └──────────────┘ └───────┘ └──────────┘ └────────┘ │
└────────────────────────────────────────────────────────────────┘
            +
┌────────────────────────────────────────────┐
│        Environment (容器模板)              │
│   包、网络访问、运行时配置                 │
└────────────────────────────────────────────┘
            │
            ▼
┌────────────────────────────────────────────┐
│        Session (运行实例)                  │
│   Agent 在 Environment 中执行某个任务      │
└────────────────────────────────────────────┘
            ↕
┌────────────────────────────────────────────┐
│        Events (双向消息)                   │
│  user.message  →  agent.message            │
│                →  agent.tool_use           │
│                →  session.status_idle      │
└────────────────────────────────────────────┘
```

---

## 四个对象详解

### 1. Agent（智能体配置）

**本质**：静态配置的模板，定义"这个 agent 是谁"。

| 字段 | 说明 |
|---|---|
| `model` | 用哪个 Claude 版本（如 `claude-opus-4-7`） |
| `system` | System prompt |
| `tools` | 启用哪些工具（如 `agent_toolset_20260401` 工具集） |
| `mcp_servers` | 外接的 MCP 服务 |
| `skills` | 可复用的技能包 |

**类比**：像一个"岗位职责说明书"，描述这个 agent 的能力边界。

**创建**：`ant beta:agents create ...` → 返回 `agent.id`

### 2. Environment（容器模板）

**本质**：定义 agent 执行工具时所在的**运行环境**。

| 字段 | 说明 |
|---|---|
| `type` | 目前见到 `cloud`（Anthropic 托管） |
| `networking` | 网络访问策略（如 `unrestricted`） |
| *(推测)* packages | 预装包（文档未详述） |

**类比**：像一个"工位"——有哪些工具能用、能不能上网。

**创建**：`ant beta:environments create ...` → 返回 `environment.id`

### 3. Session（运行实例）

**本质**：`Agent` 在 `Environment` 中的**一次具体任务执行**。

**关系**：Session = Agent × Environment × Task

**创建**：`client.beta.sessions.create(agent=..., environment_id=..., title="...")` → 返回 `session.id`

**生命周期**：创建 → 接收 user.message → agent 循环（tool_use） → `session.status_idle`

### 4. Events（双向消息流）

**本质**：session 运行时，应用和 agent 之间通过事件通信。双向流。

**已知事件类型**：

| Event Type | 方向 | 含义 |
|---|---|---|
| `user.message` | 客户端 → agent | 用户提问/指令 |
| `agent.message` | agent → 客户端 | agent 回复文本 |
| `agent.tool_use` | agent → 客户端 | agent 调用了某工具 |
| `session.status_idle` | agent → 客户端 | 任务完成，agent 空闲（可 break 流） |

**SDK 用法**：

```python
with client.beta.sessions.events.stream(session.id) as stream:
    client.beta.sessions.events.send(session.id, events=[...])   # 发 user event
    for event in stream:
        match event.type:
            case "agent.message":      ...
            case "agent.tool_use":     ...
            case "session.status_idle": break
```

---

## 服务端的事件循环

当你发一个 `user.message`，Anthropic 托管侧做这些事（来源：[[开始使用 Claude Managed Agents]]）：

1. **配置容器**（按 Environment 定义 spin up）
2. **运行 agent 循环**（Claude 决定用哪些工具）
3. **执行工具**（在容器内跑）
4. **流式推送 events** 给你
5. **进入空闲**（发 `session.status_idle`）

---

## 设计取舍

- **Agent vs Session 分离**：Agent 可复用，Session 是一次性的 → agent 配置一次，跑无数次任务
- **Environment 独立**：同一个 agent 可以配不同 env（开发环境 vs 生产环境）
- **事件流而非请求-响应**：支持长时间工具执行 + 实时感知 agent 思考过程
- **Beta 命名前缀**：所有 API 都在 `beta:` / `client.beta.*` 下 —— Anthropic 明示接口还会变

---

## 相关

- [[Claude Managed Agents]] — 产品本身
- [[开始使用 Claude Managed Agents]] — 来源文档
- [[ant CLI]] / [[anthropic Python SDK]] — 主要操作工具

> [!gap] 每个对象的完整字段、约束、配额、错误处理等需要 ingest 更多官方文档补齐。
