---
title: "I built a tiny GitHub repo auditor, and it found my own mess"
date: 2026-11-11T13:49:37+00:00
canonical_url: https://sishodiarobin.hashnode.dev/i-built-a-tiny-github-repo-auditor-and-it-found-my-own-mess
cover_image: 
tags: []
brief: "Just shipped repo-health-report: a tiny, dependency-free Python tool that audits your GitHub repos through the REST API. It flags missing licenses…"
series: "DevOps & AWS"
serial: 45
---

> Originally published at [sishodiarobin.hashnode.dev](https://sishodiarobin.hashnode.dev/i-built-a-tiny-github-repo-auditor-and-it-found-my-own-mess). This is an automated backup; read and comment on the blog.

Just shipped **repo-health-report**: a tiny, dependency-free Python tool that audits your GitHub repos through the REST API.

It flags missing licenses, descriptions, topics and READMEs, plus pull requests that have gone stale. It also runs as a scheduled GitHub Action and writes the results to the job summary.

On my own account it found 15 repos without a license. I fixed 12 of them in an afternoon.

## What it checks

- Missing license
- Missing description or topics
- Missing README
- Open pull requests with no activity for 30+ days

## Try it

```bash
python repo_health_report.py <github-username>
```

Code and setup: <https://github.com/RobinSishodia/repo-health-report>

Feedback and issues welcome. If it's useful to you, a star helps.
