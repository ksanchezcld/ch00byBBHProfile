FROM ubuntu:kinetic
RUN apt-get update -y \
    #&& apt-transport-https \
    && apt-get install -y tree \
    && apt-get install -y vim \
    && apt-get install -y python3.8 \
    && apt-get install -y python3-pip \
    && apt-get install -y git \
    && apt-get install -y apt-utils \
    && rm -rf /root/ch00byBBHProfile/ \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /root/
RUN git clone https://github.com/ksanchezcld/ch00byBBHProfile.git
RUN cd /root/ch00byBBHProfile/
#WORKDIR /root/ch00byBBHProfile/
RUN python3 /root/ch00byBBHProfile/ch00byBBHEnvSetup.py
#ENTRYPOINT ["python3", "ch00byBBHEnvSetup.py"]
#tree -L 2 /root/BBH
