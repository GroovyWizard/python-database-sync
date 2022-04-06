build:
	docker build -t mysql:python .

seed:
	docker exec -it simulated_db bash -c "mysql -uroot -p test_db < db/seed.sql"

up:
	docker-compose up -d 

sh:
	docker exec -it simulated_db bash

python-test:
	docker exec -it simulated_db bash -c "python3 "

pip:
	docker exec -it simulated_db bash -c "cd db && python3 -m pip install -r requirements.txt"

seed-w-dump:
	docker exec -it simulated_db bash -c "cd db && python3 main.py"

parse-sql:
	docker exec -it simulated_db bash -c "cd db && python3 parser.py"