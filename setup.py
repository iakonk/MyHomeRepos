import os
from setuptools import setup, find_packages
from glob import glob
from ipop2_core import __version__, __description__

# details about App
with open(os.path.join(os.path.dirname(__file__), 'README.rst')) as readme:
    README = readme.read()

# allow setup.py to be run from any path
os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))


setup(
    name='ipop',
    description=__description__,
    version=__version__,
    license='',
    long_description=README,
    author='Ronkart Andre',
    author_email='andre.ronkart@bics.com',
    url='http://bicswiki.bc/display/psddevsystem/IPOP+Home+Page',
    packages=find_packages(),
    data_files=[
        ('', glob('*.py')),
        ('', glob('*.txt')),
    ],
    include_package_data=True,
    platforms=['Any'],
    zip_safe=False
)