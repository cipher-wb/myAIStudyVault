---
type: entity
title: "MarkItDown"
entity_type: product
role: "文档 → Markdown 转换工具（LLM 预处理管道）"
created: 2026-04-23
updated: 2026-04-23
tags:
  - tool/ingest
  - org/microsoft
  - domain/llm-tooling
status: developing
related:
  - "[[Ingest 流水线]]"
  - "[[overview]]"
sources:
  - "https://github.com/microsoft/markitdown"
first_mentioned: 2026-04-23
---

# MarkItDown

由 Microsoft 开源的 Python 工具，把**各种格式的文档转成 LLM 友好的 Markdown**。目标不是"高保真还原给人看"，而是"给 LLM 喂一份干净可检索的文本"。在本知识库里，它是 [[Ingest 流水线]] 的第一步。

---

## 支持格式一览

| 类别 | 格式 | 备注 |
|---|---|---|
| 文档 | PDF, DOCX, DOC, PPTX, PPT, RTF, ODT, EPUB | PDF 用 pdfminer/pdfplumber；PPTX 支持 LLM 图片描述 |
| 网页 | HTML, HTM | |
| 邮件 | MSG (Outlook) | |
| 数据 | XLSX, XLS, CSV, TSV, JSON, XML | Excel 转为 Markdown 表格 |
| 图片 | JPG/PNG/... | EXIF + OCR（LLM 描述需配置） |
| 音频 | MP3, WAV | EXIF + 语音转文字 |
| 视频 | YouTube URL | 抓取字幕 |
| 打包 | ZIP | 递归处理内容 |

---

## 安装

```bash
pip install 'markitdown[all]'               # 全量依赖（最省心）
pip install 'markitdown[pdf,docx,pptx]'     # 按需
```

可选 extras：`pptx` / `docx` / `xlsx` / `xls` / `pdf` / `outlook` / `az-doc-intel` / `audio-transcription` / `youtube-transcription`。

**本知识库已安装**：Python 3.12 和 3.14 双环境皆装 `markitdown[all]` 0.1.5。

---

## CLI 用法

```bash
# 最常用：输入文件 → 指定输出
markitdown input.pdf -o output.md

# stdin 管道
cat input.pdf | markitdown > output.md

# 启用插件
markitdown --use-plugins input.pdf -o output.md
markitdown --list-plugins

# 使用 Azure Document Intelligence（更强的 PDF 解析）
markitdown input.pdf -o output.md -d -e "<endpoint>"
```

> [!warn]
> **Windows 坑**：直接 `>` 重定向会走 GBK 编码导致中文乱码。**必须用 `-o` 让 markitdown 自己写 UTF-8 文件**。本库的 `.claude/scripts/md转换.py` 已处理这一点。

---

## Python API

```python
from markitdown import MarkItDown
md = MarkItDown(enable_plugins=False)
result = md.convert("file.pdf")
print(result.text_content)
```

启用 LLM 图片描述（仅对 PPTX 和图片文件原生支持）：

```python
from openai import OpenAI
md = MarkItDown(
    llm_client=OpenAI(),
    llm_model="gpt-4o",
    llm_prompt="可选的自定义 prompt",
)
```

更细粒度 API：`convert_local()` / `convert_stream()` / `convert_response()`。

---

## 已知限制

- 输出是给 LLM 看的，不追求人类阅读的排版保真
- 原生 LLM 图片描述仅支持 PPTX + 图片；PDF/DOCX 内嵌图的 OCR 需装 `markitdown-ocr` 插件
- 音频转录需 `[audio-transcription]` extras + 系统有 `ffmpeg`
- YouTube 需 `[youtube-transcription]` extras
- **安全**：`convert()` 对不可信输入要限制 URI 协议，封掉 loopback / link-local / 元数据服务地址

---

## 在本知识库中的集成

- 工具调用位置：`.claude/scripts/md转换.py`
- 流水线说明：[[Ingest 流水线]]
- Slash 命令：`/ingest <文件或URL>`
- 工作目录映射：
  - 原件丢 `源文档/原始/`
  - 脚本按扩展名分流到 `源文档/{文章|文字稿|截图|数据}/<stem>.md`
- 后续由 Claude 基于 `.md` 创建 `知识库/来源/<stem>.md` 源摘要 + 实体 + 概念页

---

## 相关

- [[Ingest 流水线]] — 本库如何用 MarkItDown
- 竞品：pandoc（更偏格式互转，不专为 LLM）、llamaparse（收费，高保真 PDF）、Unstructured（分块友好）
