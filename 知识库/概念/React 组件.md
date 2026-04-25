---
type: concept
title: "React 组件"
complexity: intermediate
domain: web-dev
aliases:
  - "组件"
  - "Server Components"
  - "Client Components"
  - "props"
created: 2026-04-23
updated: 2026-04-23
tags:
  - concept/architecture
  - domain/react
  - domain/web-dev
status: developing
related:
  - "[[React]]"
  - "[[Next.js]]"
  - "[[shadcn/ui]]"
sources:
  - "[[学习笔记]]"
---

# React 组件

[[React]] 应用的基本构建块。可重用的独立代码片段，像乐高积木一样组合成完整界面。

---

## 组件基础

```jsx
// 定义一个按钮组件
export default function Button({ text, onClick, color = "blue" }) {
  return (
    <button onClick={onClick}
      className={`px-4 py-2 rounded text-white bg-${color}-500`}>
      {text}
    </button>
  );
}
```

**核心概念**：
- **props**：传给组件的数据（类似函数参数）
- **children**：组件标签之间的内容（允许包裹其他元素）

---

## 服务端组件 vs 客户端组件

Next.js 13 引入的关键区分：

| | 服务端组件（默认） | 客户端组件 |
|---|---|---|
| **运行位置** | 服务器 | 浏览器 |
| **声明** | 不需要特殊声明 | 文件顶部加 `'use client'` |
| **可以** | 直接访问数据库/文件系统、保持敏感信息在服务器 | 用 useState/useEffect、事件处理、浏览器 API |
| **不可以** | 用 hooks、事件处理、浏览器 API | 直接访问服务器资源 |
| **适用场景** | 数据获取、静态展示 | 表单、交互、动态更新 |

### 组合模式（最佳实践）

**服务端组件获取数据 → 传给客户端组件做交互**：

```
服务端组件 ──(data)──► 客户端组件
  ↑ fetch DB                ↑ useState / onClick
```

---

## 组件组织

```
my-project/
├── components/
│   ├── ui/            # 基础 UI 组件（Button, Input, Card）
│   ├── layout/        # 布局组件（Navbar, Footer）
│   └── features/      # 功能组件（ProductList, ContactForm）
└── app/
    └── dashboard/
        └── components/  # 仅 dashboard 使用的组件
```

**命名约定**：
- 文件用 PascalCase：`Button.jsx`、`NavBar.jsx`
- 函数名与文件名相同

---

## 常用组件库

| 库 | 特点 |
|---|---|
| [[shadcn/ui]] | 代码直接复制到项目，完全可控 |
| MUI | Google Material Design |
| Ant Design | 企业级，适合管理系统 |
| Chakra UI | 注重无障碍和简洁 |

---

## 页面间导航

使用 `Link` 组件（比 `<a>` 标签更高效）：

```jsx
import Link from 'next/link';

<Link href="/about">关于</Link>
```

优势：客户端导航（不刷新整页）、自动代码分割、预加载可见链接。

---

## 相关

- [[React]] — 组件所属库
- [[Next.js 项目结构]] — 组件在项目中的位置
- [[Next.js API Routes]] — 数据获取的后端支撑
