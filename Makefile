install:
	pip install --upgrade pip &&\
		pip install -r requirements.txt

test:
	python -m pytest -vv

format:
	black  *.py */*.py

lint:
	pylint --disable=R,C *.py */*.py

all: install lint format test