FROM docker:24

RUN apk add --no-cache git bash

WORKDIR /app

COPY builder.sh .

RUN chmod +x builder.sh

ENTRYPOINT ["./builder.sh"]
