#!/bin/bash

# chmod +x refresh.sh
# ./refresh.sh

echo "🔧 Cambiando al entorno Docker de Minikube..."
eval $(minikube docker-env)

echo "🐳 Construyendo la imagen Docker con tag 'catbox'..."
docker build -t catbox .

echo "🚀 Reiniciando el deployment 'catbox' en Kubernetes..."
kubectl rollout restart deployment/catbox

echo "✅ ¡Actualización completada!"