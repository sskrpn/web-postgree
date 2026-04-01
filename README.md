# webpostgree

## Основные особенности

*   **Full Stack Monitoring:** Сбор и визуализация метрик (Prometheus + Grafana).
*   **Containerization:** Полная изоляция сервисов через Docker.
*   **Reverse Proxy:** Высокопроизводительный Nginx для обработки трафика.
*   **CI/CD Automation:** Автоматическая проверка кода и сборка через GitHub Actions.

## Технологический стек

*   **Backend:** Python
*   **Database:** PostgreSQL
*   **Infrastructure:** Docker, Docker Compose, Nginx
*   **Observability:** Prometheus, Grafana
*   **Automation:** GitHub Actions (CI/CD)

## GitHub Actions (CI/CD)

В проекте настроен workflow, который при каждом `push` выполняет:
*   **Деплой на целевой сервер**


## Быстрый запуск

```bash
git clone https://github.com/sskrpn/web-postgree.git
cd web-postgree
docker-compose up -d --build
```

## Панель управления

| Сервис | Адрес | Описание |
| :--- | :--- | :--- |
| **App API** | [http://localhost:8000](http://localhost:8000) | Python веб-приложение |
| **Grafana** | [http://localhost:3000](http://localhost:3000) | Визуализация (admin/admin) |
| **Prometheus** | [http://localhost:9090](http://localhost:9090) | Сбор метрик |

## Структура репозитория

*   `.github/workflows/` — конфигурация GitHub Actions.
*   `app/` — исходный код приложения и Dockerfile.
*   `nginx/` — конфигурация прокси-сервера.
*   `prometheus/` & `grafana/` — конфигурации мониторинга.
*   `docker-compose.yml` — манифест для развертывания всего стека.

## Настройка окружения
Не забудьте создать файл `.env` на основе примера для корректной работы базы данных:
```env
DATABASE_URL=postgresql://user:password@db:5432/web_db
POSTGRES_USER=user
POSTGRES_PASSWORD=password
POSTGRES_DB=web_db
```
