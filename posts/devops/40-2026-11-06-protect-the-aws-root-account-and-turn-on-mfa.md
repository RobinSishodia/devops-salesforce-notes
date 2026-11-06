---
title: "Protect the AWS Root Account and Turn on MFA"
date: 2026-11-06T16:12:08+00:00
canonical_url: https://sishodiarobin.hashnode.dev/protect-the-aws-root-account-and-turn-on-mfa
cover_image: https://cdn.hashnode.com/uploads/covers/6693dc4e158429a5c6ab492f/332adbcb-b6c2-4f76-8a3a-2d8fb4c371c5.png
tags: ["AWS", "IAM", "120daysofaws", "cloudsecurity", "Devops"]
brief: "Every AWS account starts with one identity that can do everything: the root user. IAM policies cannot restrict it, so if someone gets in, there is no…"
series: "DevOps & AWS"
serial: 40
---

> Originally published at [sishodiarobin.hashnode.dev](https://sishodiarobin.hashnode.dev/protect-the-aws-root-account-and-turn-on-mfa). This is an automated backup; read and comment on the blog.

Every AWS account starts with one identity that can do everything: the **root user**. IAM policies cannot restrict it, so if someone gets in, there is no safety net. Before building anything else, lock it down.

## What the root user is (and is not)

- It is the email address you signed up with, and it has **unrestricted access** to the whole account, including billing and closing the account.
- It is **not** an IAM user, so you cannot limit it with a policy.
- You should almost never sign in with it. Daily work belongs to IAM identities (Day 1) and roles (Day 3).

## The root account checklist

| Step | Why it matters |
| --- | --- |
| Turn on **MFA** for the root user | A stolen password alone is no longer enough |
| Use a **long, unique password** in a password manager | Root should not share a password with anything else |
| **Delete root access keys** (or never create them) | A leaked key would have full power with no MFA prompt |
| Use a **shared mailbox or alias** you control | You keep recovery access if one person leaves |
| Keep alternate contacts and billing alerts up to date | You hear about problems early |

## Choosing an MFA type

- **Passkey or security key (FIDO2):** phishing-resistant, the strongest everyday option.
- **Authenticator app (TOTP):** free, quick to set up, and fine for most learners.
- **Hardware TOTP token:** a physical code generator, mostly for strict environments.

You can register more than one MFA device on the same user, so add a second one as a backup.

## Hands-on: try it in your own account

1. Sign in as the root user, open the account menu and choose **Security credentials**.
2. Under **Multi-factor authentication (MFA)**, choose **Assign MFA device**.
3. Give it a clear name, pick **Authenticator app** or **Passkey or security key**, and follow the prompts.
4. Under **Access keys**, confirm there are none. If there are, delete them.
5. Sign out and sign in again to confirm the MFA prompt appears.
6. Create an IAM admin identity for daily use and stop using root.

## Common mistakes

- Using root for everyday tasks "just this once".
- Keeping root access keys in a script or a laptop folder.
- Registering MFA on a single phone with no backup device.
- Using a personal inbox that only one person can read.

## What only root can do

A short list of tasks still needs root, such as changing the account name or email, closing the account and restoring IAM permissions if you lock yourself out. That is the only reason to sign in as root.

## Key takeaways

- The root user is unrestricted, so protect it before anything else.
- Turn on MFA, remove access keys and keep a backup MFA device.
- Do real work with IAM users and roles, not root.

Tomorrow I'll look at what comes next once the front door is locked.
