.PHONY: build up down go

build:
	@docker-compose -f docker-compose.yml build

up:
	@docker-compose -f docker-compose.yml up -d 

down:
	@docker-compose -f docker-compose.yml down

restart: down up

log:
	@docker-compose -f docker-compose.yml logs $(app)

migrate:
	@docker-compose -f docker-compose.yml exec backend python manage.py migrate

makemigrations:
	@docker-compose -f docker-compose.yml exec backend python manage.py makemigrations -v 3 $(c)

createsuperuser:
	@docker-compose -f docker-compose.yml exec backend python manage.py createsuperuser --email=root@localhost