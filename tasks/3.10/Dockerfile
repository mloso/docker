FROM python:3.11-alpine

WORKDIR /app

COPY main.py .

RUN adduser -D appuser && \
    chown appuser:appuser /app

USER appuser

CMD ["python", "main.py"]