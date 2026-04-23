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
2026-04-23 — vault 基础设施就绪，已清空测试内容，等待首次正式 ingest

## Key Recent Facts
- 基于 Andrej Karpathy 的 LLM Wiki 模式构建 AI 学习知识库，Mode E (Research)
- **基础设施已就位**：
  - 目录：`源文档/{原始,文章,文字稿,截图,数据,素材}/` 和 `知识库/{来源,实体,概念,对比,问答,元数据,画布}/`
  - 工具：markitdown 0.1.5（Python 3.12 + 3.14 均装了 `[all]` extras）
  - 脚本：`.claude/scripts/md转换.py`（按扩展名自动分流）
  - 命令：`.claude/commands/ingest.md`（`/ingest` slash 命令）
  - Web Clipper：Vault = AI学习，Note location = `源文档/文章/`
  - 版本控制：Git 已初始化，remote → github.com/cipher-wb/myAIStudyVault，obsidian-git 30 分钟自动备份
- **关键限制**：Obsidian 禁止外部工具（Web Clipper 等）写入 `.` 开头的文件夹
- **Windows 坑**：markitdown 输出必须用 `-o` 写文件（`>` 重定向会被 cmd GBK 吃掉）

## Recent Changes
- Reset: 清空所有测试 ingest 的实体/概念/来源页面，回到"刚搭完基础设施"的状态

## Active Threads
- 等待投递第一批真实源文档进行 ingest
- 可选增强：配置 ffmpeg（音频转录）、Azure Document Intelligence（高保真 PDF）
