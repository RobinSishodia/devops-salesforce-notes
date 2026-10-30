---
title: "Day 1/120 – #120DaysOfAWS: IAM, the Front Door to Everything in AWS"
date: 2026-10-29T14:04:45+00:00
canonical_url: https://sishodiarobin.hashnode.dev/day-1-120-120daysofaws-iam-the-front-door-to-everything-in-aws
cover_image: https://cdn.hashnode.com/uploads/covers/6693dc4e158429a5c6ab492f/1406349a-d476-4396-9f2a-03b7f242fe27.png
tags: ["AWS", "IAM", "cloudsecurity", "120daysofaws", "Devops"]
brief: "Every AWS action, from launching an EC2 instance to reading an S3 object, goes through one question: is this identity allowed to do this? IAM (Identity and…"
---

> Originally published at [sishodiarobin.hashnode.dev](https://sishodiarobin.hashnode.dev/day-1-120-120daysofaws-iam-the-front-door-to-everything-in-aws). This is an automated backup; read and comment on the blog.

Every AWS action, from launching an EC2 instance to reading an S3 object, goes through one question: *is this identity allowed to do this?* IAM (Identity and Access Management) answers it, so I'm starting here.

## The 5 building blocks

- **Users:** a person or app with long-term credentials.
- **Groups:** a collection of users that share permissions. Attach policies to groups, not to individual people.
- **Roles:** temporary credentials that anyone or anything can assume. This is how EC2, Lambda and cross-account access should work.
- **Policies:** JSON documents that say who can do what on which resource.
- **MFA:** a second factor that protects the account if a password leaks.

## How a policy reads

```json
{
  "Effect": "Allow",
  "Action": "s3:GetObject",
  "Resource": "arn:aws:s3:::my-bucket/*"
}
```

Effect, Action and Resource are the three parts to check first. An explicit Deny always beats an Allow, and anything not allowed is denied by default.

## What I did hands-on today

![](https://cdn.hashnode.com/uploads/covers/6693dc4e158429a5c6ab492f/19494e48-794b-43f4-abbd-eb5fe9e91660.png)

- Checked my IAM dashboard: MFA is on for my root user and my IAM user, and I have no stale access keys.
- Created a user group called `ReadOnlyTeam` and attached the AWS-managed `ReadOnlyAccess` policy.
- Used the **Policy Simulator** to test two S3 actions against that group:
  - `s3:GetObject` was **Allowed** (explicit allow).
  - `s3:DeleteObject` was **Denied** (implicit deny: no policy allows it, so it's blocked by default).
- Ran the same test against my own user, which has `AdministratorAccess`, and both actions were Allowed. The same action gets a different answer depending on which policies are attached, which is why least privilege matters.

![](https://cdn.hashnode.com/uploads/covers/6693dc4e158429a5c6ab492f/9a6021eb-28d2-443c-9422-8c18fc88bd40.png)

## 3 habits I'm keeping

1. Never use the root user for daily work.
2. Grant least privilege: start with nothing and add only what's needed.
3. Prefer roles over long-lived access keys.

Tomorrow (Day 2): writing a custom IAM policy from scratch.
