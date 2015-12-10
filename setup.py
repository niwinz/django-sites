#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup
import sys


INSTALL_REQUIRES = [
    "django >=1.4",
]

if sys.version_info < (2, 7):
    INSTALL_REQUIRES.append('importlib')

setup(
    name = "django-sites",
    version = "0.9",
    description = "Alternative implementation of django sites framework",
    long_description = "",
    keywords = "django, sites",
    author = "Andrey Antukh",
    author_email = "niwi@niwi.nz",
    url = "https://github.com/niwinz/django-sites",
    license = "BSD",
    packages = [
        "django_sites",
        "django_sites.templatetags",
    ],

    install_requires = INSTALL_REQUIRES,
    classifiers = [
        "Development Status :: 4 - Beta",
        "Framework :: Django",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: BSD License",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.2",
        "Programming Language :: Python :: 3.3",
        "Programming Language :: Python :: 3.4",
        "Programming Language :: Python :: 3.5",
        "Topic :: Internet :: WWW/HTTP",
    ]
)
