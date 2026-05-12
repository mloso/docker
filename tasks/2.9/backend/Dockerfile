FROM golang:1.16-alpine

WORKDIR /app

COPY go.mod .

RUN go mod download

COPY . .

RUN go build -o server .

ENV REQUEST_ORIGIN=http://localhost:5000

CMD ["./server"]