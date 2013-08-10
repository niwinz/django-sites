# -*- coding: utf-8 -*-

from .. import utils

try:
    from django_jinja.base import Library
    jinja_register = Library()

    def sites_url(name, *args, **kwargs):
        return utils.reverse(name, args=args, kwargs=kwargs)

    jinja_register.global_function("sites_url", sites_url)
except ImportError:
    pass
