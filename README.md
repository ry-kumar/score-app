
# 2. Save it to a file

docker save score-app:v2 -o score-app-v2.tar



# 3. Load it into Minikube

minikube image load score-app-v2.tar

 
docker build -t score-app:v1 .

minikube service score-service -n dev

kubectl set image deployment/score-app score-app=score-app:v2 -n dev


Create a Staging environment. 

kubectl create namespace staging

Creating a minikube service for staging. 
minikube service score-service -n staging



 956  docker build . 
  957  docker run -p 5000:5000 score_api
  958  minikube image load score-app-v2.tar
  959  kubectl set image deployment/score-app score-app=score-app:v2 -n dev
  960  kubectl set image deployment/score-app score-app=score-app:v2



  | Tool     | What You Do                               |
| -------- | ----------------------------------------- |
| Minikube | `eval $(minikube docker-env)` → build     |
| kind     | `docker build` → `kind load docker-image` |




kind create cluster --name score-api --config kind-3node.yaml 

kubectl config current-context
kind-score-api

yaswanthkumar@Yaswanths-MacBook-Pro score_api % kubectl config get-contexts

kubectl config get-contexts
CURRENT   NAME                                                  CLUSTER                                               AUTHINFO                                              NAMESPACE
          Democluster                                           Democluster                                           Democluster                                           default
          arn:aws:eks:us-east-1:799363008941:cluster/ToDo-App   arn:aws:eks:us-east-1:799363008941:cluster/ToDo-App   arn:aws:eks:us-east-1:799363008941:cluster/ToDo-App   
          docker-desktop                                        docker-desktop                                        docker-desktop                                        
          kind-dme-container-in-k8s-pod-2                       kind-dme-container-in-k8s-pod-2                       kind-dme-container-in-k8s-pod-2                       
          kind-nginx-ingress                                    kind-nginx-ingress                                    kind-nginx-ingress                                    
*         kind-score-api                                        kind-score-api                                        kind-score-api                                        
          minikube                                              minikube                                              minikube                                              default
          practice-cluster                                      practice-cluster                                      practice-cluster                                      default

