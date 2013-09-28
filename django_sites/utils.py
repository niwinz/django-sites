# -*- coding: utf-8 -*-

from django.core.urlresolvers import reverse as _reverse
from django.contrib.staticfiles.templatetags.staticfiles import static as _static
from django.utils.functional import lazy

from . import base


def reverse(*args, **kwargs):
    """
    Django-Sities version of reverse method that
    return full urls (with domain, protocol, etc...)
    """

    url = _reverse(*args, **kwargs)
    site = base.get_current()

    url_tmpl = "{scheme}//{domain}{url}"
    scheme = site.scheme and "{0}:".format(site.scheme) or ""
    return url_tmpl.format(scheme=scheme, domain=site.domain, url=url)


def static(path):
    url = _static(path)

    if url.startswith("http"):
        return url

    site = base.get_current()
    url_tmpl = "{scheme}//{domain}{url}"
    scheme = site.scheme and "{0}:".format(site.scheme) or ""
    return url_tmpl.format(scheme=scheme, domain=site.domain, url=url)


reverse_lazy = lazy(reverse, str)
static_lazy = lazy(static, str)
