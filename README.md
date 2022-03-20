# Streaming
> Online OTT platform streaming backend web application.

### Dependencies

- Python 3.8
- PostgreSQL 12.8


### Create Database

<h2>How to create mysql database</h2>
First go to your terminal then follow the command line
```psql
psql postgres
CREATE DATABASE streaming;
```

#### Setup:
```bash
git clone https://github.com/mbrsagor/streaming.git
cd streaming
```

Create a python virtual environment:

```bash/zsh
virtualenv venv --python=python3.8
```

Activate it:

```bash/zsh
source env/bin/activate
```

###### Then create ``.env`` file and paste code from `.env_sample` file and add validate information.

-------------------------------------------
```bash
|--> .env-sample
|--> .env
```

```bash
pip install -r requirements.txt
./manage.py migrate
./manage.py runserver
./manage.py createsuperuser
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
