FROM python:3.8.9

COPY . /app

WORKDIR /app

RUN pip install -r requirements.txt

EXPOSE 8000

ENV SERVER_SIDE_APP_IP="http://104.154.118.228"

ENV SERVER_SIDE_APP_PORT=30000

CMD ["python","manage.py","runserver","0.0.0.0:8000"]