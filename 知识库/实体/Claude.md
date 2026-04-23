---
type: entity
title: "Claude"
entity_type: product
role: "Anthropic 旗下的 LLM 家族"
created: 2026-04-23
updated: 2026-04-23
tags:
  - product/llm
  - vendor/anthropic
  - domain/llm
status: seed
related:
  - "[[Anthropic]]"
  - "[[Claude Managed Agents]]"
aliases:
  - "Claude 模型"
  - "Claude Models"
sources:
  - "[[开始使用 Claude Managed Agents]]"
first_mentioned: 2026-04-23
---

# Claude

[[Anthropic]] 的 LLM 家族。按能力/成本分三条产品线：

| 档次 | 定位 | 典型场景 |
|---|---|---|
| **Opus** | 旗舰，最强推理 | 复杂 agent、长上下文、深度分析 |
| **Sonnet** | 平衡，性价比 | 日常 API 调用、工具使用 |
| **Haiku** | 轻量，快速 | 分类、简单摘要、高吞吐 |

## 已知版本（来自本库已 ingest 的文档）

- `claude-opus-4-7` — 见于 [[开始使用 Claude Managed Agents]] 的示例配置

> [!gap] 完整版本矩阵、模型卡、价格等需要 ingest Anthropic 专门的 model card 文档。

## 调用方式

- **Messages API**（直接调用模型）
- **Claude Code**（命令行 agent，基于本机执行）
- **[[Claude Managed Agents]]**（Anthropic 托管的 agent 运行时，beta）
- **Console** 交互界面：https://claude.ai/
- **第三方集成**：Amazon Bedrock、Google Vertex AI 等

## 相关

- [[Anthropic]] — 提供方
- [[Claude Managed Agents]] — 托管 agent 运行时

---

*注：seed 页，主要是为了让后续提到"Claude"的文档能锚定到同一个实体。*
