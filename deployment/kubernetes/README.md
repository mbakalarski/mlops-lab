# Kubernetes Deployment Code

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
kubectl apply -R -f deployment/kubernetes
```

```
kubectl delete -R -f deployment/kubernetes
```

```
kind delete cluster
```
