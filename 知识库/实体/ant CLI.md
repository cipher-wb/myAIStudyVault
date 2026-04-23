---
type: entity
title: "ant CLI"
entity_type: product
role: "Anthropic 官方命令行工具，主要用于 Managed Agents 的 agent/environment 管理"
created: 2026-04-23
updated: 2026-04-23
tags:
  - tool/cli
  - vendor/anthropic
  - domain/llm-tooling
status: seed
related:
  - "[[Anthropic]]"
  - "[[Claude Managed Agents]]"
  - "[[anthropic Python SDK]]"
sources:
  - "[[开始使用 Claude Managed Agents]]"
first_mentioned: 2026-04-23
---

# ant CLI

Anthropic 官方的命令行工具。主要场景是管理 [[Claude Managed Agents]] 的资源（Agent、Environment 等）。

## 安装

```bash
# macOS（Homebrew）
brew install anthropics/tap/ant

# macOS 取消 Gatekeeper 隔离
xattr -d com.apple.quarantine "$(brew --prefix)/bin/ant"

# 验证
ant --version
```

> [!gap] Windows / Linux 安装方式需 ingest 补充文档。

## 常用命令（已知）

```bash
# 创建 Agent
ant beta:agents create \
  --name "Coding Assistant" \
  --model '{id: claude-opus-4-7}' \
  --system "You are a helpful coding assistant..." \
  --tool '{type: agent_toolset_20260401}'

# 创建 Environment
ant beta:environments create \
  --name "quickstart-env" \
  --config '{type: cloud, networking: {type: unrestricted}}'
```

注意 beta 前缀（`beta:agents`、`beta:environments`）—— 服务处于 beta 阶段。

## 与 SDK 的分工

- **[[ant CLI]]**：一次性资源管理（创建、列出、删除 agent/environment）
- **[[anthropic Python SDK]]**：运行时交互（发 events、接 stream）

典型工作流：用 CLI 配好 agent+env，把 id 固化到代码里，然后用 SDK 跑 session。

## 相关

- [[Anthropic]] — 维护方
- [[Claude Managed Agents]] — 主要操作对象
- [[anthropic Python SDK]] — 兄弟工具
