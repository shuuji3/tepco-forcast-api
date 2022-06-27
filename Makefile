.PHONY: setup generate-index-html

setup:
	pip install poetry
	poetry install

update-today-data:
	./generate-index-html.bash > public/index.html
	poetry run python today.py
