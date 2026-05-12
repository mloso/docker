FROM alpine:3.19

WORKDIR /app

COPY . .

RUN apk add --no-cache go git && \
    go mod download && \
    CGO_ENABLED=0 go build -o server . && \
    apk del go git && \
    rm -rf /root/go && \
    rm -rf /var/cache/apk/* && \
    rm -rf /tmp/*

CMD ["./server"]