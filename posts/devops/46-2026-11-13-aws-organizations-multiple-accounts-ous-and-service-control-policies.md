---
title: "AWS Organizations: Multiple Accounts, OUs and Service Control Policies"
date: 2026-11-13T14:37:10+00:00
canonical_url: https://sishodiarobin.hashnode.dev/aws-organizations-multiple-accounts-ous-and-service-control-policies
cover_image: https://cdn.hashnode.com/uploads/covers/6693dc4e158429a5c6ab492f/85b59680-73ea-4bdd-911d-e3a934c22353.png
tags: ["AWS", "AWS Organizations", "Cloud Computing", "Devops"]
brief: "So far I have secured root, set a budget, turned on CloudTrail and CloudWatch, and added tags. All of that sits in one account. The next step is the…"
series: "DevOps & AWS"
serial: 46
---

> Originally published at [sishodiarobin.hashnode.dev](https://sishodiarobin.hashnode.dev/aws-organizations-multiple-accounts-ous-and-service-control-policies). This is an automated backup; read and comment on the blog.

So far I have secured root, set a budget, turned on CloudTrail and CloudWatch, and added tags. All of that sits in one account. The next step is the structure around it: **AWS Organizations**.

## Why more than one account

- An AWS account is a strong boundary for **security, cost and blast radius**.
- A mistake in a sandbox account cannot touch production.
- Each account has its own root user, IAM and limits, so teams can work separately.

## The building blocks

| Term | What it is | Notes |
| --- | --- | --- |
| **Organization** | The group of accounts you manage together | Created from one account |
| **Management account** | The account that creates the organization and pays the bill | SCPs do not apply to it |
| **Member accounts** | Every other account in the organization | One per workload or team |
| **OU** | An organizational unit that groups accounts | Policies on an OU apply to its accounts |
| **SCP** | A service control policy | Sets the maximum permissions, never grants them |

## Consolidated billing

- All member accounts roll up to **one bill** on the management account.
- Usage across accounts can count together for **volume discounts**.
- Tags still let you split cost by project or owner.

## How SCPs behave

- An SCP is a **guardrail**: an action must be allowed by the SCP **and** by the identity's own IAM policy.
- They apply to IAM users and roles in member accounts, including the account root user.
- They do not apply to the **management account**, so keep workloads out of it.
- Use **all features** mode to turn SCPs on.

## A simple starting structure

- **Security** OU: logging and audit accounts
- **Workloads** OU: production and non-production accounts
- **Sandbox** OU: learning and experiments, with tighter SCPs

## Hands-on: try it in your own account

1. Open **AWS Organizations** and choose **Create an organization**.
2. Check that **MFA is on for the management account root user**.
3. Create an OU named **Sandbox**.
4. Choose **Add an AWS account**, then **Create an AWS account**, and give it a unique email address and a name. Move it into the Sandbox OU.
5. Open **Policies**, enable service control policies, and attach a deny policy to the Sandbox OU, for example one that stops the account leaving the organization.
6. Sign in to the management account and **assume the OrganizationAccountAccessRole** in the new account to check it works.

## Common mistakes

- Running workloads in the management account.
- Using SCPs as if they grant permissions. They only limit.
- Reusing one email address for several accounts. Each account needs a unique one.
- Attaching SCPs to the organization root before testing on a Sandbox OU.

## Key takeaways

- Use separate accounts as security and cost boundaries.
- Group accounts into OUs and attach policy once.
- SCPs set the maximum, IAM still grants.
- Keep the management account for administration only.

Tomorrow I'll look at how people and tools sign in across these accounts.

*Part of #120DaysOfAWS.*
