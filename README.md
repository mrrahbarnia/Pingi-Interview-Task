# Pingi Interview Task

## Run the project

Start all services:

```bash
docker compose up --build
```

## Apply database migrations

In another terminal, run:

```bash
docker compose exec app python src/manage.py migrate
```

## Swagger Documentation

After the application is running, Swagger is available at:

```
http://localhost:8000/docs/swagger/
```

## Load Testing

Locust is available at:

```
http://localhost:8089
```
