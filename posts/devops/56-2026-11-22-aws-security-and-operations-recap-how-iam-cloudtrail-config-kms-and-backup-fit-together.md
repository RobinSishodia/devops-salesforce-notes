---
title: "AWS Security and Operations Recap: How IAM, CloudTrail, Config, KMS and Backup Fit Together"
date: 2026-11-22T15:16:07+00:00
canonical_url: https://sishodiarobin.hashnode.dev/aws-security-and-operations-recap-how-iam-cloudtrail-config-kms-and-backup-fit-together
cover_image: https://cdn.hashnode.com/uploads/covers/6693dc4e158429a5c6ab492f/fdb0868b-38c8-47ac-9187-f11ead1b0f44.png
tags: ["AWS", "cloud security", "Cloud Computing", "Devops"]
brief: "How to decide between Salesforce Flow and Apex for automation: what Flow handles well, when Apex is the better choice, and how to combine them."
series: "DevOps & AWS"
serial: 56
---

> Originally published at [sishodiarobin.hashnode.dev](https://sishodiarobin.hashnode.dev/aws-security-and-operations-recap-how-iam-cloudtrail-config-kms-and-backup-fit-together). This is an automated backup; read and comment on the blog.

Over the last few posts I covered the services that keep an AWS account safe and tidy. Today is a recap: what each one does, and how they fit together.

## The series at a glance

| Service | What it answers |
| --- | --- |
| **IAM Identity Center** | Who can sign in, and to which accounts and roles |
| **CloudWatch Alarms + SNS** | Is something wrong right now, and who gets told |
| **CloudTrail** | Who did what, and when |
| **AWS Config** | What does the setup look like, and does it follow the rules |
| **Systems Manager** | How do I manage and patch my instances without logging in one by one |
| **Secrets Manager and Parameter Store** | Where do passwords and settings live, outside the code |
| **AWS KMS** | Who holds the keys that protect the data |
| **AWS Backup** | Can I get the data back if it is lost |

## How they fit together

- **Access:** IAM Identity Center gives people the right access, and CloudTrail records what they do.
- **Visibility:** CloudWatch Alarms tell you when something looks wrong, and SNS sends the message.
- **Rules:** AWS Config checks resources against rules, so drift gets noticed.
- **Operations:** Systems Manager lets you run commands and patch at scale.
- **Secrets and keys:** Secrets Manager and Parameter Store keep values out of the code, and KMS protects them.
- **Recovery:** AWS Backup keeps recovery points, which can be encrypted with KMS.

## Quick questions to ask yourself

1. Who can access this account, and is it least privilege?
2. If something changes, will I see it in CloudTrail?
3. Will an alarm tell me before a user does?
4. Are my secrets out of the code, and is the key policy tight?
5. Have I tested a restore?

## Hands-on: a simple self-check in your own account

1. In **CloudTrail**, confirm a trail or event history shows recent activity.
2. In **AWS Config**, check whether recording is on and look at one rule.
3. In **CloudWatch**, list your alarms and see who gets the SNS message.
4. In **Secrets Manager** or **Parameter Store**, make sure no secret sits in plain text in your code.
5. In **KMS**, read one key policy.
6. In **AWS Backup**, check that a plan exists and that its resources are assigned.
7. Write down one gap and fix it this week.

## Common mistakes

- Turning services on once and never looking at them again.
- Alarms that send to an inbox nobody reads.
- Secrets in code or in plain environment values.
- Backups that were never restored.
- Leaving practice resources behind and paying for them.

## Key takeaways

- These services work as a set: access, visibility, rules, operations, secrets and recovery.
- Least privilege and logging come first.
- Keep secrets and keys out of the code.
- Test your alarms and your restores.

Tomorrow I'll start a new AWS topic.

*Part of #120DaysOfAWS.*
