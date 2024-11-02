run-dev:
	poetry run python manage.py runserver 0.0.0.0:8000

run-migrate:
	poetry run python manage.py makemigrations
	poetry run python manage.py migrate

run-pro:
	poetry run python manage.py runserver 0.0.0.0:8000