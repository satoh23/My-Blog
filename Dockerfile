FROM python:3.8
ENV PYTHONUNBUFFERD 1

WORKDIR /my_blog
ADD requirements.txt /my_blog/

RUN pip install -r requirements.txt
ADD . /my_blog/

EXPOSE 13500