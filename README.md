# Django REST API
The following steps will walk you thru installation on a Mac. I think linux should be similar. It's also possible to develop on a Windows machine, but I have not documented the steps. If you've developed django apps on Windows, you should have little problem getting up and running.

## Setup

### Dependancies

- Python 3.6.9 
- Django 3.0
- Mysql 8.0.19


### Create Database
The project I'm using MySql database. If you would use to `mysql`database you should follow the `command` 

First you install `mysql` on your Machine/operating system. Here I don't explain `how to install mysql?` in your 
system. your may search google how to work it!

<h2>How to create mysql database</h2>
First go to your terminal then follow the command line
```
mysql -u root -password
create dataase db_name;
```

Create a python virtual environment:

```bash/zsh
virtualenv venv --python=python3.6
```

Activate it:

```bash/zsh
source env/bin/activate
```

```
pip install -r requirements.txt

python3 manage.py runserver # or
./manage.py runserver
```

If you use `mysql` in your another project must be install mysql-client
`pip install mysqlclient`


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
