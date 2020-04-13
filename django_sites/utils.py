# -*- coding: utf-8 -*-

try:
    # For django >= 3.0
    from django.templatetags.static import static as _static
except ImportError:
    from django.contrib.staticfiles.templatetags.staticfiles import static as _static
from django.utils.functional import lazy

try:
    # For django >= 2.0
    from django.urls import reverse as _reverse
except ImportError:
    from django.core.urlresolvers import reverse as _reverse

from . import base


def reverse(viewname, args=None, kwargs=None, site_id=None):
    """
    Django-Sities version of reverse method that
    return full urls (with domain, protocol, etc...)
    """

    if site_id is None:
        site = base.get_current()
    else:
        site = base.get_by_id(site_id)

    url = _reverse(viewname, args=args, kwargs=kwargs)
    return get_absolute_url_for_site(url, site)


def static(path, site_id=None):
    url = _static(path)

    if url.startswith("http"):
        return url

    if site_id is None:
        site = base.get_current()
    else:
        site = base.get_by_id(site_id)

    return get_absolute_url_for_site(url, site)


def get_absolute_url_for_site(url, site):
    url_tmpl = "{scheme}//{domain}{url}"
    scheme = site.scheme and "{0}:".format(site.scheme) or ""
    return url_tmpl.format(scheme=scheme, domain=site.domain, url=url)


reverse_lazy = lazy(reverse, str)
static_lazy = lazy(static, str)
