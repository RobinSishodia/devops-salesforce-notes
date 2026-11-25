---
title: "Amazon S3 Bucket Policies and Block Public Access: Keep Your Buckets Private"
date: 2026-11-25T09:19:52+00:00
canonical_url: https://sishodiarobin.hashnode.dev/amazon-s3-bucket-policies-and-block-public-access-keep-your-buckets-private
cover_image: https://cdn.hashnode.com/uploads/covers/6693dc4e158429a5c6ab492f/fd45dc0b-3712-48a1-b689-f6df18bedcc6.png
tags: ["AWS", "Amazon S3", "cloud security", "Devops"]
brief: "An S3 bucket should never be public by accident. Two features control who can reach your data: Block Public Access and bucket policies. Together they keep…"
series: "DevOps & AWS"
serial: 58
---

> Originally published at [sishodiarobin.hashnode.dev](https://sishodiarobin.hashnode.dev/amazon-s3-bucket-policies-and-block-public-access-keep-your-buckets-private). This is an automated backup; read and comment on the blog.

An S3 bucket should never be public by accident. Two features control who can reach your data: **Block Public Access** and **bucket policies**. Together they keep a bucket private and say exactly who else may use it.

## What they do

- **Block Public Access** is a safety switch that stops buckets and objects from becoming public, even if a policy or ACL tries to allow it.
- A **bucket policy** is a JSON resource policy that says which principals can do which actions on the bucket.
- You can set Block Public Access on the **account** and on each **bucket**.

## Key concepts

| Piece | What it is |
| --- | --- |
| **Block Public Access** | Four settings that block public ACLs and public policies |
| **Bucket policy** | JSON policy attached to the bucket |
| **Principal** | Who the policy applies to, such as an account, role or service |
| **Action** | What they may do, such as `s3:GetObject` |
| **Resource** | The bucket or objects the rule covers |
| **Condition** | Extra limits, such as requiring HTTPS |

## Good to know

- **Block all public access** is on by default for new buckets. Leave it on unless you really need a public site.
- An **explicit Deny** always beats an Allow.
- Use `aws:SecureTransport` in a condition to **deny HTTP** requests.
- The bucket ARN covers the bucket, and `bucket/*` covers the objects inside it.
- For public websites, put **CloudFront** in front and keep the bucket private.
- **IAM Access Analyzer for S3** can show buckets that are shared outside your account.

## Hands-on: try it in your own account

1. Open **S3** and create a bucket such as `demo-policy-<your-name>`.
2. Keep **Block all public access** turned on.
3. Open the bucket's **Permissions** tab and look at the Block Public Access settings.
4. Choose **Bucket policy** and add a statement that **denies** requests that do not use HTTPS, using the condition `aws:SecureTransport = false`.
5. Save the policy.
6. Try to add a policy that allows `Principal: "*"` and read the error, because Block Public Access stops it.
7. Open **Access Analyzer for S3** and check that nothing is public.
8. Clean up: delete the policy and the bucket.

## Common mistakes

- Turning off Block Public Access to fix an unrelated error.
- Using `Principal: "*"` with an Allow and forgetting what it exposes.
- Mixing up the bucket ARN and the object ARN (`bucket/*`).
- Making a bucket public to host a website instead of using CloudFront.
- Forgetting the explicit Deny always wins when debugging access.

## Key takeaways

- Keep Block Public Access on for accounts and buckets.
- Use a bucket policy to say exactly who can do what.
- Deny HTTP with `aws:SecureTransport`.
- Check shared buckets with Access Analyzer.

Tomorrow I'll start a new AWS topic.

*Part of #120DaysOfAWS.*
