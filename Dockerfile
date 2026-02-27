# Stage 1: React frontend build
FROM node:20-alpine AS frontend

WORKDIR /app

# Paket fayllarini kocurub install edirik
COPY mdu-global-horizon/package*.json ./mdu-global-horizon/
WORKDIR /app/mdu-global-horizon
RUN npm install

# Qalan kodu kocur ve build et
COPY mdu-global-horizon/ /app/mdu-global-horizon
RUN npm run build

# Stage 2: Django backend + gunicorn
FROM python:3.12-slim AS backend

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1

WORKDIR /app

# Lazim olan OS paketleri (opsional, burada minumum saxlayiriq)
RUN apt-get update && apt-get install -y --no-install-recommends \
    ca-certificates \
  && rm -rf /var/lib/apt/lists/*

# Python paketleri
COPY requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt

# Layihenin qalan fayllari
COPY . /app

# React build neticelerini birinci stage-den kocur
COPY --from=frontend /app/mdu-global-horizon/dist /app/mdu-global-horizon/dist

ENV DJANGO_SETTINGS_MODULE=config.settings

EXPOSE 8000

# Konteyner icinde avtomatik migrate + gunicorn basladir
CMD ["sh", "-c", "python manage.py migrate && gunicorn config.wsgi:application --bind 0.0.0.0:8000"]
