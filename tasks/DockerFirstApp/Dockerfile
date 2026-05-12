FROM python:3.13-slim AS build-stage

WORKDIR /app

COPY requirements.txt ./

RUN python -m venv /opt/venv

ENV PATH="/opt/venv/bin:$PATH"
RUN pip install --no-cache-dir -r requirements.txt

FROM python:3.13-slim AS runtime

WORKDIR /app

ENV HOME=/app
ENV PATH="/opt/venv/bin:$PATH"

COPY --from=build-stage /opt/venv /opt/venv
COPY . .

CMD ["python", "app/main.py"]