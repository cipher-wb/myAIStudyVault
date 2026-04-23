---
type: entity
title: "React"
entity_type: product
role: "用于构建用户界面的 JavaScript 库"
created: 2026-04-23
updated: 2026-04-23
tags:
  - product/library
  - domain/web-dev
  - domain/frontend
status: seed
related:
  - "[[Next.js]]"
  - "[[React 组件]]"
sources:
  - "[[学习笔记（Next.js 全栈开发篇）]]"
first_mentioned: 2026-04-23
---

# React

![[ingest/react-diagram.png]]

用于构建用户界面的 JavaScript 库。核心理念：将界面拆分为可重用的组件。

## 要点

- **组件化**：每个组件管理自己的状态和渲染逻辑
- **声明式**：描述界面应该长什么样，而非如何操作 DOM
- 只关注 UI 层面 —— 路由、状态管理等需要额外工具

## 与 Next.js 的关系

React 是引擎，[[Next.js]] 是完整汽车。Next.js 建立在 React 之上，扩展了路由、渲染优化、构建工具等。

## 文件格式

- `.jsx` = JavaScript XML（在 JS 中写类 HTML）
- `.tsx` = TypeScript 版 JSX（增加类型检查）

详见 [[React 组件]]。
