---
type: meta
title: "Dashboard"
updated: 2026-04-23
tags:
  - meta
  - dashboard
status: evergreen
---

# Wiki Dashboard

## Recent Activity
```dataview
TABLE type, status, updated FROM "知识库" SORT updated DESC LIMIT 15
```

## Seed Pages (Need Development)
```dataview
LIST FROM "知识库" WHERE status = "seed" SORT updated ASC
```

## Entities Missing Sources
```dataview
LIST FROM "知识库/实体" WHERE !sources OR length(sources) = 0
```

## Recent Log Entries
```dataview
LIST FROM "知识库" WHERE type = "meta" AND contains(tags, "log") SORT updated DESC LIMIT 5
```
