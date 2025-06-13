#!/bin/bash

# chmod +x reload.sh
# ./reload.sh

echo "🔧 Cambiando al entorno Docker de Minikube..."
eval $(minikube docker-env)

echo "🐳 Construyendo las imágenes Docker con tag 'festival-app'..."
docker build -t festival-app .

echo "🚀 Reiniciando el deployment 'catbox' en Kubernetes..."
kubectl rollout restart deployment/festival-app
kubectl rollout restart deployment/festival-client

echo "✅ ¡Actualización completada!"