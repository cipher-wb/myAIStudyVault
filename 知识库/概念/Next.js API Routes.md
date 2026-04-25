---
type: concept
title: "Next.js API Routes"
complexity: intermediate
domain: web-dev
aliases:
  - "Route Handlers"
  - "API 路由"
  - "Next.js 后端"
created: 2026-04-23
updated: 2026-04-23
tags:
  - concept/architecture
  - domain/nextjs
  - domain/api
status: developing
related:
  - "[[Next.js]]"
  - "[[Next.js 项目结构]]"
sources:
  - "[[学习笔记]]"
---

# Next.js API Routes

[[Next.js]] 的后端能力。在同一个项目中构建前端界面和后端 API，无需单独的后端服务。

---

## 目录结构

```
app/
└── api/
    ├── hello/
    │   └── route.js       # GET /api/hello
    ├── users/
    │   └── route.js       # GET, POST /api/users
    ├── products/
    │   ├── route.js       # GET, POST /api/products
    │   └── [id]/
    │       └── route.js   # GET, PUT, DELETE /api/products/1
    ├── search/
    │   └── route.js       # GET /api/search?q=xxx
    └── upload/
        └── route.js       # POST /api/upload
```

---

## 基本 API

```js
// app/api/hello/route.js
export async function GET() {
  return Response.json({ message: '你好，世界！' });
}
```

---

## CRUD 示例

```js
// app/api/users/route.js
export async function GET() {
  const users = await db.users.findMany();
  return Response.json(users);
}

export async function POST(request) {
  const data = await request.json();
  if (!data.name || !data.email) {
    return Response.json({ error: '必填' }, { status: 400 });
  }
  const user = await db.users.create({ data });
  return Response.json(user, { status: 201 });
}
```

---

## 动态路由

```js
// app/api/users/[id]/route.js
export async function GET(request, { params }) {
  const user = await db.users.findUnique({ where: { id: params.id } });
  if (!user) return Response.json({ error: '不存在' }, { status: 404 });
  return Response.json(user);
}

export async function DELETE(request, { params }) {
  await db.users.delete({ where: { id: params.id } });
  return new Response(null, { status: 204 });
}
```

---

## 请求参数处理

```js
// URL 查询参数
const { searchParams } = new URL(request.url);
const query = searchParams.get('q');
const limit = parseInt(searchParams.get('limit') || '10');
```

---

## 文件上传

```js
// app/api/upload/route.js
import { writeFile } from 'fs/promises';

export async function POST(request) {
  const formData = await request.formData();
  const file = formData.get('file');
  const bytes = await file.arrayBuffer();
  const buffer = Buffer.from(bytes);
  const fileName = `${Date.now()}-${file.name}`;
  await writeFile(join(process.cwd(), 'public/uploads', fileName), buffer);
  return Response.json({ url: `/uploads/${fileName}` });
}
```

---

## 第三方 API 集成

```js
// app/api/weather/route.js
export async function GET(request) {
  const { searchParams } = new URL(request.url);
  const city = searchParams.get('city');
  const res = await fetch(
    `https://api.weatherapi.com/v1/current.json?key=${process.env.WEATHER_API_KEY}&q=${city}`
  );
  const data = await res.json();
  return Response.json({
    city: data.location.name,
    temperature: data.current.temp_c,
  });
}
```

---

## 数据获取方式

| 方式 | 场景 |
|---|---|
| **服务端组件中直接 fetch** | 不需要交互的页面 |
| **SWR**（客户端） | 需要缓存、自动刷新的交互组件 |
| **Route Handlers** | REST API 端点 |

服务端组件可以直接 `async/await`：
```jsx
export default async function UsersPage() {
  const users = await fetch('/api/users').then(r => r.json());
  return <UserList users={users} />;
}
```

---

## 相关

- [[Next.js]] — 框架本身
- [[Next.js 项目结构]] — API 目录在项目中的位置
- [[Vercel]] — 部署时自动处理 API Routes
