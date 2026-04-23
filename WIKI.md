# WIKI.md — LLM Wiki Schema

> 本文件是 claude-obsidian 系统的完整参考文档。
> 基于 Andrej Karpathy 的 LLM Wiki 模式。

---

## What This Is

你在 Obsidian 知识库中维护一个持久的、可复利增长的 Wiki。你不仅回答问题，还构建和维护一个结构化的知识库。人类负责策划来源和提问，你负责所有写作、交叉引用、归档和维护。

Wiki 是产品，对话只是接口。

---

## Architecture

```
vault/
├── .源文档/                # Layer 1: 不可变源文档
│   ├── 文章/
│   ├── 文字稿/
│   ├── 截图/
│   ├── 数据/
│   └── 素材/
│
├── 知识库/                 # Layer 2: LLM 生成的知识库
│   ├── index.md            # 所有 wiki 页面的主目录
│   ├── log.md              # 所有操作的按时间顺序记录
│   ├── hot.md              # 热缓存：最近上下文摘要（~500 词）
│   ├── overview.md         # 整个 wiki 的执行摘要
│   ├── 来源/               # 每个原始来源一个摘要页
│   ├── 实体/               # 人物、组织、产品、仓库
│   │   └── _index.md
│   ├── 概念/               # 想法、模式、框架
│   │   └── _index.md
│   ├── 对比/               # 并排分析
│   ├── 问答/               # 归档的用户查询答案
│   ├── 画布/               # 可视化画布
│   └── 元数据/             # 仪表板、lint 报告、约定
│
├── _模板/                  # Templater 模板
├── _附件/                  # wiki 页面引用的图片和 PDF
│
├── CLAUDE.md               # Claude Code 项目指令
├── WIKI.md                 # 本文件：完整 schema 参考
└── .obsidian/              # Obsidian 配置（自动管理）
```

### Rules

- `.源文档/` 是只读的。永远不要修改源文件。
- `知识库/` 是你的。自由创建、更新、重命名、删除。
- 每个 wiki 页面都有 frontmatter。无例外。
- 使用 Wikilinks 而非路径。用 `[[Page Name]]` 而非 `[text](path/to/file.md)`。
- 原子化笔记。一个概念一页。如果涵盖两个主题，拆分它。
- 更新而非复制。如果页面已存在，更新它。

---

## Frontmatter Schema

每个 wiki 页面以扁平 YAML frontmatter 开始。无嵌套对象。

### 通用字段（每个页面）：

```yaml
---
type: <source|entity|concept|domain|comparison|question|overview|meta>
title: "Human-Readable Title"
created: 2026-04-23
updated: 2026-04-23
tags:
  - <domain-tag>
  - <type-tag>
status: <seed|developing|mature|evergreen>
related:
  - "[[Other Page]]"
sources:
  - "[[.源文档/文章/source-file.md]]"
---
```

### 类型特定附加字段：

**source**: `source_type`, `author`, `date_published`, `url`, `confidence` (high|medium|low), `key_claims` (list)

**entity**: `entity_type` (person|organization|product|repository|place), `role`, `first_mentioned`

**concept**: `complexity` (basic|intermediate|advanced), `domain`, `aliases` (list)

**comparison**: `subjects` (wikilinks list), `dimensions` (list), `verdict` (one line)

**question**: `question` (original query), `answer_quality` (draft|solid|definitive)

---

## Operations

### INGEST — 单源

1. 完整阅读源文件
2. 与用户讨论关键要点（如果用户说"直接 ingest"则跳过）
3. 在 `知识库/来源/` 创建源摘要
4. 为每个提到的人物/组织/产品创建或更新实体页面
5. 为重要想法创建或更新概念页面
6. 更新 `知识库/overview.md`、`知识库/index.md`、`知识库/hot.md`
7. 追加到 `知识库/log.md`（新条目在顶部）
8. 检查矛盾并用 `> [!contradiction]` 标注

### QUERY — 回答问题

1. 先读 `知识库/hot.md`
2. 读 `知识库/index.md` 找到相关页面
3. 读这些页面（通常 3-5 个）
4. 综合回答并引用 wikilinks
5. 提议归档到 `知识库/问答/`

### LINT — 健康检查

检查：孤立页面、死链接、过时声明、缺失的交叉引用、frontmatter 缺陷、空白部分。
输出：`知识库/元数据/lint-report-YYYY-MM-DD.md`

---

## Context Window Management

- 先读 `hot.md`，可能已有答案
- 其次读 `index.md`
- 每次查询只读 3-5 页，10+ 太多
- 保持 wiki 页面简短，100-300 行，长的要拆分
- 不要将 wiki 内容粘贴到聊天中，除非用户要求

---

## Conventions

### Naming
- **文件名**: Title Case with spaces (`Machine Learning.md`)
- **文件夹**: 中文名（例如 `知识库/数据模型/`）
- **标签**: lowercase, hierarchical (`#domain/architecture`)
- **唯一文件名** 以便 wikilinks 无需路径

### Writing Style
- 陈述性，现在时。"X uses Y" 而非 "X basically does Y."
- 大量链接。每次提到 wiki 页面都加 wikilink。
- 引用来源：`(Source: [[Page]])`。
- 标记不确定性：`> [!gap] This needs more evidence.`
- 标记矛盾：`> [!contradiction] [[Page A]] claims X, but [[Page B]] says Y.`

---

*Based on Andrej Karpathy's LLM Wiki pattern.*
