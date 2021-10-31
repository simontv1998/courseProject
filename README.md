Mini Search Engine

Steps I took to run the client side app:
1) cd client_side_app
2) make sure django is installed in pip (pip install django)
3) python manage.py runserver
4) access localhost:8000 in a browser

Step I will use to connect to GCP:
1) docker build -t simontv1998/clientsideapp .
2) docker push simontv1998/clientsideapp
3) create a project called "min-search" in GCP
4) In cloud shell, docker pull simontv1998/clientsideapp
5) docker tag simontv1998/clientsideapp gcr.io/min-search/clientsideapp
6) docker push gcr.io/min-search/clientsideapp
7) Deploy the container to GKE via UI
8) Create services via UI
9) View my running application