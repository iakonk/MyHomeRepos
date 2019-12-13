PYENV_HOME=venv

install-deps: requirements.txt
	${PYENV_HOME}/bin/pip install -U -r requirements.txt

venv: clean
	rm -rf ${PYENV_HOME}
	virtualenv -p python3 ${PYENV_HOME}
	mkdir -p ${PYENV_HOME}/site-packages
	echo "../.." > ${PYENV_HOME}/site-packages/app.pth
	. ${PYENV_HOME}/bin/activate
	make install-deps

test:
	${PYENV_HOME}/bin/python -m unittest

clean:
	rm -rf `find . -name __pycache__`
	rm -f `find . -type f -name '*.py[co]' `
	rm -f `find . -type f -name '.coverage' `
	rm -rf `find . -type d -name '.cache' `
	rm -rf dist
	rm -rf *.egg-info


.PHONY: test install-deps clean
