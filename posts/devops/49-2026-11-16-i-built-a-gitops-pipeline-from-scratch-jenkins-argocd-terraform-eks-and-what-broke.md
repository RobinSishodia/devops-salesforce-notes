---
title: "I built a GitOps pipeline from scratch (Jenkins, ArgoCD, Terraform, EKS), and what broke"
date: 2026-11-16T04:22:03+00:00
canonical_url: https://sishodiarobin.hashnode.dev/i-built-a-gitops-pipeline-from-scratch-jenkins-argocd-terraform-eks-and-what-broke
cover_image: 
tags: ["Devops", "Kubernetes", "Terraform", "AWS"]
brief: "I wanted one project where a git push ends up as a running pod with no manual steps, then the same thing on real AWS. Here is what I built and what went…"
series: "DevOps & AWS"
serial: 49
---

> Originally published at [sishodiarobin.hashnode.dev](https://sishodiarobin.hashnode.dev/i-built-a-gitops-pipeline-from-scratch-jenkins-argocd-terraform-eks-and-what-broke). This is an automated backup; read and comment on the blog.

I wanted one project where a `git push` ends up as a running pod with no manual steps, then the same thing on real AWS. Here is what I built and what went wrong.

## The flow

1. I push a change to GitHub.
2. Jenkins notices it by polling (every 2 minutes), builds a Docker image and pushes it to Docker Hub.
3. Jenkins commits the new image tag into `k8s/deployment.yaml`.
4. ArgoCD sees the manifest change and syncs it to Kubernetes.

I proved it by changing the page heading and watching the new text appear without touching anything after the push. Repo: <https://github.com/RobinSishodia/aws-eks-gitops-argocd>

## Terraform and EKS

I rebuilt the cluster on AWS with Terraform: a VPC with public and private subnets and a NAT gateway, plus an EKS cluster with a managed node group. ArgoCD ran on it with the app Synced and Healthy. Then I destroyed all 56 resources, verified nothing was left, and deleted the access key.

## What went wrong

1. **Jenkins rebuilt its own commits.** The pipeline pushes a commit, so auto-triggering would loop forever. I added a guard that skips any build whose latest commit says `[skip ci]`. Jenkins core does not honour that tag by itself. I also once put that exact text in my own commit message and skipped a build I wanted.
2. **AWS Free plan instance types.** `t3.medium` was rejected as not free-tier eligible. I queried the eligible types and switched to `c7i-flex.large`.
3. **Nodes that never joined.** The EKS Terraform module does not install vpc-cni, kube-proxy or CoreDNS by default, so the nodes had no networking and the node group hung for hours. Declaring the add-ons fixed it. I also added a 25-minute create timeout so a stuck build fails fast.

## What I would do next

A real GitHub webhook instead of polling (it needs Jenkins reachable from the internet), then monitoring with Prometheus and Grafana.
