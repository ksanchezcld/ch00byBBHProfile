FROM alpine:latest
RUN apk update
RUN apk add \
git \
RUN rm -rf /var/cache/apk/*
WORKDIR /root
RUN git clone https://github.com/thewhiteh4t/finalrecon.git
WORKDIR /root/bbhprofile/
RUN pip3 install wheel
RUN pip3 install --upgrade pip
RUN pip3 install -r requirements.txt
ENTRYPOINT ["python3", "finalrecon.py"]