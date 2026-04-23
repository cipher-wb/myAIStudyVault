---
type: meta
title: "Hot Cache"
updated: 2026-04-23
tags:
  - meta
  - hot-cache
status: evergreen
---

# Recent Context

## Last Updated
2026-04-23 — 接入 [[MarkItDown]] 作为 [[Ingest 流水线]] 的转换层；vault 文件夹中文化完成

## Key Recent Facts
- 基于 Andrej Karpathy 的 LLM Wiki 模式构建 AI 学习知识库
- 使用 Mode E (Research) 作为主要模式
- 源文档 → wiki 的摄取流水线已就位：`.源文档/原始/` → markitdown → `.源文档/{文章|文字稿|截图|数据}/` → `/ingest` 命令
- MarkItDown 已全量安装（Python 3.12 + 3.14 均可，版本 0.1.5）
- Windows 坑提醒：markitdown 输出必须用 `-o` 写文件，不能 `>` 重定向（GBK 乱码）

## Recent Changes
- Created: [[MarkItDown]], [[Ingest 流水线]]
- Created: `.claude/scripts/md转换.py` 转换脚本，`.claude/commands/ingest.md` slash 命令
- Created: `.源文档/原始/` 原件投递文件夹
- Renamed: 全 vault 文件夹中文化（.raw → .源文档、wiki → 知识库 等）

## Active Threads
- 等待用户投递第一个真实源文档进行 ingest 实战
- 可选增强：配置 ffmpeg（音频转录）、Azure Document Intelligence（高保真 PDF）
