# Food Delivery API

A Django + Django REST Framework based food delivery backend API.

## Project Overview

- Purpose: Provide an API for restaurants, menu items, orders, payments, reviews, and user management.
- Tech stack: Python, Django, Django REST Framework, SQLite (default), Docker (optional).

## Quick Start (what to add and use)

- Prerequisites:
  - Python 3.11+
  - pip
  - virtualenv or venv
  - (Optional) Docker & Docker Compose

- Recommended steps to add in this README (already included below):
  - Setup environment and virtualenv commands
  - Install dependencies
  - Configure environment variables (.env)
  - Run migrations and create a superuser
  - Start the development server
  - Run tests

## Setup (Add these commands to README)

1. Create virtualenv and activate

```bash
python -m venv .venv
source .venv/bin/activate
```

2. Install dependencies

```bash
pip install -r requirements.txt
```

3. Copy .env example and update values

```bash
cp .env.example .env
# edit .env and set SECRET_KEY, DEBUG, DATABASE settings, etc.
```

4. Apply migrations

```bash
cd food_delivery
python manage.py migrate
```

5. Create superuser

```bash
python manage.py createsuperuser
```

6. Run the development server (from project root)

```bash
cd food_delivery
python manage.py runserver 8000
```

Notes: If `manage.py` isn't found when running from repo root, run from the `food_delivery` folder where `manage.py` lives.

## Environment variables

Add / update the following in `.env`:

- `SECRET_KEY` - Django secret key
- `DEBUG` - `True` or `False`
- `DATABASE_URL` or local DB settings if using Postgres
- Any API keys for payment providers (if applicable)

## Docker (optional)

- To run with Docker, build and run the compose stack:

```bash
docker-compose build
docker-compose up -d
```

## Running tests

```bash
cd food_delivery
python manage.py test
```

## Linting & Formatting

- Add instructions to run `black`, `flake8`, `isort` if you use them.

## Project Structure (top-level)

- `manage.py` - Django CLI
- `requirements.txt` - Python dependencies
- `food_delivery/` - Django project module (settings, urls, wsgi, asgi)
- `accounts/`, `restaurants/`, `menu/`, `orders/`, `payments/`, `reviews/`, etc. - Django apps
- `static/` - static assets
- `media/` - uploaded files
- `logs/` - application logs
- `docs/` - architecture, ER diagrams, screenshots
- `tests/` - high-level integration/unit tests

(You can paste the full tree here — include any missing apps or modules.)

## What to Add Later (placeholders)

- API documentation link (Swagger/OpenAPI) and endpoint examples.
- Example `.env` values or template for local dev.
- Database seeding commands (if you have fixtures or management commands).
- CI/CD instructions (GitHub Actions or other pipelines) — add workflow file links.
- How to run in production (gunicorn/uvicorn, Nginx, env vars, secrets management).
- Monitoring/logging setup and log rotation details.

## Contribution

- Fork, create a branch, make changes, and open a PR. Follow coding style and run tests locally.

## License

Add license information and link (e.g., MIT License).

## Contact

Add maintainer contact or repository owner details.
