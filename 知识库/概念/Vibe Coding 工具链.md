---
type: concept
title: "Vibe Coding 工具链"
complexity: basic
domain: web-dev
aliases:
  - "AI 编程工具组合"
  - "Cursor 替代方案"
created: 2026-04-23
updated: 2026-04-23
tags:
  - concept/toolchain
  - domain/web-dev
  - domain/ai-coding
status: developing
related:
  - "[[VS Code]]"
  - "[[shadcn/ui]]"
  - "[[Vercel]]"
  - "[[学习笔记]]"
---

# Vibe Coding 工具链

用 AI 辅助编程（"Vibe Coding"）所需的工具组合。基于【熠辉】Vibe Coding 实战课的推荐。

---

## 核心编辑器 + AI

| 组合 | 说明 |
|---|---|---|
| **Cursor** | 课程教学使用的 AI IDE，内置 AI 对话 |
| **[[VS Code]] + Claude Code 插件** | 课程确认"二者差不多"，可完全替代 Cursor |

## 必装 VS Code 插件

| 插件 | 用途 |
|---|---|
| **Claude Code for VS Code** | AI 编程助手 |
| **Live Server** | 本地直接打开 HTML 文件预览 |
| **Chinese Language Pack** | VS Code 中文化 |
| **[[GitLens]]** | Git 可视化（版本回退必需） |

## UI 组件参考

**[[shadcn/ui]]**（https://ui.shadcn.com/docs/components）

- 可查看所有 UI 组件的**动态效果**
- 用途：当你想让 AI 开发某种动态效果，但不知道怎么描述时，先去这里找参考
- 不是传统组件库，而是可以直接复制到项目中的代码

## 网页设计模板

**Vercel 模板**（https://vercel.com/templates/next.js）

- 各种不同功能的已做好的网站模板
- 不需要自己从零设计

## Obsidian 相关

| 插件 | 用途 |
|---|---|
| **Obsidian Web Clipper** | Chrome 剪藏网页到 vault |
| **Local Images Plus** | 配合 Web Clipper，把外链图片下载到本地 |

---

## 前端框架选型

课程选择 **Next.js**（React 框架）：

- **开箱即用**：路由、构建优化、图像处理都集成
- **多种渲染**：SSR / SSG / 客户端渲染
- **AI 友好**：清晰的项目结构让 AI 更容易理解项目并生成合适代码
- **生态强大**：shadcn/ui、Tailwind CSS、SWR 等开箱可用

部署平台选择 **[[Vercel]]**（免费 Hobby 计划）。

---

## 相关

- [[学习笔记]] — 来源笔记
- [[学习笔记]] — Next.js 详解
- [[Git 版本控制]] — 版本管理基础
