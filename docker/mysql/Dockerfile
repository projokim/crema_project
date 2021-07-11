# FROM mysql:8.0.25
FROM mysql:5.7.34

# WORKDIR .

ENV TZ Asia/Seoul
# ENV MYSQL_HOST localhost
# ENV MYSQL_PORT 3306
ENV MYSQL_ROOT_PASSWORD datarize123
ENV MYSQL_DATABASE crema
ENV MYSQL_USER datarize
ENV MYSQL_PASSWORD datarize123

# 마운트는 안에 있는 것을 꺼내올 때만
VOLUME ["./db/conf.d", "/etc/mysql/conf.d"]
VOLUME ["./db/data", "/var/lib/mysql"]

# 소켓 에러를 해결하기 위한 시도
# COPY create_id.sql /

COPY ./db/crema.sql /
