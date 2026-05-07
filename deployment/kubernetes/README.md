# Kubernetes Deployment Code

## Tools

kind, kubectl, helm

## Kind

```
cat <<EOF | kind create cluster --config -
kind: Cluster
apiVersion: kind.x-k8s.io/v1alpha4
nodes:
- role: control-plane
  extraMounts:
  - containerPath: /var/lib/kubelet/config.json
    hostPath: /home/student/.docker/config.json
  extraPortMappings:
  - containerPort: 30000
    hostPort: 30000
  - containerPort: 30100
    hostPort: 30100
  - containerPort: 30200
    hostPort: 30200
  - containerPort: 30300
    hostPort: 30300
- role: worker
  extraMounts:
  - containerPath: /var/lib/kubelet/config.json
    hostPath: /home/student/.docker/config.json
- role: worker
  extraMounts:
  - containerPath: /var/lib/kubelet/config.json
    hostPath: /home/student/.docker/config.json
EOF
```

```
kubectl get nodes
```

```
NAME                 STATUS   ROLES           AGE   VERSION
kind-control-plane   Ready    control-plane   16m   v1.35.0
kind-worker          Ready    <none>          15m   v1.35.0
kind-worker2         Ready    <none>          15m   v1.35.0
```


## Model and Streamlit

```
kubectl apply -R -f deployment/kubernetes
```

## Prometheus Stack
```
helm repo add prometheus-community https://prometheus-community.github.io/helm-charts
helm repo update
```

```
helm upgrade prom prometheus-community/kube-prometheus-stack \
  --install \
  --namespace monitoring \
  --create-namespace \
  --set grafana.service.type=NodePort \
  --set grafana.service.nodePort=30200 \
  --set prometheus.service.type=NodePort \
  --set prometheus.service.nodePort=30300
```

```
helm list -n monitoring
```

```
NAME    NAMESPACE       REVISION        UPDATED                                 STATUS          CHART                           APP VERSION
prom    monitoring      1               2026-05-07 08:48:16.69556384 +0000 UTC  deployed        kube-prometheus-stack-84.5.0    v0.90.1 
```

## Cleanup

```
kubectl delete -R -f deployment/kubernetes
```

```
kind delete cluster
```
