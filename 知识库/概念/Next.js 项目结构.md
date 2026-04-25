---
type: concept
title: "Next.js 项目结构"
complexity: intermediate
domain: web-dev
aliases:
  - "App Router"
  - "文件系统路由"
  - "Next.js 目录结构"
created: 2026-04-23
updated: 2026-04-23
tags:
  - concept/architecture
  - domain/nextjs
  - domain/web-dev
status: developing
related:
  - "[[Next.js]]"
  - "[[React 组件]]"
sources:
  - "[[学习笔记]]"
---

# Next.js 项目结构

[[Next.js]] 的核心设计理念：**文件系统路由** —— 你的目录结构直接决定 URL 路径，不需要额外配置路由。

---

## App Router（官方推荐）

从 Next.js 13 开始，`app/` 目录是官方推荐方式。

```
my-nextjs-project/
├── app/                 # 应用主目录
│   ├── favicon.ico      # 网站图标
│   ├── globals.css      # 全局样式
│   ├── layout.tsx       # 根布局（所有页面共享）
│   ├── page.tsx         # 首页（对应 /）
│   ├── about/
│   │   └── page.tsx     # 关于页（对应 /about）
│   └── blog/
│       ├── page.tsx     # 博客列表（/blog）
│       └── [slug]/
│           └── page.tsx # 动态路由（/blog/xxx）
├── components/          # 可复用组件（自建）
├── public/              # 静态资源
└── ...                  # 配置文件
```

---

## 核心文件说明

| 文件 | 用途 |
|---|---|
| `app/page.tsx` | 首页，对应 `/` |
| `app/layout.tsx` | 根布局，包含所有页面共享结构 |
| `app/globals.css` | 全局 CSS |
| `app/<目录>/page.tsx` | 子页面，对应 `/<目录>` |

---

## 特殊文件命名

| 文件名 | 用途 |
|---|---|
| `page.tsx` | 路由的主要内容 |
| `layout.tsx` | 共享 UI 布局 |
| `loading.tsx` | 加载中 UI |
| `error.tsx` | 错误 UI |
| `not-found.tsx` | 404 页面 |

---

## URL 映射规则

```
app/page.tsx              → /
app/about/page.tsx        → /about
app/blog/page.tsx         → /blog
app/blog/post/page.tsx    → /blog/post
```

### 嵌套布局

```
app/layout.tsx            → 应用于所有页面
app/blog/layout.tsx       → 应用于所有 /blog/* 页面
```

---

## 动态路由

用 `[参数名]` 创建动态路径：

```jsx
// app/blog/[slug]/page.jsx
export default function BlogPost({ params }) {
  return <h1>文章: {params.slug}</h1>
}
```

访问 `/blog/hello-world` → `params.slug` = `"hello-world"`

---

## 路由组（不影响 URL）

用括号 `()` 命名的文件夹不会出现在 URL 中，但可以共享不同布局：

```
app/(marketing)/page.jsx        → /
app/(marketing)/about/page.jsx  → /about
app/(dashboard)/dashboard/page.jsx → /dashboard
```

---

## 静态资源

`public/` 目录存放图片、字体等，直接用 URL 路径访问：

```jsx
// 普通 img 标签
<img src="/images/logo.png" alt="Logo" />

// Next.js 优化的 Image 组件（推荐）
import Image from 'next/image';
<Image src="/images/banner.jpg" alt="Banner" width={800} height={400} />
```

Image 组件优势：自动优化大小、延迟加载、防止布局偏移、支持现代格式。

---

## Pages Router（旧版，不推荐）

```
pages/
├── _app.js       # 全局 App
├── _document.js  # 自定义文档
├── index.js      # 首页
└── about.js      # 关于页
```

新项目建议用 App Router。

---

## 相关

- [[Next.js]] — 框架本身
- [[React 组件]] — 组件开发
- [[Next.js API Routes]] — 后端能力
