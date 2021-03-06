.PHONY: clean clean-test clean-pyc clean-build docs help
.DEFAULT_GOAL := help

define BROWSER_PYSCRIPT
import os, webbrowser, sys

try:
	from urllib import pathname2url
except:
	from urllib.request import pathname2url

webbrowser.open("file://" + pathname2url(os.path.abspath(sys.argv[1])))
endef
export BROWSER_PYSCRIPT

define PRINT_HELP_PYSCRIPT
import re, sys

for line in sys.stdin:
	match = re.match(r'^([a-zA-Z_-]+):.*?## (.*)$$', line)
	if match:
		target, help = match.groups()
		print("%-20s %s" % (target, help))
endef
export PRINT_HELP_PYSCRIPT

BROWSER := python -c "$$BROWSER_PYSCRIPT"

help:
	@python -c "$$PRINT_HELP_PYSCRIPT" < $(MAKEFILE_LIST)

clean: clean-build clean-pyc clean-test clean-swagger ## remove all build, test, coverage and Python artifacts

clean-build: ## remove build artifacts
	rm -fr build/
	rm -fr dist/
	rm -fr .eggs/
	find . -name '*.egg-info' -exec rm -fr {} +
	find . -name '*.egg' -exec rm -f {} +

clean-pyc: ## remove Python file artifacts
	find . -name '*.pyc' -exec rm -f {} +
	find . -name '*.pyo' -exec rm -f {} +
	find . -name '*~' -exec rm -f {} +
	find . -name '__pycache__' -exec rm -fr {} +

clean-test: ## remove test and coverage artifacts
	rm -fr .tox/
	rm -f .coverage
	rm -fr htmlcov/
	rm -fr .pytest_cache

clean-swagger:
	rm -rf python_vectra_cognito_detect_v1
	rm -rf python_vectra_cognito_detect_v2

lint: ## check style with flake8
	flake8 vectra_api_client tests

test: swagger ## run tests quickly with the default Python
	pytest --doctest-modules

test-all: swagger ## run tests on every Python version with tox
	tox

coverage: swagger ## check code coverage quickly with the default Python
	coverage run --source vectra_api_client -m pytest
	coverage report -m
	coverage html

docs: swagger ## generate Sphinx HTML documentation, including API docs
	rm -f docs/vectra_api_client.rst
	rm -f docs/modules.rst
	sphinx-apidoc -o docs/ vectra_api_client
	sphinx-apidoc -o docs/ python_vectra_cognito_detect_v1
	sphinx-apidoc -o docs/ python_vectra_cognito_detect_v2
	$(MAKE) -C docs clean
	$(MAKE) -C docs html
	$(BROWSER) docs/_build/html/index.html

servedocs: docs ## compile the docs watching for changes
	watchmedo shell-command -p '*.rst' -c '$(MAKE) -C docs html' -R -D .

release: dist ## package and upload a release
	twine upload dist/*

dist: clean swagger ## builds source and wheel package
	python setup.py sdist
	python setup.py bdist_wheel
	ls -l dist

install: clean swagger ## install the package to the active Python's site-packages
	python setup.py install

USERNAME=$(shell id --user --name)
UID=$(shell id --user $(USERNAME))
GID=$(shell id --group $(USERNAME))

CONFIG_DIR=swagger/config
OUTPUT_DIR?=.
GENERATOR_NAME?=python

docker-build:
	docker build \
		--build-arg USERNAME=$(USERNAME) \
		--build-arg UID=$(UID) \
		--build-arg GID=$(GID) \
		-t openapi-generator-cli \
		-f docker/Dockerfile \
		. \
		2>&1 >/dev/null


.PHONY: swagger
swagger: docker-build clean-swagger
	SWAG_DIR=swagger/cognito/detect/v1 GENERATOR_NAME=python ./scripts/run_swagger.sh
	SWAG_DIR=swagger/cognito/detect/v2 GENERATOR_NAME=python ./scripts/run_swagger.sh
	rm -rf .openapi-generator
	rm -rf test
