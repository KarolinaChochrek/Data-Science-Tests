FROM jenkins/ssh-agent:latest-debian-jdk21

USER root

RUN apt-get update
RUN apt install -y procps build-essential libssl-dev zlib1g-dev libbz2-dev \
libreadline-dev libsqlite3-dev wget curl llvm libncurses5-dev libncursesw5-dev \
xz-utils tk-dev libffi-dev liblzma-dev python3-openssl git

WORKDIR /root

RUN wget https://www.python.org/ftp/python/3.12.7/Python-3.12.7.tgz
RUN tar -xf Python-3.12.7.tgz

WORKDIR /root/Python-3.12.7

RUN ./configure --enable-optimizations
RUN make -j $(nproc)
RUN make altinstall

WORKDIR /root

RUN wget https://www.python.org/ftp/python/3.11.10/Python-3.11.10.tgz
RUN tar -xf Python-3.11.10.tgz

WORKDIR /root/Python-3.11.10

RUN ./configure --enable-optimizations
RUN make -j $(nproc)
RUN make altinstall

WORKDIR /root

RUN wget https://www.python.org/ftp/python/3.9.19/Python-3.9.19.tgz
RUN tar -xf Python-3.9.19.tgz

WORKDIR /root/Python-3.9.19

RUN ./configure --enable-optimizations
RUN make -j $(nproc)
RUN make altinstall

WORKDIR /root

RUN wget https://www.python.org/ftp/python/3.7.17/Python-3.7.17.tgz
RUN tar -xf Python-3.7.17.tgz

WORKDIR /root/Python-3.7.17

RUN ./configure --enable-optimizations
RUN make -j $(nproc)
RUN make altinstall

RUN apt install -y python3.11-venv

RUN apt-get clean && \
    rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/* /root/Python-*

WORKDIR /root

COPY . .

RUN mkdir -p /home/jenkins/.ssh
RUN chmod 700 /home/jenkins/.ssh
RUN cat id_rsa.pub > /home/jenkins/.ssh/authorized_keys
RUN chmod 600 /home/jenkins/.ssh/authorized_keys
RUN chown jenkins:jenkins -R /home/jenkins/.ssh
RUN rm /root/id_rsa.pub