build:
	docker-compose --file docker-compose.yml build

full-build:
		docker-compose --file docker-compose.yml build --no-cache

run:
	docker-compose --file docker-compose.yml run --rm web

up:
	docker-compose --file docker-compose.yml up
