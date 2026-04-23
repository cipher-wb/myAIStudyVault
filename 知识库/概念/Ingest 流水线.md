---
type: concept
title: "Ingest 流水线"
complexity: intermediate
domain: knowledge-base-ops
aliases:
  - "摄取流水线"
  - "Source Ingest Pipeline"
created: 2026-04-23
updated: 2026-04-23
tags:
  - concept/workflow
  - domain/knowledge-base-ops
status: developing
related:
  - "[[MarkItDown]]"
  - "[[overview]]"
  - "[[getting-started]]"
---

# Ingest 流水线

本知识库把任意格式的源文档变成结构化 wiki 页面的标准化流程。核心理念：**二进制永远不进 wiki**，wiki 只消费 markdown。

---

## 全流程图

```
 ①              ②                  ③                    ④                   ⑤
┌────────┐   ┌──────────────┐   ┌──────────────┐   ┌──────────────┐   ┌──────────────┐
│ 用户丢 │   │ markitdown   │   │ 转换后的 .md │   │ Claude 读取  │   │ 结构化 wiki  │
│ 原件   │──►│ 自动转换     │──►│ 落到对应子   │──►│ 生成页面     │──►│ + 索引更新   │
│        │   │ (按扩展名)   │   │ 文件夹       │   │              │   │              │
└────────┘   └──────────────┘   └──────────────┘   └──────────────┘   └──────────────┘
 .源文档/    .claude/scripts/    .源文档/文章/      知识库/来源/       知识库/index.md
 原始/       md转换.py           .源文档/文字稿/    知识库/实体/       知识库/hot.md
                                 .源文档/截图/      知识库/概念/       知识库/log.md
                                 .源文档/数据/
```

---

## 分阶段详解

### ① 投递（Drop）
用户把任意格式文件放进 `.源文档/原始/`。支持 PDF / DOCX / PPTX / XLSX / MSG / EPUB / HTML / CSV / JSON / XML / JPG / PNG / MP3 / WAV / YouTube URL / ZIP 等。

### ② 转换（Convert）
由 `.claude/scripts/md转换.py` 调用 [[MarkItDown]] 完成。**关键行为**：
- 按扩展名路由到 `.源文档/{文章|文字稿|截图|数据}/` 之一
- 强制 `-o` 输出到文件（避免 Windows GBK 乱码）
- 保留原件（不移动、不删除）
- 目标已存在则跳过，除非 `--force`

**启动方式**：
```bash
python .claude/scripts/md转换.py <文件或URL>      # 单个
python .claude/scripts/md转换.py --all            # 批量 原始/ 下所有
python .claude/scripts/md转换.py <x> --print      # 只预览目标路径不执行
```

### ③ 归位（Route）
| 扩展名 | 去向 |
|---|---|
| pdf / docx / pptx / epub / html / msg / md / txt | `.源文档/文章/` |
| mp3 / wav / m4a / flac / YouTube URL | `.源文档/文字稿/` |
| jpg / jpeg / png / gif / webp / bmp / heic | `.源文档/截图/` |
| xlsx / xls / csv / tsv / json / xml | `.源文档/数据/` |

### ④ 提炼（Extract）
Claude 执行 `/ingest` slash 命令（本质是 `.claude/commands/ingest.md` 里的指令）：
1. `Read` 转换后的 .md
2. 必要时先用 3-5 条要点与用户确认（除非用户说"直接 ingest"）
3. 按 [[WIKI]] schema 生成：
   - `知识库/来源/<stem>.md` 源摘要（必选）
   - `知识库/实体/<Name>.md` 每个提到的人/组织/产品/仓库（必选，可更新已存在）
   - `知识库/概念/<Name>.md` 核心想法/模式（按需）
   - `知识库/对比/*.md` / `知识库/问答/*.md`（按需）

### ⑤ 索引（Index）
- `知识库/index.md`：每类分节加新条目
- `知识库/hot.md`：最近事实 + 变更列表
- `知识库/log.md`：**新条目加顶部**，记录本次 ingest 的完整操作

---

## 不变量（Invariants）

这些是每次 ingest 都必须满足的硬性约束：

- [ ] `.源文档/原始/` 的原件**从不被修改**
- [ ] 每个 wiki 页面都有 YAML frontmatter
- [ ] `sources:` 字段用 wikilink 指回 `.源文档/<类型>/<stem>.md`
- [ ] 文件名在全库唯一（让 `[[stem]]` 无需路径也能解析）
- [ ] 已存在的实体/概念页**更新而非复制**
- [ ] 发现矛盾时用 `> [!contradiction] [[A]] 说 X，[[B]] 说 Y。` 显式标注

---

## 何时**不**走这条流水线

- 在线阅读后手写笔记 → 直接在 `知识库/概念/` 或 `知识库/来源/` 建页，不走原件环节
- 对话中产生的洞见 → `/save` 之类对话归档命令（未来扩展）
- 手改 wiki 页面修补笔误 → 直接编辑，不需要 ingest

---

## 依赖与工具

- [[MarkItDown]] — 核心转换器
- Python 3.12（含 `markitdown[all]` 全量依赖）
- 可选：`ffmpeg`（启用音频转录时）
- 可选：Azure Document Intelligence（更强 PDF 解析，用 `-d -e <endpoint>`）

---

## 相关

- [[MarkItDown]] — 工具详解
- [[getting-started]] — 用户入门
- [[overview]] — 整库概览
