#Dockerfile , image, container

FROM python:3.8.12

COPY requirements.txt requirements.txt

RUN pip install -r requirements.txt

COPY post post

CMD ["uvicorn","post.main:app","--host","0.0.0.0"]