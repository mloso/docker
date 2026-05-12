FROM golang:1.16-alpine AS builder

WORKDIR /app

COPY go.mod go.sum ./

RUN go mod download

COPY backend .

RUN CGO_ENABLED=0 GOOS=linux go build -a -installsuffix cgo -o server .

FROM scratch

WORKDIR /app

COPY --from=builder /app/server .

CMD ["/app/server"]