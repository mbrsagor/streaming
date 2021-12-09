# Django REST API
The following steps will walk you thru installation on a Mac. I think linux should be similar. It's also possible to develop on a Windows machine, but I have not documented the steps. If you've developed django apps on Windows, you should have little problem getting up and running.

## Setup

### Dependancies

- Python 3.6.9 
- Django 3.0
- PostgreSQL 12.8


### Create Database

<h2>How to create mysql database</h2>
First go to your terminal then follow the command line
```
psql postgres
CREATE DATABASE db_name;
```

Create a python virtual environment:

```bash/zsh
virtualenv venv --python=python3.6
```

Activate it:

```bash/zsh
source env/bin/activate
```

After that create `.env` file and paste all code from `.env-sample` file and add validation information

```
pip install -r requirements.txt
./manage.py migrate
./manage.py runserver
```

###### If you run the app `docker` please follow the instructions:
Open your terminal then run the command for `docker`

```bash
docker compose up
```
If you want to migrate or something similar please follow below commands:
```bash
docker-compose exec backend sh
python manage.py migrate
python manage.py makemigrations
python manage.py createsuperuser
```
