FROM jenkins/ssh-agent:latest-debian-jdk21

USER root

RUN apt-get update
RUN apt install -y procps build-essential libssl-dev zlib1g-dev libbz2-dev \
libreadline-dev libsqlite3-dev wget curl llvm libncurses5-dev libncursesw5-dev \
xz-utils tk-dev libffi-dev liblzma-dev python3-openssl git

WORKDIR /root

RUN wget https://www.python.org/ftp/python/3.12.0/Python-3.12.0.tgz
RUN tar -xf Python-3.12.0.tgz

WORKDIR /root/Python-3.12.0

RUN ./configure --enable-optimizations
RUN make -j 1
RUN make altinstall

WORKDIR /root

RUN wget https://www.python.org/ftp/python/3.11.0/Python-3.11.0.tgz
RUN tar -xf Python-3.11.0.tgz

WORKDIR /root/Python-3.11.0

RUN ./configure --enable-optimizations
RUN make -j 1
RUN make altinstall

WORKDIR /root

RUN wget https://www.python.org/ftp/python/3.9.0/Python-3.9.0.tgz
RUN tar -xf Python-3.9.0.tgz

WORKDIR /root/Python-3.9.0

RUN ./configure --enable-optimizations
RUN make -j 1
RUN make altinstall

WORKDIR /root

RUN wget https://www.python.org/ftp/python/3.7.0/Python-3.7.0.tgz
RUN tar -xf Python-3.7.0.tgz

WORKDIR /root/Python-3.7.0

RUN ./configure --enable-optimizations
RUN make -j 1
RUN make altinstall

RUN apt-get clean && \
    rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/* /root/Python-3.12.0

WORKDIR /root

COPY . .

RUN mkdir -p /home/jenkins/.ssh
RUN chmod 700 /home/jenkins/.ssh
RUN cat id_rsa.pub > /home/jenkins/.ssh/authorized_keys
RUN chmod 600 /home/jenkins/.ssh/authorized_keys
RUN chown jenkins:jenkins -R /home/jenkins/.ssh
RUN rm /root/id_rsa.pub