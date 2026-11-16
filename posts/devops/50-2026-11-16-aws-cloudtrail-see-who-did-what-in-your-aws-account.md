---
title: "AWS CloudTrail: See Who Did What in Your AWS Account"
date: 2026-11-16T14:14:40+00:00
canonical_url: https://sishodiarobin.hashnode.dev/aws-cloudtrail-see-who-did-what-in-your-aws-account
cover_image: https://cdn.hashnode.com/uploads/covers/6693dc4e158429a5c6ab492f/0c66f0ed-3ff5-4935-b281-5905b8f1f828.png
tags: ["AWS", "AWS CloudTrail", "Cloud Computing", "Devops"]
brief: "Last time I set up an alarm to be told when something goes wrong. The next question is different: who did what in my account? When a setting changes or a…"
series: "DevOps & AWS"
serial: 50
---

> Originally published at [sishodiarobin.hashnode.dev](https://sishodiarobin.hashnode.dev/aws-cloudtrail-see-who-did-what-in-your-aws-account). This is an automated backup; read and comment on the blog.

Last time I set up an alarm to be told when something goes wrong. The next question is different: **who did what in my account?** When a setting changes or a resource disappears, the answer comes from **AWS CloudTrail**.

## What CloudTrail does

- It records **API activity** in your account: who made the call, what they did, when, and from where.
- That includes actions in the console, the CLI, SDKs and other AWS services.
- It is the first place to look after a surprise change or a security question.

## The building blocks

| Term | What it is | Notes |
| --- | --- | --- |
| **Event** | One recorded API call | Shows user, action, time, source IP |
| **Event history** | A searchable view of recent events | Management events, last 90 days, per Region |
| **Trail** | A setting that delivers events to an S3 bucket | Keeps history longer than 90 days |
| **Management events** | Actions on resources | Examples: CreateTopic, RunInstances, DeleteBucket |
| **Data events** | Actions on the data inside resources | Examples: S3 object reads, Lambda invokes. Off by default |

## Event history or a trail?

- **Event history** is on by default, needs no setup and covers the last 90 days of management events.
- A **trail** stores events in S3 so you can keep them, search them later and share them across the organization.
- A trail can apply to **all Regions**, so activity in a Region you never use still gets recorded.

## Hands-on: find who did something

1. Open **CloudTrail**, then **Event history**.
2. Filter by **Event name** and search for `CreateTopic`. That is the SNS topic from my last post.
3. Open the event and read the **user name**, **event time** and **source IP address**.
4. Create a trail: choose **Create trail**, name it `management-events`, let it create a new S3 bucket, and keep **Management events** selected.
5. Turn on **Apply trail to all Regions**.
6. Check it from the CLI: `aws cloudtrail lookup-events --lookup-attributes AttributeKey=EventName,AttributeValue=CreateTopic --max-results 5`

## Common mistakes

- Treating Event history as permanent when it only keeps 90 days.
- Creating a trail for one Region only.
- Turning on data events everywhere without thinking about cost.
- Leaving the log bucket open to more people than needed.

## Key takeaways

- CloudTrail answers who did what, when and from where.
- Event history is free and quick, a trail keeps the history.
- Use a trail that covers all Regions.
- Protect the bucket that holds the logs.

Tomorrow I'll look at AWS Config, which tracks how your resources looked over time.

*Part of #120DaysOfAWS.*
