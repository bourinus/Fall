.PHONY: help prepare-dev test lint run doc reset clean

VENV_NAME?=venv
VENV_ACTIVATE=. $(VENV_NAME)/bin/activate
PYTHON=${VENV_NAME}/bin/python3

.DEFAULT: help
help:
	@echo "make prepare-dev"
	@echo "   prepare development environment, use only once"
	@echo "make test"
		@echo "       run tests"
	@echo "make lint"
	@echo "   run pylint and mypy"
	@echo "make run"
	@echo "   run project"
	@echo "make doc"
	@echo "   build sphinx documentation"
	@echo "make reset"
	@echo "   reset venv"
	@echo "make clean"
	@echo "   clean build directory"
	
prepare-dev:
	sudo apt-get -y install python3.5 python3-pip
	python3 -m pip install virtualenv
	virtualenv venv

# Requirements are in setup.py, so whenever setup.py is changed, re-run installation of dependencies.
venv: $(VENV_NAME)/bin/activate
	$(VENV_NAME)/bin/activate: requirements.py
	test -d $(VENV_NAME) || virtualenv -p python3 $(VENV_NAME)
	${PYTHON} -m pip install -U pip
	${PYTHON} -m pip install -e .
	touch $(VENV_NAME)/bin/activate


test: venv
	${PYTHON} -m pytest

lint: venv
	${PYTHON} -m pylint
	${PYTHON} -m mypy

run: venv
	${PYTHON} app.py

doc: venv
	$(VENV_ACTIVATE) && cd docs; make html
	
reset:
	make clean
	@rm -Rf "$(VIRTUAL_ENV)"
	if [ -d "venv/" ]; then rm -Rf venv/; fi
	make venv

clean:
	if [ -d "venv/" ]; then rm -Rf venv/; fi
	if [ -d "docs/build/" ]; then rm -Rf docs/build/; fi
	if [ -d "source/__pycache__/" ]; then rm -Rf source/__pycache__/; fi
	if [ -d "source/exceptions/__pycache__/" ]; then rm -Rf source/exceptions/__pycache__/; fi
	#if [ -d "tests/__pycache__/" ]; then rm -Rf tests/__pycache__/; fi
	
