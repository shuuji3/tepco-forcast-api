.PHONY: setup generate-index-html

setup:
	pip install poetry
	poetry install
	poetry shell

generate-index-html:
	./generate-index-html.bash > public/index.html

update-today-data:
	python today.py
