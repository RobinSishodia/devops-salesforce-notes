---
title: "AWS Tagging Strategy: Name, Owner and Environment Tags for Every Resource"
date: 2026-11-10T18:49:12+00:00
canonical_url: https://sishodiarobin.hashnode.dev/aws-tagging-strategy-name-owner-and-environment-tags-for-every-resource
cover_image: https://cdn.hashnode.com/uploads/covers/6693dc4e158429a5c6ab492f/663c873f-a882-420e-b81b-74b8731154b3.png
tags: ["AWS", "tagging", "120daysofaws", "Devops"]
brief: "By now I have IAM, a budget, CloudTrail and CloudWatch. One more habit makes all of them easier to use: tags. When the bill rises or something looks odd…"
series: "DevOps & AWS"
serial: 44
---

> Originally published at [sishodiarobin.hashnode.dev](https://sishodiarobin.hashnode.dev/aws-tagging-strategy-name-owner-and-environment-tags-for-every-resource). This is an automated backup; read and comment on the blog.

By now I have IAM, a budget, CloudTrail and CloudWatch. One more habit makes all of them easier to use: **tags**. When the bill rises or something looks odd, tags tell you **what the resource is, who owns it and what it is for**.

## What tags are

- A tag is a **key and value pair** attached to a resource, such as `Environment = dev`.
- Most AWS resources support tags, and you can have up to **50 tags per resource**.
- Tags are labels for people and tools. They do not change how the resource works.

## A simple starting set

| Key | Example value | Why |
| --- | --- | --- |
| **Name** | `web-server-1` | Shows in the console list |
| **Environment** | `dev`, `test`, `prod` | Separate workloads |
| **Owner** | `robin` | Who to ask |
| **Project** | `blog-site` | Group related resources |
| **CostCenter** | `learning` | Split the bill |

## What tags are used for

- **Cost allocation:** activate **cost allocation tags** in Billing, then filter Cost Explorer by tag.
- **Access control:** IAM policies can allow or deny actions based on tags (ABAC).
- **Automation:** scripts can find resources by tag, such as all `Environment = dev` instances to stop at night.
- **Search:** Tag Editor and Resource Groups find resources across Regions.

## Good to know

- Tag keys and values are **case sensitive**, so `Owner` and `owner` are different.
- Tags are **not retroactive** in Cost Explorer. Cost allocation tags only show costs from the time you activate them.
- **Tag policies** in AWS Organizations help keep names consistent.
- Do not put secrets or personal data in tags.

## Hands-on: try it in your own account

1. Open **EC2** or **S3** and select a resource you created.
2. Add the tags **Name**, **Environment**, **Owner** and **Project**.
3. Open **Resource Groups & Tag Editor** and use **Tag Editor** to search by `Environment = dev` across Regions.
4. Open **Billing** and **Cost allocation tags**, then activate `Project`.
5. After a day, filter **Cost Explorer** by the `Project` tag.

## Common mistakes

- Inconsistent keys, such as `env`, `Env` and `Environment`.
- Tagging only some resources, so reports have gaps.
- Forgetting to activate cost allocation tags.
- Storing sensitive data in tag values.

## Key takeaways

- Tags answer what, who and why for every resource.
- Pick a small standard set and use it everywhere.
- Activate cost allocation tags to see costs by tag.
- Keep tag names consistent.

Tomorrow I'll look at how to see all of this from a single place: AWS Organizations and account structure.

*Part of #120DaysOfAWS.*
