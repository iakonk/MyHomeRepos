package: setup.py
	make clean
	python setup.py sdist

install-deps: requirements.txt
	pip install --no-cache-dir --upgrade --requirement requirements.txt

install:
	make install-deps
	pip install `find . -name 'coookit-*.tar.gz'`
	make django-collectstatic
	make post-install

post-install:
	pip cache purge

django-collectstatic: $(UWSGI_CHDIR)/manage.py
	python $(UWSGI_CHDIR)/manage.py collectstatic

database:
	cd /opt/bics_ipop/migrations/
	nomad init

clean:
	rm -rf `find . -name __pycache__`
	rm -f `find . -type f -name '*.py[co]' `
	rm -f `find . -type f -name '.coverage' `
	rm -rf `find . -type d -name '.cache' `
	rm -rf dist
	rm -rf *.egg-info

.PHONY: install install-deps clean database package django-collectstatic post-install
