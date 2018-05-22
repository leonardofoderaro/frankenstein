import re
import os
from setuptools import setup, find_packages

def package_files(directory):
    paths = []
    for (path, directories, filenames) in os.walk(directory):
        for filename in filenames:
            paths.append(os.path.join('..', path, filename))
    return paths

path = re.sub('setup.py', '', os.path.realpath(__file__))

path = path + 'frankie/lib'

extra_files = package_files(path)

setup(
   name='frankie',
   version='0.1',
   description='A simple tool to proxy and modify webpages',
   scripts=['frankie/frankie'],
   author='Leonardo Foderaro',
   author_email='leonardofoderaro@gmail.com',
   install_requires=['fire', 'lxml', 'requests'],
   packages=find_packages(),
   include_package_data=True,
   package_data={'': extra_files},
)

