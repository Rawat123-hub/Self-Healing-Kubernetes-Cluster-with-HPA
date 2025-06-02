# 🤖 Self-Healing Kubernetes Cluster with HPA

## 📌 Overview
This project showcases Kubernetes' ability to self-heal and auto-scale applications. A demo app is deployed with liveness/readiness probes and a Horizontal Pod Autoscaler (HPA) that reacts to CPU load using metrics-server.

## 🛠️ Technologies
- Kubernetes (Minikube or EKS)
- Docker
- HPA, Probes
- K6 (for load testing)
- metrics-server

## ⚙️ Setup Instructions

### 1. Clone & Build
```bash
git clone https://github.com/Rawat123-hub/Self-Healing-Kubernetes-Cluster-with-HPA.git
cd Self-Healing-Kubernetes-Cluster-with-HPA
docker build -t self-healing-app .
```

### 2. Apply Kubernetes Manifests

Apply the manifests to deploy the app, expose the service, and configure autoscaling:

```bash
kubectl apply -f deployment.yaml
kubectl apply -f service.yaml
kubectl apply -f hpa.yaml
```

📌 **Note**: Ensure the `metrics-server` is installed and running:

```bash
kubectl apply -f https://github.com/kubernetes-sigs/metrics-server/releases/latest/download/components.yaml
```

You can verify the setup with:
```bash
kubectl get pods
kubectl get svc
kubectl get hpa
```

### 3. Load Testing

Use [K6](https://k6.io/) to simulate traffic and CPU load:

```bash
k6 run load-test/test.js
```

Monitor scaling:
```bash
kubectl get hpa --watch
```

## 📊 Expected Results
- Pods restart if health checks fail (self-healing).
- Pods scale up/down based on CPU usage.
