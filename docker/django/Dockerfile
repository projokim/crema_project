FROM python:3.9.5-buster

ENV PYTHONUNBUFFERED 1
# ENV DJANGO_DEBUG True
# ENV DJANGO_DB_HOST=mysqldb
# ENV DJANGO_DB_PORT=3306
# ENV DJANGO_DB_USERNAME=root
# ENV DJANGO_DB_PASSWORD=datarize123
# WORKDIR은 RUN, CMD, ENTRYPOINT의 명령이 실행될 디렉터리
# WORKDIR .
COPY requirements.txt /
RUN pip install -r requirements.txt

RUN mkdir ./api
COPY ./api /api
# COPY /Users/juwonkim/Datarize/CREMA/api /

CMD python3 /api/manage.py runserver 0:8000
 