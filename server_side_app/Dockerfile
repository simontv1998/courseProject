FROM python:3.8.9

WORKDIR /app

COPY . /app

RUN pip install -r requirements.txt

EXPOSE 30000

ENV FLASK_RUN_PORT=30000

CMD ["flask","run","--host=0.0.0.0"]