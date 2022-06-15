.PHONY: serve

ifneq (,$(wildcard ./.env))
    include .env
    export
endif

VENV=.venv
PYTHON=$(VENV)/bin/python3

serve:  ## Run application server in development
	$(PYTHON) main.py
