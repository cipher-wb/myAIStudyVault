---
type: entity
title: "Next.js"
entity_type: product
role: "基于 React 的全栈 Web 框架"
created: 2026-04-23
updated: 2026-04-23
tags:
  - product/framework
  - domain/web-dev
  - domain/react
status: developing
related:
  - "[[React]]"
  - "[[Vercel]]"
  - "[[shadcn/ui]]"
  - "[[Tailwind CSS]]"
sources:
  - "[[学习笔记（Next.js 全栈开发篇）]]"
first_mentioned: 2026-04-23
---

# Next.js

由 [[Vercel]] 开发维护的 [[React]] 全栈框架。目前最流行的 React 框架之一。

## 为什么选 Next.js

- **开箱即用**：路由、构建优化、图像处理、API 支持全部集成
- **多种渲染**：SSR（服务器渲染）/ SSG（静态生成）/ 客户端渲染
- **AI 友好**：清晰的项目结构让 AI 更容易理解和生成代码
- **全栈**：同一项目中同时开发前端和后端
- **免费部署**：[[Vercel]] Hobby 计划

## 生态

![[ingest/nextjs-ecosystem-2.png]]

| 类别 | 工具 |
|---|---|
| UI 组件 | [[shadcn/ui]]、Radix UI |
| CSS | [[Tailwind CSS]] |
| 认证 | NextAuth.js |
| 数据获取 | SWR |
| 部署 | [[Vercel]] |
| 启动模板 | Create T3 App、next-enterprise |

## 与 React 的关系

> **[[React]] 是引擎，Next.js 是一辆配备了引擎、车身、轮子和方向盘的完整汽车。**

- React 提供组件系统和状态管理
- Next.js 添加了路由、渲染优化、构建工具等
- `.jsx` = JavaScript 中写 HTML；`.tsx` = TypeScript 版本

## 核心概念

详见各概念页：

- [[Next.js 项目结构]] — App Router、文件系统路由
- [[React 组件]] — 服务端/客户端组件、props
- [[Next.js API Routes]] — Route Handlers、REST API
