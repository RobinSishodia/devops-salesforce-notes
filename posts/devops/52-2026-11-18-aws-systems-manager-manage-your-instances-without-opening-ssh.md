---
title: "AWS Systems Manager: Manage Your Instances Without Opening SSH"
date: 2026-11-18T14:25:38+00:00
canonical_url: https://sishodiarobin.hashnode.dev/aws-systems-manager-manage-your-instances-without-opening-ssh
cover_image: https://cdn.hashnode.com/uploads/covers/6693dc4e158429a5c6ab492f/4f94d4e8-c49f-4196-a3f5-64b2513ea64f.png
tags: ["AWS", "AWS Systems Manager", "Cloud Computing", "Devops"]
brief: "Config shows what changed and whether it follows the rules. The next question is how to actually manage the instances without opening SSH to the world…"
series: "DevOps & AWS"
serial: 52
---

> Originally published at [sishodiarobin.hashnode.dev](https://sishodiarobin.hashnode.dev/aws-systems-manager-manage-your-instances-without-opening-ssh). This is an automated backup; read and comment on the blog.

Config shows what changed and whether it follows the rules. The next question is how to actually **manage** the instances without opening SSH to the world. That is where **AWS Systems Manager** comes in.

## What it does

- Systems Manager is a set of tools to **view and manage** your AWS resources and nodes from one place.
- A **managed node** is an instance (or server) that runs the **SSM Agent** and can reach Systems Manager.
- You can connect, run commands and patch **without opening inbound port 22** and without key pairs.

## The tools to know first

| Tool | What it does | Example use |
| --- | --- | --- |
| **Session Manager** | Opens a shell from the console or CLI | Log in with no SSH and no bastion host |
| **Run Command** | Runs a command on one or many nodes | Run `uptime` on a group of instances |
| **Patch Manager** | Scans and installs patches | Patch on a schedule |
| **Parameter Store** | Stores configuration values and secrets | Keep a database name or a secure string |
| **Automation** | Runs runbooks for common tasks | Stop an instance, create an AMI |

## What an instance needs to become a managed node

- The **SSM Agent** installed and running (it comes pre-installed on many Amazon-provided AMIs, including Amazon Linux 2023).
- An **instance profile** with an IAM role, for example the AWS managed policy `AmazonSSMManagedInstanceCore`.
- A network path to the Systems Manager endpoints, such as a public route or **VPC endpoints**.

## Hands-on: try it in your own account

1. Open **IAM**, create a role for **EC2**, and attach `AmazonSSMManagedInstanceCore`.
2. Launch a small **Amazon Linux 2023** instance and choose that role as the **IAM instance profile**.
3. In the security group, **remove all inbound rules**. You will not use SSH.
4. Open **Systems Manager**, then **Fleet Manager** or **Session Manager**, and wait until the instance shows as a managed node.
5. In **Session Manager**, choose **Start session**, pick the instance, and run `whoami`.
6. Open **Run Command**, choose the document `AWS-RunShellScript`, enter `uptime` and run it on the instance.
7. Check from the CLI: `aws ssm describe-instance-information`
8. When you finish practising, terminate the instance and delete the role.

## Common mistakes

- Forgetting to attach the instance profile, so the node never appears.
- Using an instance with no route to the Systems Manager endpoints.
- Leaving port 22 open even though Session Manager makes it unnecessary.
- Giving the instance role more permissions than it needs.
- Leaving practice instances running.

## Key takeaways

- Systems Manager manages nodes without SSH or key pairs.
- An instance needs the agent, an instance profile and network access.
- Session Manager is for access, Run Command for tasks, Patch Manager for updates.
- Clean up practice instances when you finish.

Tomorrow I'll look at AWS Secrets Manager and Parameter Store, and how to keep secrets out of your code.

*Part of #120DaysOfAWS.*
