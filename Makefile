# From:
# https://blog.horejsek.com/makefile-with-python/
# https://www.dinotools.de/en/2019/12/23/use-python-with-virtualenv-in-makefiles/
# https://stackoverflow.com/questions/50199070/sphinx-extension-installation-of-sphinxcontrib-bibtex
.PHONY: help install test lint run doc reset clean var pdf

VENV_NAME?=venv
VENV_ACTIVATE=. $(VENV_NAME)/bin/activate
PYTHON=${VENV_NAME}/bin/python3

.DEFAULT: help
help:
	@echo "make install"
	@echo "   prepare development environment, use only once"
	@echo "make test"
	@echo "       run tests"
	@echo "make lint"
	@echo "   run pylint and mypy"
	@echo "make run"
	@echo "   run project"
	@echo "make doc"
	@echo "   build fall documentation"
	@echo "make reset"
	@echo "   reset venv"
	@echo "make clean"
	@echo "   clean build directory"
	@echo "make var"
	@echo "   echo python var path"
	@echo "make pdf"
	@echo "   build pdf from latex source"
	
install:
	which python3.8  || apt install -y  python3.8 python3-pip
	sudo apt install latexmk texlive texlive-science texlive-formats-extra	
	sudo apt install -y curl
	which get-pip.py || curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py
	python3.8 get-pip.py pip==20.1.1 wheel==0.34.2 setuptools==47.3.1 
	which virtualenv || python3 -m pip install virtualenv
	which venv || python3.8 -m pip install -r requirements.txt

	#warning while installing, recommanding  to upgrade pip.
	#	
	python3 -m pip install --upgrade pip
	#At this break-point, we need to check dependencies for future dev (ie sys.path)
	which dpkg-buildpackage || apt install -y debhelper dh-virtualenv dh-systemd lintian
	make venv

#alias activate=". ../.env/bin/activate"

# Requirements are in setup.py, so whenever setup.py is changed, re-run installation of dependencies.
#venv: 
#	VENV_ACTIVATE=. $(VENV_NAME)/bin/activate
#	
#	test -d $(VENV_NAME) || virtualenv -p python3 $(VENV_NAME)
#	sudo ${PYTHON} -m pip install -U pip
#	sudo ${PYTHON} -m pip install -e
#	sudo $(VENV_NAME)/bin/activate

venv: $(VENV_NAME)/bin/activate
$(VENV_NAME)/bin/activate: setup.py
	test -d $(VENV_NAME) || virtualenv -p python3 $(VENV_NAME)
	${PYTHON} -m pip install -U pip setuptools
	${PYTHON} -m pip install -r requirements.txt 
	touch $(VENV_NAME)/bin/activate

var:
	@echo " VENV_NAME:" + ${VENV_NAME}
	@echo " VENV_ACTIVATE: " + ${ENV_ACTIVATE}
	@echo " PYTHON" + ${PYTHON}
	@echo " ------------------------------"
	
test: venv
	${PYTHON} -m pytest

lint: venv
	${PYTHON} -m pylint
	${PYTHON} -m mypy

run: venv
	${PYTHON} ./source/main.py

doc:
	cd docs; make html
	
pdf: venv
	${PYTHON} ./docs/source/latex2pdf.py
	
#	$(VENV_ACTIVATE) && cd docs; make html
	
reset:
	make clean
	@rm -Rf "$(VIRTUAL_ENV)"
	if [ -d "venv/" ]; then rm -Rf venv/; fi
	virtualenv venv  -p /usr/bin/python3.7
#	VENV_ACTIVATE=. $(VENV_NAME)/bin/activate
clean:
	if [ -d "venv/" ]; then rm -Rf venv/; fi
	if [ -d "docs/build/" ]; then rm -Rf docs/build/; fi
	if [ -d "source/__pycache__/" ]; then rm -Rf source/__pycache__/; fi
	if [ -d "source/exceptions/__pycache__/" ]; then rm -Rf source/exceptions/__pycache__/; fi
	#if [ -d "tests/__pycache__/" ]; then rm -Rf tests/__pycache__/; fi
	
