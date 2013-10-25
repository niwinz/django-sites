# -*- coding: utf-8 -*-

import sys, os
from django.conf import settings
from django.core.management import call_command

#RUNTESTS_DIR = os.path.abspath(os.path.dirname(__file__))
#sys.path.insert(0, PREVIOUS_DIR)


test_settings = {
    'DATABASES':{
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
        }
    },
    'INSTALLED_APPS': [
        'django.contrib.auth',
        'django.contrib.contenttypes',
        'django.contrib.sessions',
        'django.contrib.staticfiles',
        'django.contrib.messages',
        'django_sites',
    ],
    'ROOT_URLCONF':'testing.urls',
    'USE_I18N': True,
    'USE_TZ': True,
    'LANGUAGE_CODE':'en',
    'MIDDLEWARE_CLASSES': (
        'django.middleware.common.CommonMiddleware',
        'django.contrib.sessions.middleware.SessionMiddleware',
        'django.middleware.csrf.CsrfViewMiddleware',
        'django.contrib.auth.middleware.AuthenticationMiddleware',
        'django.contrib.messages.middleware.MessageMiddleware',
    ),
    'MANAGERS': ("niwi@niwi.be",),
    'SITES': {
        1: {"domain": "example1.com", "name": "example1.com", "scheme": "https"},
        2: {"domain": "example2.com", "name": "example2.com"}
    },
    "SITE_ID": 1,
}


if __name__ == '__main__':
    test_args = sys.argv[1:]

    if not settings.configured:
        settings.configure(**test_settings)

    if not test_args:
        test_args = ['django_sites']

    call_command("test", *test_args, verbosity=2)
