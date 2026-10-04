---
title: "AWS IAM Explained: Users, Groups, Roles and Policies for Beginners"
date: 2026-10-03T21:45:02+00:00
canonical_url: https://sishodiarobin.hashnode.dev/aws-iam-explained-users-groups-roles-and-policies-for-beginners
cover_image: https://cdn.hashnode.com/uploads/covers/6693dc4e158429a5c6ab492f/3f10720e-03d9-4134-bde3-75ae30fe3eba.png
tags: ["AWS", "IAM", "cloud security", "Devops"]
brief: "Almost every AWS problem I've debugged as a beginner came back to one thing: permissions. AWS Identity and Access Management (IAM) decides who can do what in your account, so it's worth understanding"
---

> Originally published at [sishodiarobin.hashnode.dev](https://sishodiarobin.hashnode.dev/aws-iam-explained-users-groups-roles-and-policies-for-beginners). This is an automated backup; read and comment on the blog.

Almost every AWS problem I've debugged as a beginner came back to one thing: **permissions**. AWS Identity and Access Management (IAM) decides who can do what in your account, so it's worth understanding properly before anything else.

## The four building blocks

### Users

An IAM **user** is an identity for a person or an application that needs long-term credentials (a password for the console, or access keys for the CLI).

Best practice today is to avoid long-lived access keys where you can. For people, use **IAM Identity Center** (single sign-on). For workloads, use **roles**.

### Groups

A **group** is a collection of users. You attach permissions to the group, and every user in it inherits them. For example, a `Developers` group might get read access to CloudWatch logs and permission to deploy Lambda functions.

Groups cannot contain other groups, and a group is not an identity you can log in as.

### Roles

A **role** is an identity with permissions but **no permanent credentials**. Something *assumes* the role and gets temporary credentials. Roles are used by:

- EC2 instances (via an instance profile)
- Lambda functions (the execution role)
- Other AWS accounts (cross-account access)
- CI/CD systems such as GitHub Actions (via OpenID Connect)
- People signing in through SSO

If you remember one thing from this post: **prefer roles over access keys**.

### Policies

A **policy** is a JSON document that allows or denies actions. Here's a small example that allows reading objects from one S3 bucket:

```json
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Effect": "Allow",
      "Action": ["s3:GetObject"],
      "Resource": "arn:aws:s3:::my-app-bucket/*"
    }
  ]
}
```

Every statement has an **Effect** (Allow or Deny), **Actions**, **Resources** and optionally **Conditions**.

## How AWS evaluates permissions

1. By default, everything is **denied**.
2. An explicit **Allow** in a policy grants access.
3. An explicit **Deny** anywhere **always wins** over an Allow.

Other layers can also restrict access, such as Service Control Policies in AWS Organizations, permission boundaries and resource-based policies (like S3 bucket policies).

## Policy types you'll meet

- **AWS managed policies** – prebuilt by AWS (for example `ReadOnlyAccess`). Convenient but often broader than you need.
- **Customer managed policies** – written by you and reusable across users, groups and roles.
- **Inline policies** – embedded directly in one identity. Use them sparingly.

## Least privilege in practice

"Least privilege" means granting only what's needed. Practical ways to get there:

- Start from a managed policy, then narrow it down to specific actions and resources.
- Use **IAM Access Analyzer** to generate policies from real CloudTrail activity and to find resources shared outside your account.
- Check the **Last accessed** information on users and roles to remove unused permissions.

## Common beginner mistakes

- **Using the root user for daily work.** Lock it down with MFA and use it only for the few tasks that require it.
- **Committing access keys to Git.** Use roles, or store secrets in a secrets manager.
- **`"Action": "*"` and `"Resource": "*"` everywhere.** It works, until it becomes a security incident.
- **Not enabling MFA** for human users.

## Quick checklist

- MFA on the root user, root access keys deleted
- People sign in through IAM Identity Center or users with MFA
- Applications use roles, not access keys
- Permissions granted to groups and roles, not individual users
- Access Analyzer enabled

IAM looks dry, but once it clicks, the rest of AWS becomes much easier to reason about. Tomorrow I'll switch to Salesforce and look at its security model.
