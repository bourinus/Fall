#!/usr/bin/env python3

import setuptools


with open('README.md') as f:
    long_description = ''.join(f.readlines())


setuptools.setup(
    name='fallapp',
    version='1.0',
    packages=setuptools.find_packages(exclude=['tests']),
    include_package_data=True,

    description='Fall app with debian packaging (dh_virtualenv & systemd)',
    long_description=long_description,
    author='choucroutage.com',
    author_email='mail@choucroutage.com',
    url='https://github.com/bourinus/Fall',

    # All versions are fixed just for case. Once in while try to check for new versions.
    install_requires=[
        'flask==1.0.2',
        'psycopg2==2.7.5',
    ],

    # Do not use test_require or build_require, because then it's not installed and
    # can be used only by setup.py. We want to use it manually as well.
    # Actually it could be in file like dev-requirements.txt but it's good to have
    # all dependencies close each other.
    extras_require={
        'devel': [
            'mypy==0.620',
            'pylint==2.1.1',
            'pytest==3.7.1',
        ],
    },

    entry_points={
        'console_scripts': [
            'fallapp = source.main:main',
        ],
    },

    classifiers=[
        'Framework :: None',
        'Intended Audience :: Developers',
        'Development Status :: 0- Beta',
        'License :: Other/Proprietary License',
        'Natural Language :: English',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3',
        'Topic :: Internet :: WWW/HTTP :: WSGI :: Application',
    ],
    zip_safe=False,
)