## Movies Notifications

[![python](https://img.shields.io/static/v1?label=python&message=3.8%20|%203.9%20|%203.10&color=informational)](https://github.com/8ubble8uddy/movies-notifications/actions/workflows/main.yml)
[![dockerfile](https://img.shields.io/static/v1?label=dockerfile&message=published&color=2CB3E8)](https://hub.docker.com/search?q=8ubble8uddy%2Fnotifications)
[![last updated](https://img.shields.io/static/v1?label=last%20updated&message=march%202023&color=yellow)](https://img.shields.io/static/v1?label=last%20updated&message=march%202022&color=yellow)
[![lint](https://img.shields.io/static/v1?label=lint&message=flake8%20|%20mypy&color=brightgreen)](https://github.com/8ubble8uddy/movies-notifications/actions/workflows/main.yml)
[![code style](https://img.shields.io/static/v1?label=code%20style&message=WPS&color=orange)](https://wemake-python-styleguide.readthedocs.io/en/latest/)
[![platform](https://img.shields.io/static/v1?label=platform&message=linux%20|%20macos&color=inactive)](https://github.com/8ubble8uddy/movies-notifications/actions/workflows/main.yml)

### **Описание**

_Целью данного проекта является реализация сервиса уведомлений для онлайн-кинотеатра. В связи с этим разработана система из нескольких микросервисов. Источником уведомлений является API для приёма событий на фреймворке [FastAPI](https://fastapi.tiangolo.com). Процесс, который отправляет уведомление (воркер) реализован с помощью библиотеки потоковой обработки [Faust](https://faust.readthedocs.io). Общение API и воркера происходит через очередь сообщений [Kafka](https://kafka.apache.org). Для создания ручной рассылки уведомлений используется админ-панель на фреймворке [Django](https://www.djangoproject.com) в связке с [Celery](https://docs.celeryq.dev) для  отправки периодических уведомления (шедулер). Админка с шедулером работают с базой данной [PostgreSQL](https://www.postgresql.org), в которой хранятся уведомления, история их отправки и периодичность выполнения._

### **Технологии**

```Python``` ```FastAPI``` ```Django``` ```Celery``` ```Faust``` ```Kafka``` ```PostgreSQL``` ```Redis``` ```NGINX``` ```Docker```

### **Как запустить проект:**

Клонировать репозиторий и перейти внутри него в директорию ```/infra```:
```
git clone https://github.com/8ubble8uddy/movies-notifications.git
```
```
cd movies-notifications/infra/
```

Создать файл .env и добавить настройки для проекта:
```
nano .env
```
```
# PostgreSQL
POSTGRES_DB=notifications_database
POSTGRES_USER=postgres
POSTGRES_PASSWORD=postgres
POSTGRES_HOST=postgres
POSTGRES_PORT=5432

# Kafka
KAFKA_HOST=kafka
KAFKA_PORT=9092

# Redis
REDIS_HOST=redis
REDIS_PORT=6379

# Django
DJANGO_SUPERUSER_USERNAME=admin
DJANGO_SUPERUSER_EMAIL=admin@mail.ru
DJANGO_SUPERUSER_PASSWORD=1234
DJANGO_ALLOWED_HOSTS=localhost,127.0.0.1,[::1],django
DJANGO_SECRET_KEY=django-insecure-_o)z83b+i@jfjzbof_jn9#%dw*5q2yy3r6zzq-3azof#(vkf!#

# Microservices
EVENT_SOURCING_URL=fastapi:8000
ADMIN_URL=django:8000
```

Развернуть и запустить проект в контейнерах:
```
docker-compose up
```

Перейти в админ-панель и ввести логин (admin) и пароль (1234)::
```
http://127.0.0.1/notifications
```

Документация API будет доступна по адресу:
```
http://127.0.0.1/openapi
```

### Автор: Герман Сизов