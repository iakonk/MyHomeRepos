import os
from setuptools import setup, find_packages
from glob import glob


# details about App
with open(os.path.join(os.path.dirname(__file__), 'README.rst')) as readme:
    README = readme.read()

# allow setup.py to be run from any path
os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

with open('requirements.txt', 'r') as fd:
    requirements_list = [line for line in fd.read().splitlines() if line.strip()]

setup(
    name='messaging_app',
    description='ZMQ Server/Client example',
    version='0.1',
    license='',
    long_description=README,
    author='',
    author_email='',
    url='',
    packages=find_packages(),
    install_requires=requirements_list,
    data_files=[
        ('', glob('README.rst'))
    ],
    include_package_data=True,
    platforms=['Any'],
    zip_safe=False
)