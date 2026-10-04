---
title: "💻Mastering Kubernetes Troubleshooting: 30 Essential Commands for Day-to-Day Operations 🚀"
date: 2024-12-05T18:19:06+00:00
canonical_url: https://sishodiarobin.hashnode.dev/mastering-kubernetes-troubleshooting-30-essential-commands-for-day-to-day-operations
cover_image: https://cdn.hashnode.com/res/hashnode/image/upload/v1733422485727/a0b240c8-5d78-48de-baef-5e05406894ed.png
tags: ["Kubernetes", "DevOps", "CloudComputing", "Troubleshooting", "Automation", "TechTips", "CICD", "OpenSource", "ContainerOrchestration", "InfrastructureAsCode", "K8sInsights", "TechInnovation", "ITOperations", "ClusterManagement", "LearnDevOps"]
brief: "Kubernetes, the powerful container orchestration platform, is the backbone of modern cloud-native applications. However, its complexity can be overwhelming when troubleshooting issues. Whether you're dealing with pod failures, network issues, or scal..."
---

> Originally published at [sishodiarobin.hashnode.dev](https://sishodiarobin.hashnode.dev/mastering-kubernetes-troubleshooting-30-essential-commands-for-day-to-day-operations). This is an automated backup; read and comment on the blog.

Kubernetes, the powerful container orchestration platform, is the backbone of modern cloud-native applications. However, its complexity can be overwhelming when troubleshooting issues. Whether you're dealing with pod failures, network issues, or scaling challenges, knowing the right commands is crucial to keep your cluster running smoothly.

This article highlights **30 essential Kubernetes troubleshooting commands** every DevOps engineer and administrator should master to streamline daily operations.

---

### **1. Cluster Information and Health Checks**

Start by ensuring the health and status of your Kubernetes cluster.

1. **Get cluster information**

   ```
    kubectl cluster-info
   ```

   Displays essential details about your cluster, including the API server and endpoints.
2. **Check cluster nodes**

   ```
    kubectl get nodes
   ```

   Lists all nodes in the cluster and their statuses.
3. **Detailed node status**

   ```
    kubectl describe node <node-name>
   ```

   Provides detailed information about a specific node, including resource allocation and issues.
4. **Check cluster events**

   ```
    kubectl get events --sort-by='.metadata.creationTimestamp'
   ```

   View the latest cluster-wide events for identifying potential problems.

---

### **2. Pod Management and Debugging**

5. **List all pods**

   ```
    kubectl get pods -A
   ```

   Displays pods across all namespaces to identify issues at a glance.
6. **Detailed pod information**

   ```
    kubectl describe pod <pod-name>
   ```

   Offers a detailed breakdown of a pod’s configuration and current state.
7. **View pod logs**

   ```
    kubectl logs <pod-name>
   ```

   Access logs to debug application-level issues.
8. **Stream pod logs**

   ```
    kubectl logs -f <pod-name>
   ```

   Continuously stream logs for real-time monitoring.
9. **Execute commands in a pod**

   ```
    kubectl exec -it <pod-name> -- /bin/bash
   ```

   Access the shell of a running container for troubleshooting.
10. **Check pod resource usage**

```
kubectl top pod <pod-name>
```

Displays CPU and memory usage for a pod.

---

### **3. Network and Connectivity**

11. **Inspect services**

```
kubectl get svc
```

Lists all services to ensure proper exposure and routing of applications.

12. **Debug service issues**

```
kubectl describe svc <service-name>
```

Provides details about a specific service, including associated endpoints.

13. **Test DNS resolution**

```
kubectl exec -it <pod-name> -- nslookup <service-name>
```

Check if DNS resolution is working within the cluster.

14. **Inspect network policies**

```
kubectl get networkpolicy
```

Ensures proper access control between pods and services.

15. **Trace service endpoints**

```
kubectl get endpoints <service-name>
```

Validates the service is mapping to the correct pods.

---

### **4. Deployment and Replica Management**

16. **List deployments**

```
kubectl get deployments
```

Ensures deployments are running as expected.

17. **Inspect deployment status**

```
kubectl describe deployment <deployment-name>
```

Provides details about replica counts and issues during updates.

18. **Scale a deployment**

```
kubectl scale deployment <deployment-name> --replicas=<number>
```

Adjust the number of replicas to handle workload demands.

19. **Rollback a deployment**

```
kubectl rollout undo deployment <deployment-name>
```

Reverts to the previous stable deployment state.

20. **Check rollout status**

```
kubectl rollout status deployment <deployment-name>
```

Ensures the deployment update is proceeding as expected.

---

### **5. Persistent Volumes and Storage**

21. **List persistent volumes**

```
kubectl get pv
```

View the status of persistent volumes in the cluster.

22. **Inspect persistent volume claims**

```
kubectl get pvc
```

Verifies if pods are correctly bound to storage.

23. **Describe a persistent volume**

```
kubectl describe pv <pv-name>
```

Provides details about storage capacity and access modes.

---

### **6. Resource Monitoring and Usage**

24. **Check resource usage by node**

```
kubectl top node
```

Displays CPU and memory usage across all nodes.

25. **Check pod resource limits**

```
kubectl describe pod <pod-name> | grep -i "limits"
```

Validates resource limits defined for pods.

26. **Monitor resource quotas**

```
kubectl get resourcequotas
```

Ensures namespaces are within resource allocation limits.

---

### **7. Configuration and Secrets**

27. **List config maps**

```
kubectl get configmaps
```

Lists all ConfigMaps in the current namespace.

28. **Inspect secrets**

```
kubectl get secrets
```

Ensures secure information is properly configured and accessible.

---

### **8. Miscellaneous Utilities**

29. **Dry-run a deployment**

```
kubectl apply -f <file-name.yaml> --dry-run=client
```

Tests changes without applying them to the cluster.

30. **Delete a problematic resource**

```
kubectl delete pod <pod-name>
```

Removes malfunctioning pods to free up resources.

---

### **Conclusion**

Troubleshooting Kubernetes effectively involves understanding its architecture and mastering key commands. The 30 commands we've discussed cover many scenarios, helping you diagnose and fix issues efficiently.

As you get more comfortable with these commands, you'll notice a significant improvement in managing complex Kubernetes environments. Keep this list handy, practice often, and enhance your DevOps workflow!

**What are your favorite Kubernetes troubleshooting commands? Share them in the comments!** 🚀
