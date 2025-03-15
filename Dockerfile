# Используем Python 3.11 (стабильный) на базе Alpine 3.17
FROM python:3.11-alpine3.17

# Обновляем apk-репозитории
RUN apk update && apk add --no-cache chromium chromium-chromedriver tzdata gcompat gcc musl-dev python3-dev libffi-dev openssl-dev cargo openjdk11-jre curl tar

# Устанавливаем Allure
RUN curl -o allure-2.13.8.tgz -Ls https://repo.maven.apache.org/maven2/io/qameta/allure/allure-commandline/2.13.8/allure-commandline-2.13.8.tgz && \
    tar -zxvf allure-2.13.8.tgz -C /opt/ && \
    ln -s /opt/allure-2.13.8/bin/allure /usr/bin/allure && \
    rm -f allure-2.13.8.tgz

# Устанавливаем рабочую директорию
WORKDIR /usr/workspace

# Копируем файлы проекта
COPY ./requirements.txt /usr/workspace/requirements.txt

# Обновляем pip и устанавливаем зависимости
RUN python3 -m ensurepip --upgrade && \
    python3 -m pip install --upgrade "pip<24" setuptools wheel && \
    pip install --no-cache-dir -r requirements.txt
