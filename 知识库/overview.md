---
type: overview
title: "AI学习知识库总览"
created: 2026-04-23
updated: 2026-04-25
tags:
  - meta
  - overview
status: seed
related:
  - "[[index]]"
  - "[[log]]"
  - "[[hot]]"
---

# AI学习知识库总览

## Purpose

这是一个基于 LLM Wiki 模式的 AI 学习知识库。每个你添加的源文件会被处理为 8-15 个交叉引用的 wiki 页面。每个你提出的问题会从所有已读内容中综合答案。知识像利息一样复利增长。

## Architecture

- **`.源文档/`** — 原始源文档（只读，不可修改）
- **`知识库/`** — Claude 生成的知识库（可自由创建和更新）
- **`_模板/`** — Templater 模板
- **`_附件/`** — 图片和 PDF 附件

## How to Use

1. **Ingest**: 将源文件放入 `.源文档/`，告诉 Claude "ingest [文件名]"
2. **Query**: 提问，Claude 会先读取索引再深入相关页面
3. **Lint**: 定期说 "lint the wiki" 进行健康检查

## Current State

- 模式：E (Research)
- 页面数：24
- 已处理源：3
- 知识领域：Git 版本控制 / Vibe Coding 工具链 / Next.js 全栈开发 / OpenClaw Bot 网关 / API 代充服务 / GPT-Image-2
- 下一步：学习 GPT-Image-2 API 详细用法，构建稳定的图像生成 skill

---

*Based on [Andrej Karpathy's LLM Wiki pattern](https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f).*
