---
title: "AWS VPC for Beginners: Subnets, Route Tables, Gateways and Security Groups"
date: 2026-10-06T18:58:21+00:00
canonical_url: https://sishodiarobin.hashnode.dev/aws-vpc-for-beginners-subnets-route-tables-gateways-and-security-groups
cover_image: https://cdn.hashnode.com/uploads/covers/6693dc4e158429a5c6ab492f/fbe0394d-2e2e-4c5d-83ee-badaeb008838.png
tags: ["AWS", "networking", "vpc", "Cloud"]
brief: "Beginner's guide to AWS VPC: CIDR blocks, public and private subnets, internet and NAT gateways, route tables, security groups and NACLs."
---

> Originally published at [sishodiarobin.hashnode.dev](https://sishodiarobin.hashnode.dev/aws-vpc-for-beginners-subnets-route-tables-gateways-and-security-groups). This is an automated backup; read and comment on the blog.

A **Virtual Private Cloud (VPC)** is your own private network inside AWS. Every EC2 instance, RDS database and many Lambda functions live in one. Networking was the part of AWS that confused me most at first, so here is the explanation I wish I'd had.

## The VPC and its CIDR block

When you create a VPC, you give it an IP range in **CIDR** notation, for example:

```
10.0.0.0/16   →   65,536 addresses (10.0.0.0 – 10.0.255.255)
```

A VPC lives in **one region** but spans all of that region's Availability Zones.

## Subnets

A **subnet** is a slice of the VPC's range in **one Availability Zone**:

```
10.0.1.0/24   public subnet   (AZ a)
10.0.2.0/24   public subnet   (AZ b)
10.0.11.0/24  private subnet  (AZ a)
10.0.12.0/24  private subnet  (AZ b)
```

AWS reserves 5 addresses in every subnet, so a `/24` gives you 251 usable IPs.

**Public vs private** isn't a setting. It depends on the subnet's **route table**.

## Internet Gateway

An **Internet Gateway (IGW)** connects the VPC to the internet. A subnet is **public** when its route table sends internet traffic to the IGW:

```
Destination     Target
10.0.0.0/16     local
0.0.0.0/0       igw-xxxx
```

Instances in it also need a public IP to be reachable.

## NAT Gateway

Instances in **private** subnets often still need to reach the internet (to download updates, for example) without being reachable *from* it. A **NAT Gateway** sits in a public subnet and handles that:

```
Private subnet route table
Destination     Target
10.0.0.0/16     local
0.0.0.0/0       nat-xxxx
```

NAT Gateways are charged per hour plus per GB processed, so they're often one of the bigger networking costs. For high availability, use one per AZ.

## Route tables

Every subnet is associated with one **route table**. The `local` route (VPC CIDR → local) is always there, so everything inside the VPC can talk to everything else unless security rules block it.

## Security groups vs network ACLs

|  | Security Group | Network ACL |
| --- | --- | --- |
| Applies to | Network interfaces (instances) | Subnets |
| Rules | Allow only | Allow and deny |
| State | **Stateful** (return traffic allowed automatically) | **Stateless** (must allow return traffic explicitly) |
| Evaluation | All rules together | In number order, first match wins |

In practice, **security groups do most of the work**. A common pattern is referencing one security group from another, for example: "the database security group allows port 5432 only from the app security group."

## A classic three-tier layout

```
Internet
   │
Internet Gateway
   │
Public subnets   →  Load balancer, NAT Gateway
   │
Private subnets  →  App servers (EC2 / ECS)
   │
Private subnets  →  Database (RDS)
```

Only the load balancer is exposed. App servers and databases stay private.

## Other pieces you'll meet

- **VPC endpoints** – reach services like S3 or DynamoDB privately, without a NAT Gateway (and often more cheaply)
- **VPC peering / Transit Gateway** – connect VPCs together
- **VPC Flow Logs** – record traffic metadata for troubleshooting and security

## Troubleshooting connectivity

When something can't connect, check in this order:

1. Route table of the source subnet
2. Security group on the destination (inbound) and source (outbound)
3. Network ACLs on both subnets (remember return traffic)
4. Public IP / Elastic IP if internet access is involved
5. VPC Flow Logs to see whether traffic was accepted or rejected

Once you can draw your VPC on paper, most networking problems become much easier to solve.
