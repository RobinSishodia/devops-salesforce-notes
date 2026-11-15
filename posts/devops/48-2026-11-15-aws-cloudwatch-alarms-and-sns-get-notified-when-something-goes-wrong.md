---
title: "AWS CloudWatch Alarms and SNS: Get Notified When Something Goes Wrong"
date: 2026-11-15T16:32:58+00:00
canonical_url: https://sishodiarobin.hashnode.dev/aws-cloudwatch-alarms-and-sns-get-notified-when-something-goes-wrong
cover_image: https://cdn.hashnode.com/uploads/covers/6693dc4e158429a5c6ab492f/4465a3bf-e20f-476d-aae3-452e04c3f0ab.png
tags: ["AWS", "Amazon Cloudwatch", "Cloud Computing", "Devops"]
brief: "In the last two posts I set up several accounts and a way for people to sign in. Now the question every real environment hits: when something goes wrong…"
series: "DevOps & AWS"
serial: 48
---

> Originally published at [sishodiarobin.hashnode.dev](https://sishodiarobin.hashnode.dev/aws-cloudwatch-alarms-and-sns-get-notified-when-something-goes-wrong). This is an automated backup; read and comment on the blog.

In the last two posts I set up several accounts and a way for people to sign in. Now the question every real environment hits: when something goes wrong, **who finds out, and how fast?** The basic answer on AWS is a **CloudWatch alarm** that sends a message through **Amazon SNS**.

## What each service does

- **Amazon CloudWatch** collects metrics, such as CPU use or estimated charges, and can watch them with alarms.
- **CloudWatch alarm** compares a metric to a threshold and moves between three states: **OK**, **ALARM** and **INSUFFICIENT\_DATA**.
- **Amazon SNS** (Simple Notification Service) sends a message to everyone subscribed to a **topic**, by email, SMS or other targets.

## The building blocks

| Term | What it is | Notes |
| --- | --- | --- |
| **Metric** | A number measured over time | Example: CPUUtilization or EstimatedCharges |
| **Alarm** | A rule on one metric | Threshold, period and number of periods |
| **SNS topic** | A channel for messages | Alarms publish to it |
| **Subscription** | Who receives the topic | An email subscription must be confirmed |
| **Alarm action** | What the alarm does on a state change | Often: publish to an SNS topic |

## Why a topic and not a direct email

- One topic can notify a whole team, and you can add people without touching the alarm.
- The same topic can be reused by many alarms.
- Later you can add other targets, such as a chat tool or a Lambda function.

## Hands-on: a billing alert in your own account

1. Sign in with a user that can open the Billing console, and turn on **Receive CloudWatch billing alerts** in Billing preferences.
2. Switch the Region to **US East (N. Virginia)**, because billing metrics are only published there.
3. Open **SNS**, create a **Standard** topic named `billing-alerts`, and add an **Email** subscription with your address.
4. Open the email and choose **Confirm subscription**. Until you do, nothing is delivered.
5. Open **CloudWatch**, then **Alarms**, then **Create alarm**. Select the metric **Billing > Total Estimated Charge** and set a threshold such as 5 USD.
6. For the alarm action choose **In alarm**, send to the `billing-alerts` topic, and create the alarm.
7. Test the notification path with the CLI: `aws cloudwatch set-alarm-state --alarm-name <your-alarm> --state-value ALARM --state-reason "test"` and check that the email arrives.

## Common mistakes

- Forgetting to confirm the email subscription.
- Creating the billing alarm in a Region other than US East (N. Virginia).
- Setting the threshold so high that the alarm never fires.
- Sending alerts to one personal inbox that nobody else watches.

## Key takeaways

- An alarm watches a metric, SNS delivers the message.
- Use a topic so you can add people and targets later.
- Confirm subscriptions and test the path on purpose.
- Start with a billing alarm in every new account.

Tomorrow I'll look at how to see who did what in your account, with AWS CloudTrail.

*Part of #120DaysOfAWS.*
