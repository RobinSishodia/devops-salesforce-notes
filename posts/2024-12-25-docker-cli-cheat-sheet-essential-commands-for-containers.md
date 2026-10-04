---
title: "Docker CLI Cheat Sheet: Essential Commands for Containers"
date: 2024-12-25T12:45:27+00:00
canonical_url: https://sishodiarobin.hashnode.dev/docker-cli-cheat-sheet-essential-commands-for-containers
cover_image: https://cdn.hashnode.com/res/hashnode/image/upload/v1735035924000/23174c08-66e8-431f-8cff-fe671d635bb7.webp
tags: ["Docker", "DevOps", "Containerization", "DockerCLI", "TechTips", "DevOpsEngineer", "SoftwareDevelopment", "Containers", "CloudComputing", "TechCommunity"]
brief: "In today's software development landscape, Docker is an essential tool for creating, deploying, and running applications smoothly across various environments. The Docker Command-Line Interface (CLI) offers a robust method to work with Docker, manage ..."
---

> Originally published at [sishodiarobin.hashnode.dev](https://sishodiarobin.hashnode.dev/docker-cli-cheat-sheet-essential-commands-for-containers). This is an automated backup; read and comment on the blog.

In today's software development landscape, **Docker** is an essential tool for creating, deploying, and running applications smoothly across various environments. The **Docker Command-Line Interface (CLI)** offers a robust method to work with Docker, manage containers, and efficiently organize your applications. This cheat sheet showcases the **key Docker commands** that every developer and DevOps engineer should be familiar with.

---

## **1. Docker Basics**

- **Check Docker Version:**

- ```
    docker --version
    docker version
  ```
- **Show System-Wide Information:**

  ```
    docker info
  ```
- **Log in to Docker Hub:**

  ```
    docker login
  ```
- **Explore All Commands and Options:**

  ```
    docker --help
  ```

---

## **2.Working with Images**

- **Search for an Image on Docker Hub:**

- ```
    docker search <image-name>
  ```
- **Pull an Image from Docker Hub:**

  ```
    docker pull <image-name>
  ```
- **List Downloaded Images:**

  ```
    docker images
  ```
- **Remove an Image:**

  ```
    docker rmi <image-id>
  ```

---

## **3. Managing Containers**

- **Create and Start a Container:**

  ```
    docker run -it <image-name>
  ```
- **Run Container in Detached Mode:**

  ```
    docker run -d <image-name>
  ```
- **List Running Containers:**

  ```
    docker ps
  ```
- **List All Containers (including stopped ones):**

  ```
    docker ps -a
  ```
- **Stop a Running Container:**

  ```
    docker stop <container-id>
  ```
- **Start a Stopped Container:**

  ```
    docker start <container-id>
  ```
- **Remove a Container:**

  ```
    docker rm <container-id>
  ```

---

## **4. Accessing Containers**

- **Access Container Shell:**

  ```
    docker exec -it <container-id> /bin/bash
  ```
- **Copy Files from Container to Host:**

  ```
    docker cp <container-id>:<source-path> <destination-path>
  ```
- **View Container Logs:**

  ```
    docker logs <container-id>
  ```

---

## **5. Managing Docker Volumes**

- **List Docker Volumes:**

  ```
    docker volume ls
  ```
- **Create a Volume:**

  ```
    docker volume create <volume-name>
  ```
- **Inspect a Volume:**

  ```
    docker volume inspect <volume-name>
  ```
- **Remove a Volume:**

  ```
    docker volume rm <volume-name>
  ```

---

## **6. Docker Networks**

- **List Networks:**

  ```
    docker network ls
  ```
- **Create a Network:**

  ```
    docker network create <network-name>
  ```
- **Connect a Container to a Network:**

  ```
    docker network connect <network-name> <container-id>
  ```
- **Disconnect a Container from a Network:**

  ```
    docker network disconnect <network-name> <container-id>
  ```

---

## **7. Docker Compose**

- **Start Services in Detached Mode:**

  ```
    docker-compose up -d
  ```
- **Stop Services:**

  ```
    docker-compose down
  ```
- **View Service Logs:**

  ```
    docker-compose logs
  ```

---

## **8. Docker Cleanup**

- **Remove Unused Data:**

  ```
    docker system prune
  ```
- **Remove All Unused Images:**

  ```
    docker image prune -a
  ```
- **Remove All Stopped Containers:**

  ```
    docker container prune
  ```

---

## **Conclusion**

The Docker CLI is a powerful tool that makes managing containers easier, streamlining workflows and ensuring consistency. Whether you're just starting or you're a seasoned engineer, keeping this **cheat sheet** nearby will help you manage your containers with confidence. 🚀

Dive into these commands, try them out, and incorporate them into your daily routines to fully leverage Docker's potential!
