---
type: concept
title: "Git 版本控制"
complexity: basic
domain: software-engineering
aliases:
  - "Git"
  - "版本管理"
  - "Version Control"
  - "VCS"
created: 2026-04-23
updated: 2026-04-23
tags:
  - concept/tool
  - domain/git
  - domain/software-engineering
status: developing
related:
  - "[[GitHub]]"
  - "[[GitLens]]"
  - "[[VS Code]]"
  - "[[学习笔记]]"
---

# Git 版本控制

分布式版本控制系统。追踪文件变化历史，管理代码版本。**AI 编程时代的后悔药** —— 让你在 AI 改坏代码后随时回退。

![[ingest/git-concept.png]]

---

## 四个核心区域

```
┌───────────┐  git add     ┌──────────┐  git commit  ┌──────────┐  git push  ┌──────────┐
│ 工作区    │ ───────────► │ 暂存区   │ ───────────► │ 本地仓库 │ ─────────► │ 远程仓库 │
│ (你编辑的 │              │ (Staging │              │ (.git    │            │ (GitHub) │
│  文件)    │ ◄─────────── │  Area)   │ ◄─────────── │  目录)   │ ◄───────── │          │
└───────────┘  git restore └──────────┘   git reset  └──────────┘  git pull  └──────────┘
```

---

## 日常命令速查

### 基础流程

| 命令 | 作用 |
|---|---|
| `git init` | 把当前文件夹变成 git 仓库 |
| `git clone <url>` | 下载远程仓库到本地 |
| `git status` | 查看哪些文件被改/暂存/未跟踪 |
| `git add .` | 把所有改动放进暂存区 |
| `git add <文件>` | 把指定文件放进暂存区 |
| `git commit -m "说明"` | 封存暂存区为一个快照 |
| `git log` / `git log --oneline` | 查看历史快照列表 |

### 远程协作

| 命令 | 作用 |
|---|---|
| `git remote add origin <url>` | 绑定远程仓库 |
| `git push origin main` | 推送到远程 |
| `git pull` | 拉取远程更新并合并 |
| `git push --force` | 强制推送覆盖远程（⚠️ 危险） |

### 分支管理

| 命令 | 作用 |
|---|---|
| `git branch` | 查看分支列表 |
| `git branch <name>` | 创建新分支 |
| `git switch <name>` | 切换分支（推荐） |
| `git switch -c <name>` | 创建并切换 |
| `git checkout <name>` | 切换分支（旧语法，仍可用） |
| `git checkout -b <name>` | 创建并切换（旧语法） |
| `git merge <branch>` | 合并分支到当前分支 |
| `git branch -d <name>` | 删除分支 |

### 回退与撤销

| 命令 | 作用 |
|---|---|
| `git restore <文件>` | 丢弃工作区的改动 |
| `git restore --staged <文件>` | 撤出暂存区 |
| `git reset <commit-id>` | 回退到某个历史版本 |
| `git commit --amend -m "新说明"` | 修改最近一次提交信息 |

---

## 为什么要用分支？

> 想象：项目上线了，正在开发新功能到一半，线上出现紧急 bug。
> 如果在当前分支修 bug → 新功能还没做完的代码也被推上线了。
> **解决方案**：在独立分支上开发新功能，bug 在主分支上修，互不干扰。

---

## 首次配置

```bash
git config --global user.name "你的名字"
git config --global user.email "你的邮箱"
```

GitHub SSH 密钥配置教程：https://www.bilibili.com/video/BV1dV411G77N

---

## Cursor / VS Code 中的 Git UI 操作

在 Cursor 或 VS Code（装了 [[GitLens]] 插件）中可以完全用 UI 操作 Git：

1. 左侧【更改】面板 → 查看修改
2. 文件旁 + 号 → 添加到暂存区
3. 输入框写提交信息 → 提交
4. 底部分支名 → 创建/切换分支
5. GitLens → Commit Graph → 版本回退

---

## 实用建议

- **经常提交**，提交信息要有意义
- **使用分支**开发新功能
- **合并前先 pull** 最新代码
- `git push --force` 是危险操作，会丢失中间所有提交
- `git status` 随时检查工作状态

---

## 相关

- [[GitHub]] — 基于 Git 的云端托管平台
- [[GitLens]] — VS Code Git 可视化增强插件
- [[学习笔记]] — 来源笔记
