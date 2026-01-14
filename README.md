# Commercial Verified - Django Application

A Django REST API backend application built with Django and Django REST Framework.

## Features

- Django 4.2+ with REST Framework
- SQLite database (easily configurable for PostgreSQL/MySQL)
- Admin interface
- Environment variable configuration

## Setup Instructions

### 1. Create a Virtual Environment

```bash
cd /home/preetamsingh/Projects_files/CV/Backend/Commercial-Backend
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

### 3. Environment Configuration

Create a `.env` file in the root directory:

```bash
SECRET_KEY=your-secret-key-here
DEBUG=True
ALLOWED_HOSTS=localhost,127.0.0.1
```

You can generate a secret key using:
```python
python -c "from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())"
```

### 4. Run Migrations

```bash
python manage.py makemigrations
python manage.py migrate
```

### 5. Create a Superuser (Optional)

```bash
python manage.py createsuperuser
```

### 6. Run the Development Server

```bash
python manage.py runserver
```

The server will be available at `http://127.0.0.1:8000/`

## API Endpoints

- **Admin Panel**: `http://127.0.0.1:8000/admin/`

## Project Structure

```
Commercial-Backend/
├── commercial_verified/    # Main project settings
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   ├── wsgi.py
│   └── asgi.py
├── manage.py
├── requirements.txt
└── README.md
```

## Next Steps

1. Create your Django apps using `python manage.py startapp <app_name>`
2. Configure your database in `commercial_verified/settings.py`
3. Add authentication and permissions as needed
4. Set up CORS if connecting to a frontend application
5. Add your API endpoints and models

## Development

To add a new app:

```bash
python manage.py startapp <app_name>
```

Then add it to `INSTALLED_APPS` in `settings.py`.

