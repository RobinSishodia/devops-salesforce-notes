---
title: "AWS IAM Identity Center: Single Sign-On Across Your AWS Accounts"
date: 2026-11-14T12:12:17+00:00
canonical_url: https://sishodiarobin.hashnode.dev/aws-iam-identity-center-single-sign-on-across-your-aws-accounts
cover_image: https://cdn.hashnode.com/uploads/covers/6693dc4e158429a5c6ab492f/0b85b72d-6a82-4b42-8837-c9cca89d8564.png
tags: ["AWS", "AWS IAM", "Cloud Computing", "Devops"]
brief: "Yesterday I set up an organization with several accounts. Now the next question: how do people get into those accounts without a pile of IAM users and…"
series: "DevOps & AWS"
serial: 47
---

> Originally published at [sishodiarobin.hashnode.dev](https://sishodiarobin.hashnode.dev/aws-iam-identity-center-single-sign-on-across-your-aws-accounts). This is an automated backup; read and comment on the blog.

Yesterday I set up an organization with several accounts. Now the next question: how do **people** get into those accounts without a pile of IAM users and long-term access keys? The answer is **AWS IAM Identity Center**.

## What it does

- It is the AWS service for **workforce single sign-on** across the accounts in your organization and supported applications.
- People sign in once at the **AWS access portal** and pick the account and role they need.
- Access is given through **temporary credentials**, so there are no long-term keys to lose.

## The building blocks

| Term | What it is | Notes |
| --- | --- | --- |
| **Identity source** | Where users and groups live | Built-in directory, Active Directory or an external identity provider |
| **Permission set** | A template of permissions | Identity Center creates a role from it in each assigned account |
| **Assignment** | Links a user or group to an account with a permission set | Assign groups, not single users |
| **Access portal** | The sign-in page for your users | One URL for all accounts |

## How it fits with Organizations

- Enable it in the **management account** with AWS Organizations turned on.
- Choose the **home Region** carefully, because it is hard to change later.
- Roles created from permission sets show up in each account with names starting `AWSReservedSSO_`.
- Session length is set per permission set.

## Hands-on: try it in your own account

1. Open **IAM Identity Center** in the management account and choose **Enable**.
2. Under **Groups**, create a group named `ReadOnly`, then create a user and add them to it.
3. Under **Permission sets**, create one that uses the AWS managed **ViewOnlyAccess** or **ReadOnlyAccess** policy.
4. Under **AWS accounts**, select an account, choose **Assign users or groups**, and pick the group and the permission set.
5. Open the **access portal URL**, sign in as the user, and choose the account and role.
6. Optional: run `aws configure sso`, then `aws sso login`, and check with `aws sts get-caller-identity`.

## Common mistakes

- Creating IAM users for every person instead of using Identity Center.
- Assigning permission sets to single users, which gets hard to manage.
- Giving broad access when a read-only permission set is enough.
- Forgetting MFA for the people who sign in.

## Key takeaways

- Use Identity Center for people and IAM roles for workloads.
- Define access once in a permission set and assign it to groups.
- Prefer temporary credentials over long-term keys.
- Keep MFA on for every user.

Tomorrow I'll look at what happens when something goes wrong in your accounts, starting with how to be notified.

*Part of #120DaysOfAWS.*
