# -*- coding: utf-8 -*-

from .. import utils

try:
    from django_jinja.base import Library
    jinja_register = Library()

    def sites_url(name, *args, **kwargs):
        return utils.reverse(name, args=args, kwargs=kwargs)

    def sites_static(path):
        return utils.static(path)

    jinja_register.global_function("sites_url", sites_url)
    jinja_register.global_function("sites_static", sites_static)
except ImportError:
    pass
