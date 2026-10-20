---
title: "Salesforce Sandbox Types Explained: Developer, Developer Pro, Partial Copy and Full"
date: 2026-10-06T18:55:43+00:00
canonical_url: https://sishodiarobin.hashnode.dev/salesforce-sandbox-types-explained-developer-developer-pro-partial-copy-and-full
cover_image: https://cdn.hashnode.com/uploads/covers/6693dc4e158429a5c6ab492f/a390ec75-d149-40f3-92ab-70bff4950d11.png
tags: ["Salesforce", "Salesforce Admin", "Devops", "Testing"]
brief: "The four Salesforce sandbox types compared: storage, data, refresh intervals and which one to use for development, testing, UAT and training."
---

> Originally published at [sishodiarobin.hashnode.dev](https://sishodiarobin.hashnode.dev/salesforce-sandbox-types-explained-developer-developer-pro-partial-copy-and-full). This is an automated backup; read and comment on the blog.

A sandbox is a copy of your production org used for building and testing without touching real users. Salesforce offers four types, and picking the right one for each stage of your release process saves a lot of pain.

## The four types at a glance

| Type | Copies metadata | Copies data | Storage (data / files) | Refresh interval |
| --- | --- | --- | --- | --- |
| **Developer** | Yes | No | 200 MB / 200 MB | 1 day |
| **Developer Pro** | Yes | No | 1 GB / 1 GB | 1 day |
| **Partial Copy** | Yes | Sample (via template) | 5 GB / same as prod | 5 days |
| **Full** | Yes | All (or selected objects) | Same as production | 29 days |

All sandboxes copy your **metadata** (objects, fields, flows, Apex, layouts and so on). The difference is how much **data** comes with it and how often you can refresh. Which types and how many you get depends on your edition and any add-ons.

## Developer sandbox

Small and quick to refresh. Ideal for:

- An individual admin or developer building a feature
- Trying out a new flow or configuration
- Learning and experimenting

You create the test data you need yourself.

## Developer Pro sandbox

The same idea with more storage. Useful when:

- You need larger test data sets
- You're doing integration development
- Several people share the environment

## Partial Copy sandbox

Includes a **sample of production data** chosen by a **sandbox template** (you pick objects; Salesforce copies up to 10,000 records per object). Good for:

- QA and integration testing with realistic data
- Testing reports, sharing and automation against real-looking records

## Full sandbox

A complete replica of production, including all data (or the objects you select). Use it for:

- **User acceptance testing (UAT)**
- **Performance and load testing**
- **Staging**: the final check before a production release
- Training on real-world data

The 29-day refresh interval means you need to plan when you refresh it.

## A typical setup

```
Developer sandboxes  →  Developer Pro / Partial (QA)  →  Full (UAT/Staging)  →  Production
```

Each person builds in their own Developer sandbox, changes are combined and tested in QA, business users sign off in UAT, and then you deploy to production.

## Tips

- **Mask sensitive data.** Production data in sandboxes is still personal data. Use **Data Mask** or scripts to anonymise it.
- **Check email deliverability.** New sandboxes default to "System email only" so you don't email real customers. Keep it that way unless you need to test emails.
- **Re-run post-refresh steps.** Use a **SandboxPostCopy** Apex class to automate tasks such as updating integration endpoints and creating test users.
- **Mind the user emails.** Sandbox users' emails get `.invalid` appended so they can't receive mail by accident. Fix only the ones you need.
- **Know the difference from scratch orgs.** Scratch orgs are short-lived, source-driven orgs created from a definition file, which suits CI pipelines. Sandboxes are copies of production, which suits integration testing and UAT.

Choosing the right sandbox for each stage keeps development fast and testing realistic, without risking production.
