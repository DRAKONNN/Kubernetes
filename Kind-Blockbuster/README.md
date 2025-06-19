📺BLOCKBUSTERS
===
## 1. Install Kind
```
$ curl -Lo ./kind https://kind.sigs.k8s.io/dl/v0.22.0/kind-linux-amd64
$ chmod +x ./kind
$ sudo mv ./kind /usr/local/bin/kind
```
## 2. Create cluster
```
$ kind create cluster --name blockbuster --config cluster-blockbuster.yaml
```
## 3. Build docker image and load
```
$ docker build -t blockbuster:latest .
$ kind load docker-image blockbuster:latest --name blockbuster
```
## 4. Apply deployment and service
```
$ kubectl apply -f k8s/
```


# Artillery
## 1. Install Metrics Server for Kind
```
# Aplicar la configuración base de Metrics Server
$ kubectl apply -f https://github.com/kubernetes-sigs/metrics-server/releases/latest/download/components.yaml

# Aplicar parche necesario para Kind
$ kubectl patch deployment metrics-server -n kube-system --type=json \
  -p='[{"op": "add", "path": "/spec/template/spec/containers/0/args/-", "value": "--kubelet-insecure-tls"}]'
```
```
$ watch kubectl top pods
```
## 2. Maintain port-forwarding
```
kubectl port-forward svc/<nombre-del-servicio> 8080:80
```
## 3. Execute Artillery
```
artillery run blockbuster-load-test.yml
```