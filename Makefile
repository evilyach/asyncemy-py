.DEFAULT_GOAL := init

.PHONY: debug
debug:
	. venv/bin/activate
	python3 src/main.py

.PHONY: init
init:
	python3 -m venv venv
	. venv/bin/activate
	pip install -e .
