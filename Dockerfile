#Dockerfile , image, container

FROM python:3.8

ADD main.py .post

RUN pip install requirements.txt

COPY post/ /post



CMD ["uvicorn","post.main:app","--host","0.0.0.0"]