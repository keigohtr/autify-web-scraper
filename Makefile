mypy:
	poetry run mypy autifycli

lint: mypy
	poetry run flake8 . --max-line-length=120 --exclude=.venv,venv

fmt:
	poetry run isort -rc -sl .
	poetry run autoflake -ri --remove-all-unused-imports --ignore-init-module-imports --remove-unused-variables .
	poetry run black .
	poetry run isort -rc -m 3 .

test:
	poetry run pytest -v --cov=autifycli tests/
