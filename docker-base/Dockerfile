FROM ubuntu:trusty
MAINTAINER cheryl.chiu
RUN apt-get update && apt-get install -y curl openssh-server unzip openjdk-7-jre-headless wget supervisor docker.io
ENV JAVA_HOME /usr/lib/jvm/java-7-openjdk-amd64/

RUN mkdir /var/run/sshd
RUN echo 'root:xyz' | chpasswd
RUN sed -i 's/PermitRootLogin without-password/PermitRootLogin yes/' /etc/ssh/sshd_config

# SSH login fix. Otherwise user is kicked off after login
RUN sed 's@session\s*required\s*pam_loginuid.so@session optional pam_loginuid.so@g' -i /etc/pam.d/sshd

ENV NOTVISIBLE "in users profile"
RUN echo "export VISIBLE=now" >> /etc/profile

EXPOSE 22
CMD ["/usr/sbin/sshd", "-D"]
