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
