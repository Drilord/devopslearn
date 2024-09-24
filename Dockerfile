FROM ubuntu
RUN apt-get update
RUN apt-get install apache2-utils -y
ADD . /var/www/html
ENV name=MyDockerfile