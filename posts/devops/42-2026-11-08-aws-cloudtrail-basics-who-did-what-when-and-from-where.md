---
title: "AWS CloudTrail Basics: Who Did What, When and From Where"
date: 2026-11-08T17:51:43+00:00
canonical_url: https://sishodiarobin.hashnode.dev/aws-cloudtrail-basics-who-did-what-when-and-from-where
cover_image: https://cdn.hashnode.com/uploads/covers/6693dc4e158429a5c6ab492f/c3b0a5a9-5204-4c65-854d-bd46e48e5e69.png
tags: ["AWS", "cloudtrail", "120daysofaws", "cloudsecurity", "Devops"]
brief: "This week I locked the root account and set a budget. Now the question that comes after both: when something changes in the account, how do I find out who…"
series: "DevOps & AWS"
serial: 42
---

> Originally published at [sishodiarobin.hashnode.dev](https://sishodiarobin.hashnode.dev/aws-cloudtrail-basics-who-did-what-when-and-from-where). This is an automated backup; read and comment on the blog.

This week I locked the root account and set a budget. Now the question that comes after both: when something changes in the account, how do I find out **who did it, what they did and when**? That is **AWS CloudTrail**.

## What CloudTrail records

- CloudTrail logs **API activity** in your account, whether it came from the console, the CLI, an SDK or another AWS service.
- Each event says **who** (the identity), **what** (the API call), **when**, and **where from** (the source IP address).
- It is the audit trail you open when a resource disappears or a setting changes.

## Event types

| Type | What it covers | Notes |
| --- | --- | --- |
| **Management events** | Control-plane actions, such as creating a role or launching an instance | Recorded by default |
| **Data events** | Object-level actions, such as S3 object reads or Lambda invokes | Off by default, extra cost |
| **Insights events** | Unusual API activity | Optional |

## Event history vs a trail

- **Event history** is on by default and lets you look up recent management events (the last 90 days) in the console, with no setup.
- A **trail** delivers events to an **S3 bucket** (and optionally CloudWatch Logs) so you keep them longer and can search them with other tools.
- A **multi-Region trail** records activity in all Regions, so nothing slips through in a Region you do not use.

## Hands-on: try it in your own account

1. Open **CloudTrail** and choose **Event history**.
2. Filter by **Event name** `ConsoleLogin` and open one event to see who signed in and from which IP address.
3. Filter by **User name** `root` to check whether root has been used, tying back to the root account checklist.
4. Choose **Create trail**, name it, and create or choose an **S3 bucket** for the logs.
5. Enable a **multi-Region trail** and **log file validation**, then create it.
6. After a few minutes, open the S3 bucket and find the delivered log files.

## Common mistakes

- Relying on event history only, then needing events older than 90 days.
- Creating a trail in one Region and missing activity elsewhere.
- Leaving the log bucket open. Keep it private.
- Turning on data events everywhere without checking the cost.

## Key takeaways

- CloudTrail answers who, what, when and from where.
- Event history is free to browse, a trail keeps the records.
- Use a multi-Region trail and keep the bucket private.
- Check root activity regularly.

Tomorrow I'll look at how to see what is happening inside your resources, not just who changed them.

*Part of #120DaysOfAWS.*
