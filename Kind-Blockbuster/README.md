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