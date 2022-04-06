FROM mysql:debian 

RUN apt-get update -y && apt-get install -y python3 && apt-get install -y python3-pip
