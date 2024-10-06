PY := python3
FLAGS := -b
SRC_DIR := src
STORAGE_SCRIPT := $(SRC_DIR)/storage.py
SENDER_SCRIPT := $(SRC_DIR)/sender.py


.PHONY: init freeze


init:
	pip install -r $(REQUIREMENTS_FILE)


freeze:
	pip freeze > $(REQUIREMENTS_FILE)
