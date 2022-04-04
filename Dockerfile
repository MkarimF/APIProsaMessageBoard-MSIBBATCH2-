#Dockerfile , image, container

FROM python:3.8

ADD main.py .post

COPY requirements.txt requirements.txt

RUN pip install -r requirements.txt



COPY . .



CMD ["uvicorn","post.main:app","--host","0.0.0.0"]