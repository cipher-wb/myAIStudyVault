---
type: entity
title: "anthropic Python SDK"
entity_type: product
role: "Anthropic 官方 Python 客户端库"
created: 2026-04-23
updated: 2026-04-23
tags:
  - tool/sdk
  - vendor/anthropic
  - lang/python
  - domain/llm-tooling
status: seed
related:
  - "[[Anthropic]]"
  - "[[Claude]]"
  - "[[Claude Managed Agents]]"
  - "[[ant CLI]]"
aliases:
  - "anthropic-sdk-python"
  - "anthropic Python client"
sources:
  - "[[开始使用 Claude Managed Agents]]"
first_mentioned: 2026-04-23
---

# anthropic Python SDK

Anthropic 官方的 Python 客户端库。覆盖 Messages API、[[Claude Managed Agents]]、流式事件等。

## 安装

```bash
pip install anthropic
```

环境变量：

```bash
export ANTHROPIC_API_KEY="sk-ant-..."
```

## Managed Agents 相关 API

处于 `client.beta.*` 命名空间（beta 阶段）：

```python
from anthropic import Anthropic
client = Anthropic()  # 读环境变量中的 API key

# 创建 session
session = client.beta.sessions.create(
    agent=agent_id,
    environment_id=environment_id,
    title="Quickstart session",
)

# 流式收发事件
with client.beta.sessions.events.stream(session.id) as stream:
    client.beta.sessions.events.send(
        session.id,
        events=[{"type": "user.message", "content": [{"type": "text", "text": "..."}]}],
    )
    for event in stream:
        match event.type:
            case "agent.message":     ...
            case "agent.tool_use":    ...
            case "session.status_idle": break
```

## Beta 请求头

SDK 自动注入 `anthropic-beta: managed-agents-2026-04-01`，手搓 HTTP 时需要手动加。

## 相关

- [[Anthropic]] — 维护方
- [[Claude]] — 主要模型
- [[ant CLI]] — 姊妹命令行工具
- [[Claude Managed Agents]] — beta 功能
- [[开始使用 Claude Managed Agents]] — 引入来源

---

> [!gap] 本页仅覆盖来源文档提到的 Managed Agents 部分 API。Messages API、工具使用、流式标准响应等需后续 ingest。
