#!/bin/bash

# chmod +x reload.sh
# ./reload.sh

echo "🔧 Cambiando al entorno Docker de Minikube..."
eval $(minikube docker-env)

echo "🐳 Construyendo las imágenes Docker con tag 'catbox' y 'dogbox'..."
docker build -f Dockerfile.cat -t catbox .
docker build -f Dockerfile.dog -t dogbox .

echo "🚀 Reiniciando el deployment 'catbox' en Kubernetes..."
kubectl rollout restart deployment/catbox
kubectl rollout restart deployment/dogbox

echo "✅ ¡Actualización completada!"