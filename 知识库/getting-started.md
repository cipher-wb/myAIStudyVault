---
type: meta
title: "Getting Started"
updated: 2026-04-23
tags:
  - meta
  - onboarding
status: evergreen
related:
  - "[[index]]"
  - "[[overview]]"
  - "[[hot]]"
---

# Getting Started

欢迎！这是你的 AI 学习知识库 — 一个基于 Claude 和 Obsidian 的持久化"第二大脑"。

每个你添加的源文件会被处理为 8-15 个交叉引用的 wiki 页面。每个你提出的问题会从所有已读内容中综合答案。知识像利息一样复利增长。

---

## 三步快速开始

### 1. 放入源文件

将任何文档放入 `.源文档/` 文件夹：
- PDF、Markdown 文件、文字稿、文章
- 或粘贴 URL 让 Claude 抓取

### 2. Ingest

在 Claude Code 中输入：

```
ingest [文件名]
```

Claude 会读取源文件，创建 8-15 个 wiki 页面，交叉引用所有内容，并更新 `知识库/index.md`、`知识库/log.md` 和 `知识库/hot.md`。

### 3. 提问

```
what do you know about [topic]?
```

Claude 读取热缓存，扫描索引，深入相关页面，给你一个综合答案 — 引用具体的 wiki 页面，而非训练数据。

---

## 关键命令

| 你说的 | Claude 做的 |
|--------|------------|
| `ingest [file]` | 从源文件创建 8-15 个 wiki 页面 |
| `what do you know about X?` | 查询 wiki，引用页面 |
| `/save` | 将当前对话归档为 wiki 笔记 |
| `/autoresearch [topic]` | 自主搜索网络、抓取、综合、归档 |
| `lint the wiki` | 健康检查 — 找到孤立页面、缺口、过时链接 |
| `update hot cache` | 刷新会话上下文摘要 |

---

## 导航知识库

- **[[index]]** — 主目录，按类型列出所有页面
- **[[overview]]** — 知识库内容执行摘要
- **[[hot]]** — 最近上下文缓存
- **[[log]]** — 操作日志

---

*基于 Andrej Karpathy 的 LLM Wiki 模式。*
