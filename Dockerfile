# Используем Python 3.12 на базе Alpine 3.17
FROM python:3.12.0a4-alpine3.17

# Обновляем apk-репозитории
RUN echo "http://dl-cdn.alpinelinux.org/alpine/v3.17/main" >> /etc/apk/repositories && \
    echo "http://dl-cdn.alpinelinux.org/alpine/v3.17/community" >> /etc/apk/repositories && \
    apk update

# Устанавливаем нужные пакеты: Chromium, Chromedriver, tzdata
RUN apk add --no-cache chromium chromium-chromedriver tzdata

# Устанавливаем glibc (исправленные ссылки)
RUN wget -q -O /etc/apk/keys/sgerrand.rsa.pub https://alpine-pkgs.sgerrand.com/sgerrand.rsa.pub && \
    wget https://github.com/sgerrand/alpine-pkg-glibc/releases/download/2.32-r0/glibc-2.32-r0.apk && \
    wget https://github.com/sgerrand/alpine-pkg-glibc/releases/download/2.32-r0/glibc-bin-2.32-r0.apk && \
    apk add --no-cache glibc-2.32-r0.apk glibc-bin-2.32-r0.apk && \
    rm -f glibc-2.32-r0.apk glibc-bin-2.32-r0.apk

# Устанавливаем OpenJDK 11, curl и tar
RUN apk add --no-cache openjdk11-jre curl tar

# Устанавливаем Allure
RUN curl -o allure-2.13.8.tgz -Ls https://repo.maven.apache.org/maven2/io/qameta/allure/allure-commandline/2.13.8/allure-commandline-2.13.8.tgz && \
    tar -zxvf allure-2.13.8.tgz -C /opt/ && \
    ln -s /opt/allure-2.13.8/bin/allure /usr/bin/allure && \
    rm -f allure-2.13.8.tgz

# Устанавливаем рабочую директорию
WORKDIR /usr/workspace

# Копируем файлы проекта
COPY ./requirements.txt /usr/workspace/requirements.txt

# Устанавливаем зависимости Python
RUN pip install --no-cache-dir -r requirements.txt
