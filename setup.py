# -*- coding: utf-8 -*-
# Learn more: https://github.com/kennethreitz/setup.py

from setuptools import setup, find_packages


with open('README.rst') as f:
	readme = f.read()

with open('LICENSE') as f:
	license = f.read()

setup(
	name='Fall',
	version='0.1.0',
	description='stable operators of fall, paradox & repetition based functions in python.',
	long_description=readme,
	author='choucroutage.com',
	author_email='davidgueguen2000@yahoo.fr',
	url='https://github.com/bourinus/Fall',
	license=license,
	packages=find_packages(exclude=('tests', 'docs'))
)
