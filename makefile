.PHONY: build up down migrate go

build:
	@docker-compose -f docker-compose.yml build

up:
	@docker-compose -f docker-compose.yml up -d 

down:
	@docker-compose -f docker-compose.yml down

restart: down up

log:
	@docker-compose -f docker-compose.yml logs $(app)
