.PHONY: info env dev clean

help:
	@echo "Steps to be run only during initialization"
	@echo "  env         install the Python v3 virtual environment"
	@echo "  dev         install all dev and production dependencies (virtualenv is assumed)"
	@echo "Dev Steps"
	@echo "  clean       remove unwanted stuff"
	@echo "  lint        check style with black"
	@echo "  test        run tests"
	@echo "  run		 run flask app locally"
	@echo "Deploy Steps"
	@echo "  build       generate source and wheel dist files"
	@echo "  upload      generate source and wheel dist files and upload them"

info:
	@pipenv --version
	@pipenv run python --version
	@pipenv --venv

env:
	pipenv install --python 3.9
	pipenv run python -m pip install --upgrade pip

dev: env
	pipenv install --dev

clean:
	rm -fr build
	rm -fr dist
	find . -name '*.pyc' -exec rm -f {} \;
	find . -name '*.pyo' -exec rm -f {} \;
	find . -name '*~' -exec rm -f {} \;

lint: clean
	pipenv run black uchi.py app

run:
	pipenv run flask run