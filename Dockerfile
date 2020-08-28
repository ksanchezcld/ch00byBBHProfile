FROM alpine:latest
RUN apk update
RUN apk add \
git \
RUN rm -rf /var/cache/apk/*
WORKDIR /root
RUN git clone https://github.com/ksanchezcld/ch00byBBHProfile.git
WORKDIR /root/ch00byBBHProfile/
RUN pip3 install wheel
RUN pip3 install --upgrade pip
RUN pip3 install -r requirements.txt
ENTRYPOINT ["python3", "ch00byBBHEnvSetup.py"]