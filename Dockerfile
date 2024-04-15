FROM ubuntu

COPY . /home/Desktop/forum
WORKDIR /home/Desktop/forum

RUN apt-get update && apt-get install -y python3 && apt install -y python3-psycopg2 && apt-get install -y python3-flask && apt-get install -y gunicorn3

ENTRYPOINT ["bash", "python3", "app/app.py"]
