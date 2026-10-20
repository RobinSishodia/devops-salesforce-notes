---
title: "Dockerfile Best Practices: Smaller, Faster and Safer Images"
date: 2026-10-06T18:47:39+00:00
canonical_url: https://sishodiarobin.hashnode.dev/dockerfile-best-practices-smaller-faster-and-safer-images
cover_image: https://cdn.hashnode.com/uploads/covers/6693dc4e158429a5c6ab492f/44a6e4c1-f2f0-4211-92b2-e42fc15d29e8.png
tags: ["Docker", "containers", "Devops", "best practices"]
brief: "Practical Dockerfile best practices: multi-stage builds, layer caching, small base images, non-root users and .dockerignore, with examples."
---

> Originally published at [sishodiarobin.hashnode.dev](https://sishodiarobin.hashnode.dev/dockerfile-best-practices-smaller-faster-and-safer-images). This is an automated backup; read and comment on the blog.

Writing a Dockerfile that *works* is easy. Writing one that builds fast, produces a small image and doesn't run as root takes a few habits. Here are the ones that made the biggest difference for me.

## 1. Start from a small, specific base image

```dockerfile
# Avoid
FROM node:latest

# Prefer
FROM node:20-alpine
```

- **Pin a version.** `latest` changes under you and makes builds unreproducible.
- **Use slim or alpine variants** when your app supports them. Smaller images pull faster and have fewer packages to patch.
- For compiled languages, consider **distroless** or `scratch` for the final image.

## 2. Order instructions for layer caching

Docker caches each layer. If a layer changes, every layer after it is rebuilt. Put things that change rarely first:

```dockerfile
WORKDIR /app
COPY package*.json ./
RUN npm ci --omit=dev
COPY . .
```

Now changing your source code doesn't re-run `npm ci`. Dependencies are only reinstalled when `package.json` changes.

## 3. Use multi-stage builds

Build tools don't belong in production images. A multi-stage build compiles in one stage and copies only the output into a clean final stage:

```dockerfile
# Build stage
FROM node:20-alpine AS build
WORKDIR /app
COPY package*.json ./
RUN npm ci
COPY . .
RUN npm run build

# Runtime stage
FROM node:20-alpine
WORKDIR /app
ENV NODE_ENV=production
COPY package*.json ./
RUN npm ci --omit=dev
COPY --from=build /app/dist ./dist
USER node
EXPOSE 3000
CMD ["node", "dist/server.js"]
```

The final image contains no dev dependencies, compilers or source files it doesn't need.

## 4. Add a .dockerignore

Without it, `COPY . .` sends everything to the build context, including `node_modules`, `.git` and possibly secrets.

```
node_modules
.git
.env
*.log
dist
```

This speeds up builds and keeps sensitive files out of the image.

## 5. Don't run as root

Containers run as root by default. If an attacker breaks out of your app, root makes it worse. Many official images include a non-root user (`node` in Node images). Otherwise create one:

```dockerfile
RUN addgroup -S app && adduser -S app -G app
USER app
```

## 6. Combine and clean up RUN steps

Each `RUN` creates a layer. Clean up in the **same** layer you create files in, or the files still take space:

```dockerfile
RUN apt-get update \
    && apt-get install -y --no-install-recommends curl \
    && rm -rf /var/lib/apt/lists/*
```

## 7. Never bake secrets into images

Anything in an image layer can be extracted, even if a later layer deletes it. Pass secrets at runtime (environment variables from a secrets manager, mounted files) or use BuildKit's `--mount=type=secret` for build-time secrets.

## 8. Prefer exec-form CMD and ENTRYPOINT

```dockerfile
CMD ["node", "server.js"]   # exec form: receives signals properly
CMD node server.js          # shell form: wraps in /bin/sh
```

The exec form lets your process receive `SIGTERM` directly, so containers stop cleanly.

## 9. Add a HEALTHCHECK (when not using an orchestrator's probes)

```dockerfile
HEALTHCHECK --interval=30s --timeout=3s \
  CMD wget -qO- http://localhost:3000/health || exit 1
```

On Kubernetes you'd use liveness and readiness probes instead.

## 10. Scan your images

Tools like **Trivy**, **Docker Scout** or **Snyk** find known vulnerabilities in base images and dependencies. Run them in CI so problems are caught before deployment.

## Quick checklist

- Pinned, minimal base image
- Dependencies copied and installed before source code
- Multi-stage build
- `.dockerignore` in place
- Non-root `USER`
- No secrets in layers
- Image scanned in CI

Small changes, but together they often cut image size by more than half and make builds noticeably faster.
