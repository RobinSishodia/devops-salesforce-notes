---
title: "AWS Budgets and Billing Alerts: Set a Spending Limit Before You Build"
date: 2026-11-07T17:18:55+00:00
canonical_url: https://sishodiarobin.hashnode.dev/aws-budgets-and-billing-alerts-set-a-spending-limit-before-you-build
cover_image: https://cdn.hashnode.com/uploads/covers/6693dc4e158429a5c6ab492f/e57520eb-ece5-4ada-9cef-6db17a101324.png
tags: ["AWS", "cloudcost", "120daysofaws", "cloudsecurity", "Devops"]
brief: "Yesterday I locked down the root account and noted \"keep billing alerts up to date\". Today is the other half of the front door: making sure a forgotten…"
series: "DevOps & AWS"
serial: 41
---

> Originally published at [sishodiarobin.hashnode.dev](https://sishodiarobin.hashnode.dev/aws-budgets-and-billing-alerts-set-a-spending-limit-before-you-build). This is an automated backup; read and comment on the blog.

Yesterday I locked down the root account and noted "keep billing alerts up to date". Today is the other half of the front door: making sure a forgotten resource never turns into a surprise bill. **AWS Budgets** does that.

## What AWS Budgets does

- You set a **spending limit** (or a usage limit) and AWS compares your actual and forecasted spend against it.
- When a threshold is crossed, it **emails you** (and can notify an SNS topic).
- Spend data is not instant. Billing data can lag, so treat alerts as an early warning, not a live meter.

## Types of budget

| Type | Tracks | Good for |
| --- | --- | --- |
| **Cost budget** | Dollars spent | Almost every learner |
| **Usage budget** | Units used, such as hours or GB | Watching a specific service |
| **Savings Plans / Reservation budgets** | Coverage and utilization | Later, when you commit to spend |

## Two templates to start with

- **Zero spend budget:** alerts you as soon as your spend goes above the free tier. Ideal for a learning account.
- **Monthly cost budget:** you choose a monthly amount, and the console sets alerts at **85% of actual spend**, **100% of actual spend** and **100% of forecasted spend**.

## Hands-on: try it in your own account

1. Sign in and open **Billing and Cost Management**, then **Budgets**.
2. Choose **Create budget** and pick a **template**, such as **Zero spend budget** or **Monthly cost budget**.
3. Name it, set the amount (for example 10 USD) and add the **email addresses** to alert.
4. Review the thresholds and create the budget.
5. Optionally, as the root user, turn on **IAM user and role access to Billing information** so your admin identity can see costs without using root.

## Common mistakes

- Creating a budget but typing the email address wrongly.
- Setting only an actual-spend alert, so you hear about a problem after the money is gone.
- Forgetting that some services keep charging until you delete the resource.
- Using root every time to check the bill instead of enabling billing access for IAM.

## Worth knowing next

**Cost Explorer** shows where your spend comes from, and **Cost Anomaly Detection** can flag unusual spikes. Budgets tells you *that* spend is rising. Those two help explain *why*.

## Key takeaways

- Create a budget before you create any real resources.
- Alert on **forecasted** spend as well as actual spend.
- Give billing access to an IAM admin, not just root.
- Delete what you stop using.

Tomorrow I'll go one step further into securing access to the account.

*Part of #120DaysOfAWS.*
