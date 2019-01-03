build:
	docker-compose --file docker-compose.yml build

full-build:
		docker-compose --file docker-compose.yml build --no-cache

run:
	docker-compose --file docker-compose.yml run --rm web

up:
	docker-compose --file docker-compose.yml up

bash:
	docker exec -it mycrawler_worker_1 bash

down:
	docker-compose --file docker-compose.yml down
