Mini Search Engine

Video:
Code WalkThrough + Demo https://www.youtube.com/watch?v=8qslW7UbN8A
How I run my apps https://www.youtube.com/watch?v=HsdnY8mkIvQ

Step to deploy server side app to GCP cluster:
1) cd server_side_app
2) docker build -t simontv1998/server_side_app .
3) docker push simontv1998/server_side_app
4) create a project called "min-search-sever-side-app" in GCP
5) In cloud shell, docker pull simontv1998/server_side_app
6) docker tag simontv1998/server_side_app gcr.io/min-search-sever-side-app/server_side_app
7) docker push gcr.io/min-search-sever-side-app/server_side_app
8) Create a cluster with 
9) Deploy the container to GKE via UI
10) Check cluster status
11) Create ingress services via UI to allow incoming traffic to access port 30000(where flask app runs)
12) Copy the external load balancer's endpoint/external ip and set it as the environment variable "SERVER_SIDE_IP" on client side

Steps I took to Dockerize and run the client side app:
1) cd client_side_app
2) docker build -t simontv1998/client_side_app .
3) docker push simontv1998/client_side_app (optional)
4) docker run -p 8000:8000 simontv1998/client_side_app
5) access localhost:8000 in a browser
