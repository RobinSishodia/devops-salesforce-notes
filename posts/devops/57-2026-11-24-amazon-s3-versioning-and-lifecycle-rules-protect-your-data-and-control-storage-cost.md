---
title: "Amazon S3 Versioning and Lifecycle Rules: Protect Your Data and Control Storage Cost"
date: 2026-11-24T18:14:55+00:00
canonical_url: https://sishodiarobin.hashnode.dev/amazon-s3-versioning-and-lifecycle-rules-protect-your-data-and-control-storage-cost
cover_image: https://cdn.hashnode.com/uploads/covers/6693dc4e158429a5c6ab492f/b751d7ba-8913-443d-aae7-dc84550da37e.png
tags: ["AWS", "Amazon S3", "Cloud Computing", "Devops"]
brief: "Amazon S3 can keep every version of an object and move or delete old data on a schedule. Two features do that: versioning and lifecycle rules. Together…"
series: "DevOps & AWS"
serial: 57
---

> Originally published at [sishodiarobin.hashnode.dev](https://sishodiarobin.hashnode.dev/amazon-s3-versioning-and-lifecycle-rules-protect-your-data-and-control-storage-cost). This is an automated backup; read and comment on the blog.

Amazon S3 can keep every version of an object and move or delete old data on a schedule. Two features do that: **versioning** and **lifecycle rules**. Together they protect you from overwrites and keep storage costs down.

## What they do

- **Versioning** keeps every version of an object in a bucket, so an overwrite or delete does not destroy the old data.
- **Lifecycle rules** move objects to cheaper storage classes or delete them after a number of days.
- You can combine them: keep recent versions in standard storage and expire old ones.

## Key concepts

| Piece | What it is |
| --- | --- |
| **Versioning** | Setting on a bucket: Enabled or Suspended |
| **Version ID** | A unique ID for each version of an object |
| **Delete marker** | What S3 adds when you delete a versioned object. The old versions stay |
| **Current vs noncurrent** | The latest version is current, older ones are noncurrent |
| **Lifecycle rule** | Rules for transitions and expiration, by prefix or tag |
| **Storage class** | For example Standard, Standard-IA, Glacier Instant Retrieval |

## Good to know

- Once enabled, versioning can only be **suspended**, never fully turned off.
- A normal delete only adds a **delete marker**. To remove data for good, delete a **specific version**.
- Every version is stored and billed, so add a rule to **expire noncurrent versions**.
- Lifecycle rules can also **abort incomplete multipart uploads**, which saves money.
- Some storage classes have **minimum storage durations** and retrieval costs, so check them before moving data.
- **MFA Delete** adds extra protection for permanent deletes.

## Hands-on: try it in your own account

1. Open **S3** and create a bucket such as `demo-versioning-<your-name>`.
2. Keep **Block all public access** on.
3. Open the bucket's **Properties** tab and turn on **Bucket Versioning**.
4. Upload a small text file called `notes.txt`.
5. Edit it locally and upload it again. Turn on **Show versions** and see two versions.
6. Delete the object and look at the **delete marker**.
7. Delete the marker and see that the old version comes back.
8. Open **Management > Create lifecycle rule**, apply it to all objects, and set noncurrent versions to expire after **7 days**.
9. Clean up: delete all versions, then delete the bucket.

## Common mistakes

- Turning on versioning and forgetting that every version costs storage.
- Thinking a delete removes the data when it only adds a delete marker.
- Making a lifecycle rule that is too broad and moves or deletes the wrong objects.
- Moving small objects to a colder class where the minimum size and duration cost more.
- Leaving test buckets and versions behind.

## Key takeaways

- Versioning protects against overwrites and accidental deletes.
- Lifecycle rules control cost by moving and expiring data.
- Expire noncurrent versions, or storage keeps growing.
- Test a lifecycle rule on a small prefix first.

Tomorrow I'll start a new AWS topic.

*Part of #120DaysOfAWS.*
