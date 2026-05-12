FROM ubuntu:22.04

WORKDIR /app

COPY . .

RUN apt-get update && \
    apt-get install -y golang-go git && \
    go mod download && \
    go build -o server . && \
    apt-get purge -y --auto-remove golang-go git && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/* && \
    rm -rf /root/.cache && \
    rm -rf /tmp/*

CMD ["./server"]