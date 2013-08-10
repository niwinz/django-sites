# -*- coding: utf-8 -*-

from .. import utils

try:
    from django_jinja.base import Library
    jinja_register = Library()
    jinja_register.global_function("sites_reverse", utils.reverse)
except ImportError:
    pass
