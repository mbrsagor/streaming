# Instruction for Docker Deployment 

## Installation

Requirements:

- Default requirements mentioned above.
- Docker Latest

Follow these steps:
- Copy `example.env.toml` file to `.env.toml`
- In`.env.toml` file change `SQL_HOST="db"`
- Make a file name `.env.docker` add
```sh
POSTGRES_USER=db_user
POSTGRES_PASSWORD=db_password
POSTGRES_DB=db_name
```

## Up and Run

 - Docker Build
```sh
docker-compose up -d --build
```
- Lets Browse [http://0.0.0.0:8086](http://0.0.0.0:8086)
- Migration
```sh
docker-compose exec web python manage.py migrate --noinput
```
- Collect Statics 
```sh
docker-compose exec web python manage.py collectstatic --no-input --clear
```
- Check Logs
```sh
docker-compose logs -f
``` 
- Container down
```sh
docker-compose down
```
