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

echo:
	docker exec -ti mycrawler_worker_1 sh -c "echo a && echo b"

down:
	docker-compose --file docker-compose.yml down
