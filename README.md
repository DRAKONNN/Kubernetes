KUBERNETES
==============
**Kubernetes** (often shortened to **K8s**) is an open-source container orchestration system. It automates the deployment, scaling, and management of containerized applications, essentially acting as a conductor for your applications, especially those composed of many individual containerized components. 
### Key Features and Benefits:
- **Automation**: Kubernetes automates tasks like deployment, scaling, and management, making it easier to manage containerized applications. 

- **Container Orchestration**: It groups containers into logical units called Pods, simplifying management and discovery.

- **Scalability**: Kubernetes allows you to easily scale your applications up or down by replicating containers across multiple hosts.

- **Resilience**: It restarts failed containers, replaces faulty Pods, and can automatically scale resources to handle increased demand.

- **Service Discovery**: It provides ways for containers to discover each other and communicate, enabling the creation of distributed applications.

---
I recommend **Minikube** to start playing with Kubernetes on your virtual machine. To do this you have to install it and **Kubectl** too, which will serve as the container orchestrator:
- ### [Install Minikube](https://minikube.sigs.k8s.io/docs/start/?arch=%2Flinux%2Fx86-64%2Fstable%2Fdebian+package#Service)
- ### [Install Kubectl](https://kubernetes.io/docs/tasks/tools/)


---
*Created and documented by [DRAKONNN](https://github.com/DRAKONNN)*