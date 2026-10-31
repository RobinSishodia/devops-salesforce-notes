---
title: "Building a DevOps Support-Ticket Platform, Part 1: Ubuntu on AWS EC2"
date: 2026-10-30T19:56:50+00:00
canonical_url: https://sishodiarobin.hashnode.dev/building-a-devops-support-ticket-platform-part-1-ubuntu-on-aws-ec2
cover_image: 
tags: []
brief: "I'm starting a hands-on DevOps project around a support-ticket application. The application will grow through Linux hosting, containers, CI/CD…"
---

> Originally published at [sishodiarobin.hashnode.dev](https://sishodiarobin.hashnode.dev/building-a-devops-support-ticket-platform-part-1-ubuntu-on-aws-ec2). This is an automated backup; read and comment on the blog.

I'm starting a hands-on DevOps project around a support-ticket application. The application will grow through Linux hosting, containers, CI/CD, infrastructure as code, Kubernetes, and recovery exercises.

This first checkpoint is deliberately small: launch an Ubuntu server on AWS, restrict its SSH access, connect to it, and verify the operating system. The ticket application is not deployed yet.

I’m using AI assistance for setup and documentation. My learning rule is to understand each change, check the actual output, and record what has been completed before moving on.

## What I launched

| Setting | Lab configuration |
| --- | --- |
| Region | Asia Pacific (Mumbai), `ap-south-1` |
| Operating system | Canonical Ubuntu Server 24.04 LTS, x86\_64 |
| Instance type | One `t2.micro` |
| Root disk | 8 GiB, gp3 |
| Network | Default VPC and a public subnet |
| Public IPv4 | Enabled |
| Login | EC2 Instance Connect as `ubuntu` |
| Persistent SSH key pair | None; browser login uses temporary keys |

This is an initial learning configuration. It is not a claim of production readiness or high availability.

## The connection path

The browser connects through EC2 Instance Connect to the instance’s SSH service on TCP port 22. Successful access needs both authentication and a working network path.

A public IP alone is not enough. The subnet also needs a route to an internet gateway, the instance needs an SSH service, and the security group must allow the connection source.

## Restricting SSH correctly

The launch wizard initially offered SSH from `0.0.0.0/0`. That would allow connection attempts from any IPv4 address. I replaced it with the AWS-managed prefix list for EC2 Instance Connect in Mumbai:

```text
com.amazonaws.ap-south-1.ec2-instance-connect
```

The inbound rule is SSH, TCP 22, with that prefix list as its source. I did not open an application or database port at this checkpoint.

There is an important distinction here:

- For SSH directly from my laptop, a source of **My IP** allows my current public IP address.
- For the browser-based EC2 Instance Connect method used here, the source is AWS’s EC2 Instance Connect service, so its regional prefix list is appropriate.

The security group is only one layer. IAM permissions, temporary SSH authentication, and the instance configuration still matter. Allowing a source in a security group does not by itself authenticate a user.

## Why I did not download a PEM file

I chose **Proceed without a key pair** because this lab uses EC2 Instance Connect. It temporarily provides an SSH public key for authentication, so I did not need a saved private key on my laptop.

This is different from making the machine passwordless or publicly accessible without authentication. If I later want direct SSH access, I will configure that access explicitly.

## The first three Linux commands

After connecting, I verified the user, current directory, and distribution:

```bash
whoami
pwd
cat /etc/os-release
```

The relevant output was:

```text
ubuntu
/home/ubuntu
PRETTY_NAME="Ubuntu 24.04.5 LTS"
VERSION_ID="24.04"
```

`whoami` confirms which account is executing commands. `pwd` shows where relative file paths will start. `/etc/os-release` identifies the distribution and release, which helps choose suitable package-management instructions.

I keep commands separate while learning so it is easy to see which command produced which result.

## Cost is part of the lab

A small instance or a **Free tier eligible** label does not establish that my account has remaining free usage. Account age, plan, credits, and actual consumption affect the bill.

Compute, retained EBS storage, and public IPv4 usage can contribute charges. Closing the terminal does not stop the instance. My end-of-session routine is to save the work, stop the instance from EC2 when it is not needed, and check for resources that remain billable.

## What is complete, and what comes next

Completed: one Ubuntu EC2 instance launched, SSH limited to the connection service, browser login successful, and the user, home directory, and OS verified.

Next: refresh package metadata, install the initial tools, create a project workspace, and write a Bash health check. Nginx, the Flask application, persistence, and backups are later checkpoints.

Each checkpoint will have commands, explanations, verification results, and troubleshooting notes committed to the project repository.

**Project repository:** [devops-support-ticket-platform](https://github.com/RobinSishodia/devops-support-ticket-platform)

## Official references

- [Get started with Amazon EC2](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/EC2_GetStarted.html)
- [EC2 Instance Connect prerequisites](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-instance-connect-prerequisites.html)
- [AWS Free Tier FAQs](https://aws.amazon.com/free/free-tier-faqs/)
- [Public IPv4 pricing](https://aws.amazon.com/vpc/pricing/)
- [Stopping and starting EC2 instances](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/Stop_Start.html)
