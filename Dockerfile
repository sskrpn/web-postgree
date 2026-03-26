FROM python:3.12-alpine AS builder

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /install

RUN apk add --no-cache \
    gcc \
    musl-dev \
    postgresql-dev \
    python3-dev

COPY app/requirements.txt .

RUN pip install --no-cache-dir --prefix=/install -r requirements.txt

FROM python:3.12-alpine AS runtime

WORKDIR /app

RUN apk add --no-cache libpq

COPY --from=builder /install /usr/local

COPY app/ /app/app

RUN adduser -D myuser
USER myuser

ENV PYTHONPATH=/app

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]