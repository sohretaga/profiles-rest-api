# Profiles REST API

Profiles REST API is a simple RESTful API designed to manage user profiles. This project is built using Django and Django REST Framework.

## Features

- User registration and authentication
- User profile management (create, update, delete)
- Authorization and permission controls
- Nginx and Supervisor setup for production
- Vagrant support for development

## Installation

### 1. Requirements

Ensure you have the following dependencies installed:

- Python 3.8+
- Django 4.0+
- Django REST Framework
- Vagrant (optional)
- Nginx (for deployment)
- Supervisor (for deployment)

### 2. Clone the Project

```sh
git clone https://github.com/sohretaga/profiles-rest-api.git
cd profiles-rest-api
```

### 3. Create a Virtual Environment

```sh
python -m venv venv
source venv/bin/activate  # For MacOS/Linux
venv\Scripts\activate    # For Windows
```

### 4. Install Dependencies

```sh
poetry install
```

### 5. Apply Migrations

```sh
poetry run python manage.py migrate
```

### 6. Create a Superuser

```sh
poetry run python manage.py createsuperuser
```

### 7. Start the Development Server

```sh
poetry run python manage.py runserver
```

You can test the API locally at `http://127.0.0.1:8000/`.

## Using Vagrant

To run the development environment with Vagrant, execute:

```sh
vagrant up
```

To connect to the virtual machine:

```sh
vagrant ssh
```

## Deployment

### Deploying with Nginx and Supervisor

1. Copy `deploy/nginx_profiles_api.conf` to `/etc/nginx/sites-available/` and restart Nginx.
2. Copy `deploy/supervisor_profiles_api.conf` to `/etc/supervisor/conf.d/` and reload Supervisor.
3. Run `deploy/setup.sh` to finalize server configuration.

### Deploying Updates

To deploy new changes:

```sh
bash deploy/update.sh
```

## API Endpoints

| Method | URL | Description |
|--------|-----|-------------|
| GET | `/hello-view/` | A basic APIView example |
| GET | `/hello-viewset/` | An endpoint created with ViewSet |
| GET | `/api/profiles/` | Lists user profiles |
| POST | `/api/profiles/` | Creates a new user profile |
| GET | `/api/profiles/{id}/` | Retrieves a specific user profile |
| PUT | `/api/profiles/{id}/` | Updates a user profile |
| DELETE | `/api/profiles/{id}/` | Deletes a user profile |
| POST | `/login/` | Authenticates a user |
| GET | `/feed/` | Lists user activities |

## License

This project is licensed under the [MIT License](LICENSE).
