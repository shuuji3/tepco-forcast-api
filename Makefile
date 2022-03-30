.PHONY: setup generate-index-html

setup:
	poetry install
	poetry shell

generate-index-html:
	./generate-index-html.bash > public/index.html
