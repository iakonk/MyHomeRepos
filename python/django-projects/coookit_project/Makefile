package: setup.py
	make clean
	python setup.py sdist

install-deps: requirements.txt
	pip install --no-cache-dir --upgrade --requirement requirements.txt

install:
	make install-deps
	pip install `find . -name 'coookit-*.tar.gz'`
	ln -s $(UWSGI_CHDIR)/manage.py /usr/bin/manage.py
	chmod +x /usr/bin/manage.py
	make collectstatic

collectstatic: $(UWSGI_CHDIR)/manage.py
	manage.py collectstatic --noinput

database: $(UWSGI_CHDIR)/manage.py
	manage.py makemigrations
	manage.py migrate
	manage.py makemigrations coookit
	manage.py migrate coookit

clean:
	rm -rf `find . -name __pycache__`
	rm -f `find . -type f -name '*.py[co]' `
	rm -f `find . -type f -name '.coverage' `
	rm -rf `find . -type d -name '.cache' `
	rm -rf dist
	rm -rf *.egg-info

.PHONY: install install-deps clean database package collectstatic post-install
