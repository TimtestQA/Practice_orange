FROM python:3.12.0a4-alpine3.17

RUN echo "http://dl-4.alpinelinux.org/alpine/v3.14/main" >> /etc/apk/repositories && \
    echo "http://dl-4.alpinelinux.org/alpine/v3.14/community" >> /etc/apk/repositories && \

 RUN apk update
 RUN apk add --no-cache chromium chromium-chromedriver tzdata

 #get all prerequisites

 RUN wget -q -0 /et/apk/keys/sgerrand.rsa.pub https://alpine-pkgs.sgerrand.com/sgerrand.rsa.pub
 RUN wget https//github.com/sgerrand/alpine-pkg-glibc/releases/download/2.32-r0/glibc-2.32-r0.apk
 RUN wget https//github.com/sgerrand/alpine-pkg-glibc/releases/download/2.32-r0/glibc-bin-2.32-r0.apk

 RUN apk update && \
     apk openjdk11-jre curl tar && \
     curl -o allure-2.13.8.tgz -Ls https://repo.maven.apache.org/maven2/io/qameta/allure/allure-commandline/2.13.8/allure-commandline-2.13.8.tgz && \
     tar -zxvf allure-2.13.8.tgz -C /opt/ && \
     ln -s /opt/allure-2.13.8/bin/allure /usr/bin/allure && \
     rm allure-2.13.8.tgz

 WORKDIR /usr/workspace

 COPY ./requirements.txt    /usr/workspace/requirements.txt

 RUN pip install -r requirements.txt
