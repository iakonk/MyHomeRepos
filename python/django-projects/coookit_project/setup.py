import os
from setuptools import setup, find_packages
from glob import glob
from coookit import __version__, __description__

# details about App
with open(os.path.join(os.path.dirname(__file__), 'README.rst')) as readme:
    README = readme.read()

# allow setup.py to be run from any path
os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))


setup(
    name='coookit',
    description=__description__,
    version=__version__,
    license='',
    long_description=README,
    author='Iana Konkina',
    author_email='konkina.iana@gmail.com',
    url='https://github.com/iakonk/MyHomeRepos',
    packages=find_packages(),
    data_files=[
        ('', glob('*.py')),
        ('', glob('*.txt')),
    ],
    include_package_data=True,
    platforms=['Any'],
    zip_safe=False
)