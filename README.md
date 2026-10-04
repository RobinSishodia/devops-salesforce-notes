# 📝 DevOps & Salesforce Notes

Hands-on articles on **Salesforce Administration**, **AWS**, **DevOps** (Docker, Kubernetes, Terraform, CI/CD) and **cloud security**, written by **Robin Sishodia** while learning in public.

🔗 **Read on the blog:** [sishodiarobin.hashnode.dev](https://sishodiarobin.hashnode.dev)
💼 **LinkedIn:** [linkedin.com/in/robinsishodia](https://www.linkedin.com/in/robinsishodia)

## ⚙️ How this repo works

Posts are written on Hashnode. A **GitHub Actions** workflow ([`sync-blog.yml`](.github/workflows/sync-blog.yml)) runs whenever the feed file is updated and:

1. Converts a committed copy of the blog RSS feed ([`feed/rss.xml`](feed/rss.xml)) with [`scripts/sync_hashnode.py`](scripts/sync_hashnode.py)
2. Turns each post from HTML into Markdown and saves it in [`posts/`](posts/)
3. Rebuilds this README index and commits only when something changed

## 📚 All posts (20)

| Date | Title | Tags | Source |
|------|-------|------|--------|
| 2026-10-04 | [The Salesforce Security Model Explained: OWD, Roles, Sharing Rules and More](https://sishodiarobin.hashnode.dev/the-salesforce-security-model-explained-owd-roles-sharing-rules-and-more) | `Salesforce` `Salesforce Admin` `Security` `crm` | [Markdown](posts/2026-10-04-the-salesforce-security-model-explained-owd-roles-sharing-rules-and-more.md) |
| 2026-10-03 | [AWS IAM Explained: Users, Groups, Roles and Policies for Beginners](https://sishodiarobin.hashnode.dev/aws-iam-explained-users-groups-roles-and-policies-for-beginners) | `AWS` `IAM` `cloud security` `Devops` | [Markdown](posts/2026-10-03-aws-iam-explained-users-groups-roles-and-policies-for-beginners.md) |
| 2026-10-02 | [From Operations to Salesforce and DevOps: How I Switched Careers](https://sishodiarobin.hashnode.dev/from-operations-to-salesforce-and-devops-how-i-switched-careers) | `Career` `Devops` `Salesforce` `AWS` | [Markdown](posts/2026-10-02-from-operations-to-salesforce-and-devops-how-i-switched-careers.md) |
| 2026-10-01 | [Building a Salesforce CI/CD Pipeline with GitHub Actions and Scratch Orgs](https://sishodiarobin.hashnode.dev/building-a-salesforce-ci-cd-pipeline-with-github-actions-and-scratch-orgs) | `Salesforce` `Devops` `github-actions` `ci-cd` | [Markdown](posts/2026-10-01-building-a-salesforce-ci-cd-pipeline-with-github-actions-and-scratch-orgs.md) |
| 2025-01-15 | [Mastering Kubernetes: A Step-by-Step Guide to Pod Troubleshooting](https://sishodiarobin.hashnode.dev/mastering-kubernetes-a-step-by-step-guide-to-pod-troubleshooting) | `Kubernetes` `DevOps` `ContainerOrchestration` `Troubleshooting` | [Markdown](posts/2025-01-15-mastering-kubernetes-a-step-by-step-guide-to-pod-troubleshooting.md) |
| 2024-12-25 | [Docker CLI Cheat Sheet: Essential Commands for Containers](https://sishodiarobin.hashnode.dev/docker-cli-cheat-sheet-essential-commands-for-containers) | `Docker` `DevOps` `Containerization` `DockerCLI` | [Markdown](posts/2024-12-25-docker-cli-cheat-sheet-essential-commands-for-containers.md) |
| 2024-12-24 | [DevOps Security Solutions: A Look at Aqua, Snyk, and SonarQube](https://sishodiarobin.hashnode.dev/devops-security-solutions-a-look-at-aqua-snyk-and-sonarqube) | `DevOps` `DevSecOps` `CyberSecurity` `Snyk` | [Markdown](posts/2024-12-24-devops-security-solutions-a-look-at-aqua-snyk-and-sonarqube.md) |
| 2024-12-20 | [Unlock the Potential of Container Orchestration Using Kubernetes and Docker](https://sishodiarobin.hashnode.dev/unlock-the-potential-of-container-orchestration-using-kubernetes-and-docker) | `DevOps` `Kubernetes` `Docker` `CloudComputing` | [Markdown](posts/2024-12-20-unlock-the-potential-of-container-orchestration-using-kubernetes-and-docker.md) |
| 2024-12-11 | [Comprehensive Guide to Top DevOps Tools: Prometheus, Grafana, and ELK Stack Explained](https://sishodiarobin.hashnode.dev/comprehensive-guide-to-top-devops-tools-prometheus-grafana-and-elk-stack-explained) | `DevOps` `Monitoring` `Logging` `Prometheus` | [Markdown](posts/2024-12-11-comprehensive-guide-to-top-devops-tools-prometheus-grafana-and-elk-stack-explained.md) |
| 2024-12-11 | [Advanced Git Commands and Best Practices for Efficient Version Control](https://sishodiarobin.hashnode.dev/advanced-git-commands-and-best-practices-for-efficient-version-control) | `Git` `VersionControl` `DevOps` `SoftwareDevelopment` | [Markdown](posts/2024-12-11-advanced-git-commands-and-best-practices-for-efficient-version-control.md) |
| 2024-12-11 | [A Comprehensive Guide to Infrastructure as Code with Terraform and Ansible](https://sishodiarobin.hashnode.dev/a-comprehensive-guide-to-infrastructure-as-code-with-terraform-and-ansible) | `DevOps` `InfrastructureAsCode` `Terraform` `Ansible` | [Markdown](posts/2024-12-11-a-comprehensive-guide-to-infrastructure-as-code-with-terraform-and-ansible.md) |
| 2024-12-10 | [Jenkins vs GitLab vs CircleCI: A Comprehensive CI/CD Tools Comparison](https://sishodiarobin.hashnode.dev/jenkins-vs-gitlab-vs-circleci-a-comprehensive-cicd-tools-comparison) | `DevOps` `CICD` `Jenkins` `GitLab` | [Markdown](posts/2024-12-10-jenkins-vs-gitlab-vs-circleci-a-comprehensive-cicd-tools-comparison.md) |
| 2024-12-08 | [Step-by-Step Guide: Terraform and Kubernetes Integration](https://sishodiarobin.hashnode.dev/step-by-step-guide-terraform-and-kubernetes-integration) | `DevOps` `Terraform` `Kubernetes` `CloudComputing` | [Markdown](posts/2024-12-08-step-by-step-guide-terraform-and-kubernetes-integration.md) |
| 2024-12-07 | [Unlocking the Power of Version Control: Essential Git Commands and Strategies for Successful Project Management](https://sishodiarobin.hashnode.dev/unlocking-the-power-of-version-control-essential-git-commands-and-strategies-for-successful-project-management) | `Git` `VersionControl` `DevOps` `CICD` | [Markdown](posts/2024-12-07-unlocking-the-power-of-version-control-essential-git-commands-and-strategies-for-successful-project-management.md) |
| 2024-12-06 | [Enhance DevOps Efficiency with Jenkins Shared Libraries](https://sishodiarobin.hashnode.dev/enhance-devops-efficiency-with-jenkins-shared-libraries) | `DevOps` `Jenkins` `CICD` `PipelineAutomation` | [Markdown](posts/2024-12-06-enhance-devops-efficiency-with-jenkins-shared-libraries.md) |
| 2024-12-05 | [💻Mastering Kubernetes Troubleshooting: 30 Essential Commands for Day-to-Day Operations 🚀](https://sishodiarobin.hashnode.dev/mastering-kubernetes-troubleshooting-30-essential-commands-for-day-to-day-operations) | `Kubernetes` `DevOps` `CloudComputing` `Troubleshooting` | [Markdown](posts/2024-12-05-mastering-kubernetes-troubleshooting-30-essential-commands-for-day-to-day-operations.md) |
| 2024-12-04 | [How AWS Lambda Eases Application Deployment with Serverless DevOps](https://sishodiarobin.hashnode.dev/how-aws-lambda-eases-application-deployment-with-serverless-devops) | `Serverless` `DevOps` `AWSLambda` `CloudComputing` | [Markdown](posts/2024-12-04-how-aws-lambda-eases-application-deployment-with-serverless-devops.md) |
| 2024-12-03 | [GitLab CI/CD Pipelines: Automate Everything and Streamline Your DevOps Workflows](https://sishodiarobin.hashnode.dev/gitlab-cicd-pipelines-automate-everything-and-streamline-your-devops-workflows) | `GitLab` `CICD` `DevOps` `Automation` | [Markdown](posts/2024-12-03-gitlab-cicd-pipelines-automate-everything-and-streamline-your-devops-workflows.md) |
| 2024-12-02 | [The Ultimate Guide to Easy EC2 Connectivity: SSH Access and Secure Communication](https://sishodiarobin.hashnode.dev/the-ultimate-guide-to-easy-ec2-connectivity-ssh-access-and-secure-communication) | `AWS` `EC2` `CloudComputing` `DevOps` | [Markdown](posts/2024-12-02-the-ultimate-guide-to-easy-ec2-connectivity-ssh-access-and-secure-communication.md) |
| 2024-11-29 | [Building a Solid Networking Foundation: The Ultimate Beginner's Guide🌐💻🔌](https://sishodiarobin.hashnode.dev/building-a-solid-networking-foundation-the-ultimate-beginners-guide) | `ComputerNetworking` `NetworkingBasics` `ITInfrastructure` `NetworkingDevices` | [Markdown](posts/2024-11-29-building-a-solid-networking-foundation-the-ultimate-beginners-guide.md) |

<sub>This index is generated automatically. Edits here will be overwritten.</sub>
