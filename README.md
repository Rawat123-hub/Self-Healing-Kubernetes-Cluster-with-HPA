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
git clone https://github.com/Rawat123-hub/k8s-hpa-self-healing.git
cd k8s-hpa-self-healing
docker build -t self-healing-app .

