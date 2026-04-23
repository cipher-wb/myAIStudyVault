# AI学习 — LLM Wiki

Mode: E (Research)
Purpose: AI 学习知识库，持续积累 AI 领域的知识、概念、论文和工具
Owner: User
Created: 2026-04-23

## Structure

```
vault/
├── 源文档/           # 源文档（不可变，只读）
│   ├── 文章/
│   ├── 文字稿/
│   ├── 截图/
│   ├── 数据/
│   └── 素材/
├── 知识库/            # LLM 生成的知识库
│   ├── index.md       # 主目录
│   ├── log.md         # 操作日志（追加式）
│   ├── hot.md         # 热缓存（最近上下文摘要）
│   ├── overview.md    # 总览
│   ├── 来源/          # 每个源文件的摘要页
│   ├── 实体/          # 人物、组织、产品、仓库
│   │   └── _index.md
│   ├── 概念/          # 想法、模式、框架
│   │   └── _index.md
│   ├── 对比/          # 对比分析
│   ├── 问答/          # 归档的问答
│   ├── 元数据/        # 仪表板、lint 报告、约定
│   └── 画布/          # 可视化画布
├── _模板/             # Templater 模板
├── _附件/             # 图片和 PDF
└── WIKI.md            # 完整 schema 参考
```

## Conventions

- 所有笔记使用 YAML frontmatter：type, status, created, updated, tags（最低要求）
- Wikilinks 使用 [[Note Name]] 格式 — 文件名唯一，无需路径
- 源文档/ 包含源文档 — 永远不要修改它们
- 知识库/index.md 是主目录 — 每次 ingest 后更新
- 知识库/log.md 是追加式的 — 新条目放在顶部，不要编辑过去的条目

## Operations

### Ingest（摄取源文档）
**流水线**：原件丢 `源文档/原始/` → `markitdown` 自动转 md → `/ingest` 命令提炼为 wiki 页面。

- **任何格式**（PDF/DOCX/PPTX/XLSX/MSG/EPUB/HTML/图片/音频/YouTube URL/ZIP …）丢到 `源文档/原始/`
- 跑 `python .claude/scripts/md转换.py --all` 或 `python .claude/scripts/md转换.py <单个文件>`
  - 脚本按扩展名自动分流到 `源文档/{文章|文字稿|截图|数据}/<stem>.md`
  - **Windows 下必须用 `-o` 写文件**（markitdown stdout 是 UTF-8，直接 `>` 会被 cmd GBK 吃掉）
- 用户说 `/ingest <文件>` 或直接说 "ingest [文件名]"
- Claude 读转换后的 md，按 [[WIKI]] schema 生成 `知识库/来源/`、`知识库/实体/`、`知识库/概念/` 页面
- **原件不可修改**；转换后的 md 是来源摘要的引用目标，也不要动

详见 [[Ingest 流水线]] 和 [[MarkItDown]]。

### Query（查询）
提问 — Claude 先读 `知识库/hot.md` → `知识库/index.md` → 相关页面（3-5 个），综合回答并引用 wikilinks。

### Lint（健康检查）
说 "lint the wiki" —— 检查孤立页面、死链接、frontmatter 缺陷、过时声明，输出 `知识库/元数据/lint-report-YYYY-MM-DD.md`。

## Cross-Project Access

When you need context not already in this project:
1. Read 知识库/hot.md first (recent context, ~500 words)
2. If not enough, read 知识库/index.md
3. If you need domain specifics, read 知识库/<domain>/_index.md
4. Only then read individual wiki pages

Do NOT read the wiki for general coding questions or things already in this project.
