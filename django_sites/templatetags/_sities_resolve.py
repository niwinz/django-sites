# -*- coding: utf-8 -*-

from .. import utils

try:
    from django_jinja import library

    @library.global_function
    def sites_url(name, *args, **kwargs):
        site_id = kwargs.pop("site_id", None)
        return utils.reverse(name, args=args, kwargs=kwargs, site_id=site_id)

    @library.global_function
    def sites_static(path, site_id=None):
        return utils.static(path, site_id=site_id)
except ImportError:
    pass
