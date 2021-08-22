FROM python:3.7.11-slim
MAINTAINER kshitijkamlakar@gmail.com 
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
WORKDIR /usr/src/app
RUN pip install --upgrade pip
#RUN apk add --update --no-cache postgresql-client
#RUN apk add --update --no-cache --virtual .tmp-build-deps gcc libc-dev linux-headers postgresql-dev 
COPY ./requirements.txt /usr/src/app
COPY . /usr/src/app
RUN pip install psycopg2-binary
RUN pip install -r requirements.txt
EXPOSE 8000
CMD [ "python", "./manage.py", "runserver", "0.0.0.0:8000"]