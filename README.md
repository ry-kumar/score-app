| Step                 | Command                                            |
| -------------------- | -------------------------------------------------- |
| Create KIND cluster  | `kind create cluster --name score-api`             |
| Build Docker image   | `docker build -t score:v1 .`                       |
| Load image into KIND | `kind load docker-image score:v1 --name score-api` |
| Deploy app           | `kubectl apply -f score-k8s.yaml`                  |
| Verify pods          | `kubectl get pods -o wide`                         |
| Access app           | `http://localhost:30007` or via `port-forward`     |



Create the KIND cluster

Example:
```
kind create cluster --name score-api --config kind-config.yaml
```
Your kind-config.yaml can define multiple nodes if you want multi-node testing.

Build your Docker image
```
docker build -t score:v1 .
```
Make sure your Dockerfile starts FastAPI with 0.0.0.0:5000

Example CMD in Dockerfile:
```
uvicorn main:app --host 0.0.0.0 --port 5000
```


✅ Steps to Apply and Access

Load your image into KIND
```
kind load docker-image score:v1 --name score-api
```
Apply the YAML
```
kubectl apply -f score-k8s.yaml
```
Check pods
```
kubectl get pods -o wide
```
You should see Running with IP on one of the worker nodes.

Access your API locally
```
http://localhost:30007
```
FastAPI must be listening on 0.0.0.0:5000 inside the container.
In Dockerfile, your CMD should be:
```
uvicorn main:app --host 0.0.0.0 --port 5000
```
🔹 Optional — Port Forwarding (Even Cleaner)

Instead of NodePort, you can also do:
```
kubectl port-forward service/score-service 8080:80
```
Then open:
```
http://localhost:8080
```
This avoids choosing NodePort manually and is often preferred in CI/CD testing.



***********************************************************
-----------------------------------------------------------

🔹 Optional — Port Forwarding (Even Cleaner)

Instead of NodePort, you can also do:
```
kubectl port-forward service/score-service 8080:80
```
Then open:
```
http://localhost:8080
```
This avoids choosing NodePort manually and is often preferred in CI/CD testing.