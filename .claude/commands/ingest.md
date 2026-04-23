---
description: 摄取一个源文件到 wiki——先用 markitdown 转为 markdown，再创建/更新相应的 wiki 页面
allowed-tools: Bash, Read, Write, Edit, Glob, Grep
---

# /ingest — 源文件摄取流水线

## 输入
用户参数：`$ARGUMENTS`（可以是文件名、相对路径、绝对路径或 URL；若为空则扫描 `.源文档/原始/` 全部未转换的文件）。

## 流程

### 1. 预处理（自动转换为 markdown）

- 如果 `$ARGUMENTS` 为空：
  ```
  python .claude/scripts/md转换.py --all
  ```
- 否则：
  ```
  python .claude/scripts/md转换.py "$ARGUMENTS"
  ```
- 脚本会按扩展名自动把转换结果放到 `.源文档/{文章|文字稿|截图|数据}/<stem>.md`。
- 若原件已是 `.md` 且在 `.源文档/文章/` 下，直接进入下一步，不重复转换。
- 转换失败则中止，报错给用户并建议手动处理。

### 2. 完整阅读

用 `Read` 工具读取转换后的 `.源文档/<类型>/<stem>.md`。必要时同时读取原件（尤其 PDF 保留图表信息时）。

### 3. 与用户确认要点（可跳过）

除非用户明确说"直接 ingest"，否则先用 3-5 条要点概述，问用户是否继续。

### 4. 创建 wiki 页面

按 `WIKI.md` 的 schema：

- **来源摘要**：`知识库/来源/<stem>.md`
  - frontmatter：`type: source`、`source_type`、`author`、`date_published`、`url`、`confidence`、`key_claims`
  - 链接回原件：`sources: "[[.源文档/<类型>/<stem>.md]]"`
- **实体页**：每个提到的人物/组织/产品/仓库 → `知识库/实体/<Name>.md`（若已存在则更新）
- **概念页**：每个核心想法/模式 → `知识库/概念/<Name>.md`（若已存在则更新）

### 5. 更新索引

- `知识库/index.md`：在对应分节（Sources / Entities / Concepts）加一行
- `知识库/hot.md`：把本次 ingest 的关键事实加到 "Key Recent Facts"，Recent Changes 列出新页面
- `知识库/log.md`：**新条目加在顶部**，格式：
  ```markdown
  ## [YYYY-MM-DD] ingest | <源文件标题>
  - Operation: Ingest `<类型>/<stem>.md`
  - Pages created: [[...]], [[...]], ...
  - Pages updated: [[...]], ...
  - Key insight: <一句话>
  ```

### 6. 矛盾检查

与已有 wiki 页面比对，若发现冲突用 `> [!contradiction] [[Page A]] 说 X，但 [[Page B]] 说 Y。` 标注。

## 注意事项

- **`.源文档/` 是只读的**：永远不要修改 `.源文档/原始/` 里的原件，也不要删除转换后的 `.md`（它是来源摘要的引用目标）。
- **wikilinks 用文件名不用路径**（文件名全库唯一）。
- **优先更新已有页面**而非创建同名新页。
- 若文档 > 300 行，在 wiki 页面中拆分多个原子概念而不是塞进一页。
