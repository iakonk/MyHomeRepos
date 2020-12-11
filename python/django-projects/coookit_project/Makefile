.PHONY: package
package: setup.py
	make clean
	python setup.py sdist

.PHONY: install-deps
install-deps: requirements.txt
	pip install --no-cache-dir --upgrade --requirement requirements.txt

.PHONY: fix-permissions
fix-permissions:
	ln -s $(UWSGI_CHDIR)/manage.py /usr/bin/manage.py
	chmod +x /usr/bin/manage.py

.PHONY: prod-install
prod-install:
	echo 'Setting PROD environment'
	make install-deps
	pip install `find . -name 'coookit-*.tar.gz'`
	make post-install

.PHONY: dev-install
dev-install:
	echo 'Setting DEV environment'
	make install-deps
	pip install --editable /home
	make post-install

.PHONY: post-install
post-install:
	make fix-permissions
	make collectstatic
	make database

.PHONY: collectstatic
collectstatic: $(UWSGI_CHDIR)/manage.py
	manage.py collectstatic --noinput

.PHONY: database
database: $(UWSGI_CHDIR)/manage.py
	manage.py makemigrations
	manage.py migrate
	manage.py makemigrations coookit
	manage.py migrate coookit

.PHONY: clean
clean:
	rm -rf `find . -name __pycache__`
	rm -f `find . -type f -name '*.py[co]' `
	rm -f `find . -type f -name '.coverage' `
	rm -rf `find . -type d -name '.cache' `
	rm -rf dist
	rm -rf *.egg-info
