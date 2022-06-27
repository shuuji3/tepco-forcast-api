.PHONY: setup generate-index-html

setup:
	pip install poetry
	poetry install
	poetry shell

update-today-data:
	./generate-index-html.bash > public/index.html
	python today.py
