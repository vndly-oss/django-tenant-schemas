#!/usr/bin/env python

from os.path import exists

from setuptools import find_packages
from setuptools import setup

setup(
    name='django-tenant-schemas',
    author='Bernardo Pires Carneiro',
    author_email='carneiro.be@gmail.com',
    version="1.9.0+vndly-0.0.5",
    packages=find_packages(),
    scripts=[],
    url='https://github.com/bcarneiro/django-tenant-schemas',
    license='MIT',
    description='Tenant support for Django using PostgreSQL schemas.',
    long_description=open('README.rst').read() if exists("README.rst") else "",
    classifiers=[
        'License :: OSI Approved :: MIT License',
        'Framework :: Django',
        'Framework :: Django :: 2.0',
        'Programming Language :: Python',
        "Programming Language :: Python :: 3.5",
        "Topic :: Database",
        "Topic :: Software Development :: Libraries",
    ],
    install_requires=["Django>=2.2", "ordered-set", "psycopg2", "six"],
    setup_requires=["setuptools-scm"],
    use_scm_version=True,
    zip_safe=False,
)
