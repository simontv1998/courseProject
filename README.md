Mini Search Engine

Steps I took to Dockerize and run the client side app:
1) cd client_side_app
2) make sure django is installed in pip (pip install django)
3) python manage.py runserver
4) access localhost:8000 in a browser

Step to deploy server side app to GCP cluster:
1) docker build -t simontv1998/server_side_app .
2) docker push simontv1998/server_side_app
3) create a project called "min-search-sever-side-app" in GCP
4) In cloud shell, docker pull simontv1998/server_side_app
5) docker tag simontv1998/server_side_app gcr.io/min-search-sever-side-app/server_side_app
6) docker push gcr.io/min-search-sever-side-app/server_side_app
7) Deploy the container to GKE via UI
8) Create services via UI
9) View my running application