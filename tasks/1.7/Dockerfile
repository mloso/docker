FROM ubuntu:22.04

WORKDIR /app

RUN apt update && apt install -y curl

COPY script.sh .
RUN chmod +x script.sh

CMD ./script.sh