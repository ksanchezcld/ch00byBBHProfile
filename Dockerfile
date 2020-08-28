#FROM alpine:latest
FROM ubuntu:latest
#RUN apk update
#RUN apk add \

RUN apt-get update -y \
    #&& apt-transport-https \
    && apt-get install -y python3.8 \
    && apt-get install -y python3-pip \
    && apt-get install -y git \
    && apt-get install -y apt-utils \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /root
RUN git clone https://github.com/ksanchezcld/ch00byBBHProfile.git
RUN cd /root/ch00byBBHProfile/
WORKDIR /root/ch00byBBHProfile/
#RUN pip3 install --upgrade pip \
#    && pyyaml \
#    && awscli \
#    && pymongo \
#    && xmltodict \
#    && requests \
#    && tldextract \
#    && certstream \
#    && url \
#    && fuzzywuzzy \
#    && pycryptodomex
#RUN pip3 install --no-cache-dir -r requirements.txt
ENTRYPOINT ["python3", "ch00byBBHEnvSetup.py"]