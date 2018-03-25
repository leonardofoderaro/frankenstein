from setuptools import setup

setup(
   name='frankie',
   version='0.1',
   description='A simple tool to proxy and modify webpages',
   scripts=['frankie/frankie'],
   author='Leonardo Foderaro',
   author_email='leonardofoderaro@gmail.com',
   packages=['frankie'], 
   install_requires=['fire', 'lxml', 'requests'],
)
