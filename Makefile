# From:
# https://blog.horejsek.com/makefile-with-python/

.PHONY: help reset clean install install_dev test run doc

VENV_NAME?=venv
VENV_ACTIVATE=. $(VENV_NAME)/bin/activate
PYTHON=${VENV_NAME}/bin/python3

.DEFAULT: help
help:
	@echo '    make reset            reset the virtual environment'
	@echo "    make clean            remove temp files & virtual environment"
	@echo "    make install          install dependencies & environment"
	@echo "    make install_dev      install additional dev tools"
	@echo "    make test             run tests"
	@echo "    make run              run Fall"
	@echo "    make doc              build the documentation"

reset:
	make clean
	@rm -Rf "$(VIRTUAL_ENV)"
	if [ -d "venv/" ]; then rm -Rf venv/; fi
	make venv

clean:
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
	make venv

install_dev: install
ifeq ($(shell which dot),)
	# graphviz is used but pydeps module
	sudo apt install -y graphviz
else
	@echo "graphviz (dot) installed"
endif

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
