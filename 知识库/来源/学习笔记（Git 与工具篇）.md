---
type: source
title: "学习笔记（Git 与工具篇）"
source_type: course-notes
author: 熠辉（Vibe Coding 实战课）
date_published:
url: "https://www.bilibili.com/cheese/play/ep24104388"
created: 2026-04-23
updated: 2026-04-23
confidence: high
tags:
  - source/course-notes
  - domain/web-dev
  - domain/git
  - domain/tools
status: developing
related:
  - "[[Git]]"
  - "[[GitHub]]"
  - "[[VS Code]]"
  - "[[shadcn/ui]]"
  - "[[Vercel]]"
  - "[[Git 版本控制]]"
  - "[[Vibe Coding 工具链]]"
sources:
  - "[[.源文档/文字稿/学习笔记.md]]"
  - "[[.源文档/文章/2.1 AI 时代的前后端开发核心概念与最佳实践.md]]"
key_claims:
  - "Git 是编程中控制版本的最重要的工具，是 AI 更改的后悔药"
  - "VS Code + Claude Code 插件 ≈ Cursor，可替代使用"
  - "shadcn/ui 可用于参考 UI 组件动态效果，帮助向 AI 描述需求"
  - "Local Images Plus 插件配合 Web Clipper 可将外链图片本地化"
  - "新手不需要购买服务器就能通过 Vercel 免费部署全栈项目"
---

# 学习笔记（Git 与工具篇）

> **来源**：【熠辉】面向新手的 Vibe Coding 实战课
> **平台**：Bilibili 付费课程
> **原件**：[[.源文档/文字稿/学习笔记.md]]（微信文档剪藏）

## TL;DR

Vibe Coding 实战课的学习笔记，本篇覆盖 **Git 版本管理**（概念 + Cursor UI + 命令行）和 **开发工具链**（VS Code 插件、UI 组件参考、部署平台）。Next.js 框架部分见 [[学习笔记（Next.js 全栈开发篇）]]。

---

## 工具链概览

| 工具 | 用途 | 备注 |
|---|---|---|
| [[VS Code]] + Claude Code 插件 | 代码编辑 + AI 编程 | ≈ Cursor，可替代 |
| Live Server | 本地预览 HTML | VS Code 插件 |
| [[shadcn/ui]] | UI 组件参考 | 不知如何描述动态效果时查阅 |
| Vercel 模板 | 网页设计模板 | https://vercel.com/templates/next.js |
| Local Images Plus | Obsidian 外链图片本地化 | 配合 Web Clipper 使用 |
| [[GitLens]] | VS Code Git 可视化 | 查看 commit graph、回退版本 |

---

## Git 版本控制

详见 [[Git 版本控制]]。

### 核心命令速查

```bash
git init                  # 初始化仓库
git clone <url>           # 克隆远程仓库
git add .                 # 添加所有改动到暂存区
git commit -m "说明"      # 提交
git push origin main      # 推送到远程
git pull                  # 拉取远程更新
git status                # 查看当前状态
git branch <name>         # 创建分支
git switch <name>         # 切换分支
git merge <branch>        # 合并分支
git reset <commit-id>     # 回退到某次提交
git push --force          # 强制推送（覆盖远程历史，危险！）
```

### Git vs GitHub

![[ingest/git-concept.png]]

![[ingest/github-concept.png]]

**Git** = 本地版本控制系统（完全离线、追踪文件变化）
**GitHub** = 基于 Git 的云端托管服务（远程仓库、PR、Issues、Actions）

### Cursor 中的 Git 操作（UI）

1. **初始化**：点击「初始化项目」
2. **查看状态**：左侧【更改】面板
3. **添加暂存区**：点击文件旁的 + 号
4. **提交**：输入提交信息 → 点击提交
5. **推送**：点击【远程】→【添加远程存储库】→ 推送
6. **分支**：底部点击分支名 → 创建/切换/合并

### 版本回退

- **UI 方式**：安装 [[GitLens]] → Open in Commit Graph → Reset Current Branch to Commit
- **命令行**：`git reset <commit-id>` + `git push --force`（⚠️ 会丢失中间所有提交）

### 第一次推送配置

```bash
git config --global user.name "你的名字"
git config --global user.email "你的邮箱"
```

---

## 关键资源链接

| 资源 | URL |
|---|---|
| Vibe Coding 实战课 | https://www.bilibili.com/cheese/play/ep2410438 |
| shadcn/ui 组件库 | https://ui.shadcn.com/docs/components |
| Vercel 模板 | https://vercel.com/templates/next.js |
| GitHub SSH 配置教程 | https://www.bilibili.com/video/BV1dV411G77N |

---

## 相关页面

- [[Git 版本控制]] — 核心概念详解
- [[Vibe Coding 工具链]] — 开发工具组合
- [[学习笔记（Next.js 全栈开发篇）]] — 下一篇
