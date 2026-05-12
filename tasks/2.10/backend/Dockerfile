FROM golang:1.16-alpine

WORKDIR /app

COPY go.mod .

RUN go mod download

COPY . .

RUN go build -o server .

EXPOSE 3000

CMD ["./server"]