envs:
	docker exec -it microservices_mr_sandwich_food_factory printenv

sh:
	docker exec -it microservices_mr_sandwich_food_factory bash

dbexec:
	docker exec -it --user postgres microservices_mr_sandwich_food_factory_db psql

dev:
	python manage.py runserver 8001

su:
	docker exec -it microservices_mr_sandwich_food_factory python manage.py createsuperuser

dbmm:
	python manage.py makemigrations ${a}

dbmr:
	python manage.py migrate ${a}

dbsm:
	python manage.py showmigrations ${a}

dbload:
	python manage.py loaddata ${f}

dbdump:
	python manage.py dumpdata > ${f}
