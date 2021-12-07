#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import sys

from setuptools import setup

with open(os.path.join(os.path.dirname(__file__), "README.rst")) as readme:
    README = readme.read()

INSTALL_REQUIRES = [
    "django >=1.4",
]

if sys.version_info < (2, 7):
    INSTALL_REQUIRES.append("importlib")

setup(
    name="django-sites",
    version="0.11",
    description="Alternative implementation of django sites framework",
    long_description=README,
    keywords="django, sites",
    author="Andrey Antukh",
    author_email="niwi@niwi.nz",
    url="https://github.com/niwinz/django-sites",
    license="BSD",
    packages=[
        "django_sites",
        "django_sites.templatetags",
    ],
    install_requires=INSTALL_REQUIRES,
    classifiers=[
        "Development Status :: 4 - Beta",
        "Framework :: Django",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: BSD License",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Framework :: Django",
        "Framework :: Django :: 1.9",
        "Framework :: Django :: 1.10",
        "Framework :: Django :: 2.0",
        "Framework :: Django :: 2.2",
        "Framework :: Django :: 3.0",
        "Framework :: Django :: 3.1",
        "Framework :: Django :: 3.2",
        "Topic :: Internet :: WWW/HTTP",
    ],
)
