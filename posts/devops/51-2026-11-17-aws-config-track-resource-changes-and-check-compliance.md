---
title: "AWS Config: Track Resource Changes and Check Compliance"
date: 2026-11-17T16:07:42+00:00
canonical_url: https://sishodiarobin.hashnode.dev/aws-config-track-resource-changes-and-check-compliance
cover_image: https://cdn.hashnode.com/uploads/covers/6693dc4e158429a5c6ab492f/495683c3-d27b-4606-89d1-9bb43b9efdf2.png
tags: ["AWS", "AWS Config", "Cloud Computing", "Devops"]
brief: "CloudTrail tells me who made a change. The next question is different: what did the resource look like before, and does it follow my rules? That is the job…"
series: "DevOps & AWS"
serial: 51
---

> Originally published at [sishodiarobin.hashnode.dev](https://sishodiarobin.hashnode.dev/aws-config-track-resource-changes-and-check-compliance). This is an automated backup; read and comment on the blog.

CloudTrail tells me who made a change. The next question is different: **what did the resource look like before, and does it follow my rules?** That is the job of **AWS Config**.

## What AWS Config does

- It **records the configuration** of supported AWS resources and keeps a history of how each one changed.
- It checks those configurations against **rules** and reports each resource as **compliant** or **non-compliant**.
- It works **per Region**, so you set it up in each Region you use.

## CloudTrail and Config together

| Question | Service |
| --- | --- |
| Who made this API call, and when? | **CloudTrail** |
| What did this resource look like last week? | **Config** |
| Is this resource following our rule? | **Config** |

## The building blocks

| Term | What it is | Notes |
| --- | --- | --- |
| **Configuration recorder** | Records resource settings | Choose all resources or specific types |
| **Configuration item** | A snapshot of one resource at a point in time | Builds the resource timeline |
| **Config rule** | A check on a resource setting | AWS managed rules or your own |
| **Compliance status** | Result of a rule | COMPLIANT or NON\_COMPLIANT |
| **Remediation** | An action to fix a non-compliant resource | Can run an SSM Automation document |

## Examples of managed rules

- `s3-bucket-public-read-prohibited` flags buckets that allow public reads.
- `restricted-ssh` flags security groups that allow SSH from anywhere.
- `encrypted-volumes` flags EBS volumes that are not encrypted.

## Hands-on: try it in your own account

1. Open **AWS Config** and choose **Set up** (or **Get started**).
2. Record **specific resource types** such as S3 buckets and security groups, to keep it small.
3. Let it create an S3 bucket for the delivery channel and the service-linked role.
4. Add the managed rule `s3-bucket-public-read-prohibited`, then add `restricted-ssh`.
5. Wait for the first evaluation, then open **Rules** and read the compliance status.
6. Open **Resources**, pick a security group and read its **resource timeline**.
7. Check from the CLI: `aws configservice describe-compliance-by-config-rule`
8. When you finish practising, stop the recorder: `aws configservice stop-configuration-recorder --configuration-recorder-name default`

## Common mistakes

- Setting up Config in one Region and expecting it everywhere.
- Recording every resource type for a small practice account without checking the cost.
- Adding rules but never looking at the non-compliant list.
- Forgetting to stop the recorder after practice.

## Key takeaways

- Config records how resources change and checks them against rules.
- CloudTrail answers who, Config answers what and whether it is compliant.
- Start with a few managed rules and review the results.
- Watch the cost, because it depends on what you record and evaluate.

Tomorrow I'll look at AWS Systems Manager and how it manages instances without opening SSH.

*Part of #120DaysOfAWS.*
