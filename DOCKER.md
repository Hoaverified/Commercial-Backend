# Docker Setup for Commercial Verified

This project is fully dockerized with support for both local development and production environments.

## Prerequisites

- Docker
- Docker Compose

## Quick Start

### 1. Setup Environment Files

Create your environment files based on the examples:

```bash
# For local development
cp env/.env.local.example env/.env.local

# For production
cp env/.env.prod.example env/.env.prod
```

Edit the `.env.local` or `.env.prod` files with your actual configuration values.

### 2. Build and Run

**Local Development:**
```bash
docker-compose -f docker-compose.local.yml up --build
```

**Production:**
```bash
docker-compose -f docker-compose.prod.yml up --build
```

**Using default (local):**
```bash
docker-compose up --build
```

### 3. Access the Application

- **Web Application**: http://localhost:8003
- **Admin Panel**: http://localhost:8003/admin
- **PostgreSQL**: localhost:5432
- **Redis Master**: localhost:6379
- **Redis Slave**: localhost:6380

## Services

The Docker setup includes the following services:

1. **web** - Django application server
2. **db** - PostgreSQL database
3. **redis-master** - Redis master instance
4. **redis-slave** - Redis replica
5. **celery** - Celery worker for async tasks
6. **celery-beat** - Celery beat scheduler

## Docker Commands

### Start services
```bash
docker-compose up
```

### Start in background (detached mode)
```bash
docker-compose up -d
```

### Stop services
```bash
docker-compose down
```

### Stop and remove volumes
```bash
docker-compose down -v
```

### View logs
```bash
# All services
docker-compose logs -f

# Specific service
docker-compose logs -f web
docker-compose logs -f celery
```

### Execute commands in containers
```bash
# Django shell
docker-compose exec web python manage.py shell

# Create superuser
docker-compose exec web python manage.py createsuperuser

# Run migrations
docker-compose exec web python manage.py migrate

# Collect static files
docker-compose exec web python manage.py collectstatic --noinput
```

### Rebuild after changes
```bash
docker-compose up --build
```

## Environment Variables

Key environment variables (set in `env/.env.local` or `env/.env.prod`):

- `SECRET_KEY` - Django secret key
- `DEBUG` - Debug mode (True/False)
- `ALLOWED_HOSTS` - Comma-separated list of allowed hosts
- `POSTGRES_NAME` - Database name
- `POSTGRES_USER` - Database user
- `POSTGRES_PASSWORD` - Database password
- `POSTGRES_HOST` - Database host (use `db` in Docker)
- `POSTGRES_PORT` - Database port (5432)
- `CELERY_BROKER_URL` - Redis URL for Celery
- `CELERY_RESULT_BACKEND` - Redis URL for Celery results

## Database

The PostgreSQL database is automatically created when the `db` service starts. Migrations are run automatically when the `web` service starts.

To access the database directly:
```bash
docker-compose exec db psql -U postgres -d commercial_verified_db
```

## Celery

Celery workers and beat scheduler are configured to use Redis as the message broker.

To monitor Celery:
```bash
# View celery worker logs
docker-compose logs -f celery

# View celery beat logs
docker-compose logs -f celery-beat
```

## Troubleshooting

### Port already in use
If port 8003, 5432, 6379, or 6380 are already in use, modify the port mappings in `docker-compose.yml`.

### Database connection errors
Ensure the `POSTGRES_HOST` in your `.env` file is set to `db` (the service name) when running in Docker.

### Permission errors
If you encounter permission errors, ensure Docker has proper permissions:
```bash
sudo usermod -aG docker $USER
```
Then log out and log back in.

### Clear everything and start fresh
```bash
docker-compose down -v
docker system prune -a
docker-compose up --build
```

## Production Deployment

For production:

1. Use `docker-compose.prod.yml`
2. Set `DEBUG=False` in `env/.env.prod`
3. Use strong passwords and secret keys
4. Configure proper `ALLOWED_HOSTS`
5. Set up SSL/TLS certificates
6. Use a production WSGI server (gunicorn/uwsgi) instead of `runserver`

Example production Dockerfile modification:
```dockerfile
# Replace the CMD in Dockerfile for production
CMD ["gunicorn", "--bind", "0.0.0.0:8003", "commercial_verified.wsgi:application"]
```
