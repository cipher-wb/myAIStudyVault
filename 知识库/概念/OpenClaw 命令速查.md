---
type: concept
title: "OpenClaw 命令速查"
complexity: basic
domain: tooling
created: 2026-04-25
updated: 2026-04-25
tags:
  - concept
  - cheat-sheet
  - cli
  - openclaw
status: seed
aliases:
  - OpenClaw Cheat Sheet
  - OpenClaw 备忘单
related:
  - "[[OpenClaw]]"
sources:
  - "[[学习笔记20260424]]"
---

# OpenClaw 命令速查

> 快速参考：[[OpenClaw]] 网关管理的常用命令。
> (Source: [[学习笔记20260424]])

## 网关控制

| 操作 | 命令 |
|------|------|
| 启动 | `openclaw gateway start` |
| 关闭 | `openclaw gateway stop` |
| 重启 | `openclaw gateway restart` |
| 查看状态 | `openclaw gateway status` |
| 全局状态 | `openclaw status` |

## 日志与交互

| 操作 | 命令 |
|------|------|
| 查看日志 | `openclaw logs` |
| 实时跟踪日志 | `openclaw logs --follow` |
| 终端交互 UI | `openclaw tui` 或 `openclaw terminal` |
| Web Dashboard | 浏览器打开 `http://127.0.0.1:18789/` |

## 通道管理

| 操作 | 命令 |
|------|------|
| 查看已配置通道 | `openclaw channels list` |
| 深度状态检查 | `openclaw channels status --deep` |
| 添加 QQ Bot | `openclaw channels add --channel qqbot --token "AppID:AppSecret"` |
| 删除 QQ Bot | `openclaw channels remove --channel qqbot` |

> 添加/删除通道后需执行 `openclaw gateway restart`

## 设备授权

| 操作 | 命令 |
|------|------|
| 查看设备列表 | `openclaw devices list` |
| 批准最新请求 | `openclaw devices approve --latest` |

## 帮助

| 命令 | 说明 |
|------|------|
| `openclaw help` | 总帮助 |
| `openclaw gateway --help` | 网关子命令帮助 |
| `openclaw channels --help` | 通道子命令帮助 |

## 人话版速查

| 想干嘛 | 打什么 |
|--------|--------|
| 开机 | `openclaw gateway start` |
| 关机 | `openclaw gateway stop` |
| 重启 | `openclaw gateway restart` |
| 看活着没 | `openclaw gateway status` |
| 看全局状态 | `openclaw status` |
| 看日志 | `openclaw logs --follow` |
| 进交互界面 | `openclaw tui` |
| 开网页面板 | 浏览器 `http://127.0.0.1:18789/` |
