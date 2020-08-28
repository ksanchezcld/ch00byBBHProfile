#FROM alpine:latest
FROM ubuntu:latest
#RUN apk update
#RUN apk add \

RUN apt-get update -y && \
    apt-get install -y python3.8 \
    && apt-get install pip3 \
    && apt-get git

RUN rm -rf /var/cache/apk/*
WORKDIR /root
RUN git clone https://github.com/ksanchezcld/ch00byBBHProfile.git
WORKDIR /root/ch00byBBHProfile/
RUN pip3 install --upgrade pip
RUN pip3 install -r requirements.txt
ENTRYPOINT ["python3", "ch00byBBHEnvSetup.py"]