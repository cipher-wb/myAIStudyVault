---
type: source
title: "学习笔记（Next.js 全栈开发篇）"
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
  - domain/nextjs
  - domain/react
status: developing
related:
  - "[[Next.js]]"
  - "[[React]]"
  - "[[Next.js 项目结构]]"
  - "[[React 组件]]"
  - "[[Next.js API Routes]]"
  - "[[Vercel]]"
sources:
  - "[[.源文档/文字稿/学习笔记.md]]"
key_claims:
  - "Next.js 是建立在 React 基础上的全栈框架，提供路由、渲染优化、构建工具等"
  - "App Router（app/ 目录）是官方推荐的路由方式，文件结构直接决定 URL 路径"
  - "组件分为服务端组件（默认）和客户端组件（需 'use client'），各自适用不同场景"
  - "Next.js 可在同一项目中构建前端和后端，API Routes 即后端服务"
  - "新手可通过 Vercel 免费部署，无需购买服务器"
---

# 学习笔记（Next.js 全栈开发篇）

> **来源**：【熠辉】面向新手的 Vibe Coding 实战课
> **前置篇**：[[学习笔记（Git 与工具篇）]]

## TL;DR

Next.js 全栈开发的完整学习路径：框架选型 → 项目结构 → 路由系统 → 组件开发 → API Routes → 部署。

---

## 框架选型

![[ingest/nextjs-why.png]]

### 什么是框架？

框架 = 预先设计好的建筑蓝图和工具箱。优势：
- 提高开发效率（常见功能已实现）
- 遵循最佳实践
- 标准化结构
- **框架说明书是 AI 编程极好的上下文**，所以现在开发项目一定要使用框架

### 为什么选 Next.js？

![[ingest/nextjs-ecosystem.png]]

- 开箱即用（路由、构建优化、图像处理）
- 多种渲染（SSR / SSG / 客户端渲染）
- AI 友好（清晰结构让 AI 更容易理解和生成代码）
- 生态强大（[[shadcn/ui]]、Tailwind CSS、SWR 等）

### React vs Next.js

![[ingest/react-diagram.png]]

- **[[React]]** = 引擎（组件系统 + 状态管理）
- **[[Next.js]]** = 完整汽车（引擎 + 车身 + 轮子 + 方向盘）
- `.jsx` = 在 JavaScript 中写类似 HTML 的代码；`.tsx` = TypeScript 版本

---

## 核心知识地图

| 主题 | 详见 |
|---|---|
| 项目结构与路由 | [[Next.js 项目结构]] |
| 组件与 UI | [[React 组件]] |
| API Routes（后端） | [[Next.js API Routes]] |
| 部署 | [[Vercel]] |

---

## 快速开始

```bash
# 安装
npx create-next-app@latest

# 运行
npm run dev
# → http://localhost:3000
```

前置条件：安装 [Node.js](https://nodejs.org/zh-cn/)

---

## 相关页面

- [[Next.js]] — 框架实体页
- [[React]] — UI 库实体页
- [[学习笔记（Git 与工具篇）]] — 前置篇
