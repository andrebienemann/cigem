SHELL := /bin/bash

ROOT := $(shell pwd)

COMMAND_TEMPLATE := "  \033[36m%s\033[0m %s\n"

.PHONY: help
help all:
	@echo "Available Commands:"; \
	grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(firstword $(MAKEFILE_LIST)) | \
	awk 'BEGIN {FS = ":.*?## "}; {printf $(COMMAND_TEMPLATE), $$1, $$2}'; \

.PHONY: setup
setup: ## Setup the project
	@virtualenv -p python3 $(ROOT)/venv; \
	source $(ROOT)/venv/bin/activate; \
	pip install -r $(ROOT)/requirements.txt; \

.PHONY: format
format: ## Format the source code
	@source $(ROOT)/venv/bin/activate; \
	isort --profile black $(ROOT)/cigem $(ROOT)/setup.py; \
	black $(ROOT)/cigem $(ROOT)/setup.py; \

.PHONY: install
install: ## Install the module
	@python3 -m pip install $(ROOT); \

.PHONY: unit-tests
unit-tests: ## Execute unit tests
	@source $(ROOT)/venv/bin/activate && python3 -B \
	-m coverage run --source $(ROOT)/cigem \
	-m unittest discover $(ROOT)/tests/test_model; \

.PHONY: coverage
coverage: ## Display coverage
	@source $(ROOT)/venv/bin/activate; \
	coverage report -m; \

.PHONY: publish-lib
publish-lib: ## Publish on PyPI
	@source $(ROOT)/venv/bin/activate; \
	python3 $(ROOT)/setup.py sdist bdist_wheel; \
	twine upload $(ROOT)/dist/*; \

.PHONY: serve-docs
serve-docs: ## Server the documentation locally
	@source $(ROOT)/venv/bin/activate; \
	mkdocs serve; \

.PHONY: build-docs
build-docs: ## Build the documentation website
	@source $(ROOT)/venv/bin/activate; \
	mkdocs build; \

.PHONY: deploy-docs
deploy-docs: ## Deploy the documentation
	@source $(ROOT)/venv/bin/activate; \
	mkdocs gh-deploy --force; \
