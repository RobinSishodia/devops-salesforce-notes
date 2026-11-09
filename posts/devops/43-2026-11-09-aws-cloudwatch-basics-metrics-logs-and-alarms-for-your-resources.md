---
title: "AWS CloudWatch Basics: Metrics, Logs and Alarms for Your Resources"
date: 2026-11-09T16:12:16+00:00
canonical_url: https://sishodiarobin.hashnode.dev/aws-cloudwatch-basics-metrics-logs-and-alarms-for-your-resources
cover_image: https://cdn.hashnode.com/uploads/covers/6693dc4e158429a5c6ab492f/daf81834-3965-479b-b034-7650726588c5.png
tags: ["AWS", "CloudWatch", "120daysofaws", "monitoring"]
brief: "Last time I looked at who changed things with CloudTrail. The next question is different: what is happening inside my resources right now? That is Amazon…"
series: "DevOps & AWS"
serial: 43
---

> Originally published at [sishodiarobin.hashnode.dev](https://sishodiarobin.hashnode.dev/aws-cloudwatch-basics-metrics-logs-and-alarms-for-your-resources). This is an automated backup; read and comment on the blog.

Last time I looked at **who** changed things with CloudTrail. The next question is different: **what is happening inside my resources right now**? That is **Amazon CloudWatch**.

## What CloudWatch does

- **Metrics:** numbers over time, such as EC2 CPU utilization or S3 request counts.
- **Logs:** log data from your applications and services, stored in log groups.
- **Alarms:** watch a metric and do something when it crosses a threshold.
- **Dashboards:** put the graphs you care about on one page.

## CloudTrail vs CloudWatch

| Question | Service |
| --- | --- |
| Who made this change? | **CloudTrail** |
| Is this resource healthy and busy? | **CloudWatch** |

## How an alarm works

- An alarm watches **one metric** over a **period** (for example, 5 minutes).
- Its state is **OK**, **ALARM** or **INSUFFICIENT\_DATA**.
- When the state changes, it can send a message to an **SNS topic**, which can email you.
- The **threshold** and the number of **periods** to evaluate decide how sensitive it is.

## Good to know

- EC2 sends basic metrics every **5 minutes** by default, and **detailed monitoring** gives 1-minute data (extra cost).
- EC2 does **not** report memory or disk usage by default. You need the **CloudWatch agent** for those.
- Logs stay forever unless you set a **retention** period, so set one.

## Hands-on: try it in your own account

1. Open **CloudWatch** and browse **All metrics** for EC2 or S3.
2. Choose **Alarms**, then **Create alarm**.
3. Pick a metric, such as **EC2 CPUUtilization** for one instance.
4. Set a threshold, for example greater than 70% for 2 periods.
5. Create or choose an **SNS topic** with your email, and confirm the subscription email.
6. Save the alarm and check that it shows **OK** or **INSUFFICIENT\_DATA** at first.

## Common mistakes

- Creating alarms with no action, so nobody is told.
- Forgetting to confirm the SNS email subscription.
- Expecting memory metrics without the CloudWatch agent.
- Leaving log groups on never-expire retention.

## Key takeaways

- CloudTrail tells you who changed it, CloudWatch tells you how it is doing.
- Metrics feed alarms, alarms feed SNS, SNS reaches you.
- Install the agent for memory and disk.
- Set log retention.

Tomorrow I'll look at how to use tags to keep resources organized and costs traceable.

*Part of #120DaysOfAWS.*
