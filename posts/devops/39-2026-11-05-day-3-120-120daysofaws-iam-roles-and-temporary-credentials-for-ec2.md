---
title: "Day 3/120 – #120DaysOfAWS: IAM Roles and Temporary Credentials for EC2"
date: 2026-11-05T08:24:48+00:00
canonical_url: https://sishodiarobin.hashnode.dev/day-3-120-120daysofaws-iam-roles-and-temporary-credentials-for-ec2
cover_image: https://cdn.hashnode.com/uploads/covers/6693dc4e158429a5c6ab492f/0099bc68-809e-41e0-993c-4f482644f64c.png
tags: ["AWS", "IAM", "120daysofaws", "cloudsecurity", "Devops"]
brief: "On Day 2 I wrote a least-privilege policy for one S3 bucket. The next question is who gets to use it. For people, that's a user or group. For servers and…"
series: "DevOps & AWS"
serial: 39
---

> Originally published at [sishodiarobin.hashnode.dev](https://sishodiarobin.hashnode.dev/day-3-120-120daysofaws-iam-roles-and-temporary-credentials-for-ec2). This is an automated backup; read and comment on the blog.

On Day 2 I wrote a least-privilege policy for one S3 bucket. The next question is who gets to use it. For people, that's a user or group. For servers and apps, it should be a **role**, so nothing long-lived ever sits on the machine.

## Users vs roles

|  | IAM user | IAM role |
| --- | --- | --- |
| **For** | A person | A service, an app or a person who needs temporary access |
| **Credentials** | Long-term (password, access keys) | Temporary, issued on demand |
| **Rotation** | You do it | Automatic |
| **Typical use** | Console and CLI sign-in | EC2, Lambda, cross-account access |

## Two policies on every role

- **Trust policy:** who is allowed to assume the role (for example `ec2.amazonaws.com`).
- **Permissions policy:** what the role can do once assumed (for example the Day 2 S3 read policy).

A trust policy for EC2 looks like this:

```json
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Effect": "Allow",
      "Principal": { "Service": "ec2.amazonaws.com" },
      "Action": "sts:AssumeRole"
    }
  ]
}
```

## How EC2 gets credentials

1. The role is attached to the instance through an **instance profile** (the console creates it for you when you make an EC2 role).
2. Software on the instance asks the **instance metadata service** for credentials.
3. **STS** (Security Token Service) issues a temporary access key, secret key and session token.
4. AWS refreshes them automatically before they expire, so nothing is stored on disk.

## Hands-on: try it in your own account

1. Create a role: trusted entity **AWS service, EC2**.
2. Attach the `ReadDemoBucketOnly` policy from Day 2 (or any least-privilege S3 read policy).
3. Launch a small EC2 instance and attach the role under **Actions, Security, Modify IAM role**.
4. Connect to the instance and run:

```bash
aws sts get-caller-identity
aws s3 ls s3://your-demo-bucket
aws s3 ls s3://some-other-bucket   # should be denied
```

5. To see the temporary credentials the instance receives (IMDSv2):

```bash
TOKEN=$(curl -s -X PUT "http://169.254.169.254/latest/api/token" \
  -H "X-aws-ec2-metadata-token-ttl-seconds: 21600")
curl -s -H "X-aws-ec2-metadata-token: $TOKEN" \
  http://169.254.169.254/latest/meta-data/iam/security-credentials/
```

`get-caller-identity` should show an **assumed-role** ARN instead of a user, which proves the instance is using the role. Don't paste the credentials from the metadata call anywhere.

## Common mistakes to avoid

1. Putting access keys in code, config files or an AMI "just for now".
2. Making the trust policy too wide, for example trusting a whole account when one role is enough.
3. Attaching `AdministratorAccess` to a role so the app "just works".
4. Forgetting the role is attached to the instance but the app still uses old keys from a config file.

## 3 habits I'm keeping

1. Workloads get roles, people get users or federated sign-in, never the other way round.
2. Keep trust and permissions separate and check both when access fails.
3. Run `aws sts get-caller-identity` first whenever something is denied.

Tomorrow (Day 4): protecting the root account and turning on MFA.
