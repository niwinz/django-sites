# -*- coding: utf-8 -*-

import sys, os
import django

from django.conf import settings

test_settings = {
    "DATABASES":{
        "default": {
            "ENGINE": "django.db.backends.sqlite3",
        }
    },
    "INSTALLED_APPS": [
        "django.contrib.auth",
        "django.contrib.contenttypes",
        "django.contrib.sessions",
        "django.contrib.staticfiles",
        "django.contrib.messages",
        "django_sites",
        "django_jinja",
    ],
    "ROOT_URLCONF":"testing.urls",
    "USE_I18N": True,
    "USE_TZ": True,
    "TEMPLATE_LOADERS": [
        "django_jinja.loaders.AppLoader",
        "django_jinja.loaders.FileSystemLoader",
    ],

    "STATIC_URL": "/static/",
    "LANGUAGE_CODE":"en",
    "MIDDLEWARE_CLASSES": (
        "django.middleware.common.CommonMiddleware",
        "django.contrib.sessions.middleware.SessionMiddleware",
        "django.middleware.csrf.CsrfViewMiddleware",
        "django.contrib.auth.middleware.AuthenticationMiddleware",
        "django.contrib.messages.middleware.MessageMiddleware",
    ),
    "MANAGERS": ("niwi@niwi.be",),
    "SITES": {
        "foo": {"domain": "example1.com", "name": "example1.com", "scheme": "https"},
        "bar": {"domain": "example2.com", "name": "example2.com"}
    },
    "SITE_ID": "foo",
}


if django.VERSION[:2] >= (1, 6):
    test_settings["TEST_RUNNER"] = "django.test.runner.DiscoverRunner"


if __name__ == "__main__":
    from django.core.management import execute_from_command_line

    if not settings.configured:
        settings.configure(**test_settings)

    args = sys.argv
    args.insert(1, "test")

    if django.VERSION[:2] < (1, 6):
        args.insert(2, "django_sites")

    execute_from_command_line(args)
