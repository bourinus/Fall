# From:
# https://blog.horejsek.com/makefile-with-python/

.PHONY: help clean check install test run doc

VENV_NAME?=venv
VENV_ACTIVATE=. $(VENV_NAME)/bin/activate
PYTHON=${VENV_NAME}/bin/python3

.DEFAULT: help
help:
	@echo "make install"
	@echo "       install dependencies & environment"
	@echo "make test"
	@echo "       run tests"
	@echo "make run"
	@echo "       run Fall"
	@echo "make doc"
	@echo "       build documentation"

clean:
	if [ -d "venv/" ]; then rm -Rf venv/; fi
	if [ -d "docs/build/" ]; then rm -Rf docs/build/; fi
	if [ -d "source/__pycache__/" ]; then rm -Rf source/__pycache__/; fi
	if [ -d "source/exceptions/__pycache__/" ]; then rm -Rf source/exceptions/__pycache__/; fi
	#if [ -d "tests/__pycache__/" ]; then rm -Rf tests/__pycache__/; fi


install: 
ifeq ($(shell which python3),)
	sudo apt install -y python3.7 
else
	@echo "python3.7 installed"
endif
ifeq ($(shell which pip),)
	sudo apt install -y python3-pip
else
	@echo "python3-pip installed"
endif
ifeq ($(shell which virtualenv),)
	sudo apt install -y virtualenv
else
	@echo "virtualenv installed"
endif
ifeq ($(shell which graphviz),)
	sudo apt install -y graphviz
else
	@echo "graphviz installed"
endif
	# graphviz is used but pydeps module
	make venv


# Requirements are in requirements.py, 
# so whenever requirements.py is changed, re-run installation of dependencies.
venv: $(VENV_NAME)/bin/activate
$(VENV_NAME)/bin/activate: requirements.py
	test -d $(VENV_NAME) || virtualenv -p python3.7 $(VENV_NAME)
	${PYTHON} -m pip install -U pip
	#${PYTHON} -m pip install -e .
	touch $(VENV_NAME)/bin/activate

test: venv
	#	${PYTHON} tests/test_advanced.py
	${PYTHON} tests/test_basic.py

run: venv
	${PYTHON} source/main.py

doc: venv
	$(VENV_ACTIVATE) && cd docs; make html
