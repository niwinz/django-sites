# -*- coding: utf-8 -*-

from functools import partial

from django.utils.functional import memoize as _memoize, cached_property
from django.conf import settings

from . import exceptions


class Site(object):
    def __init__(self, config):
        self._config = config

    @cached_property
    def domain(self):
        try:
            domain = self._config.get("domain")
        except AttributeError:
            raise exceptions.SitesNotConfigured("site has wrong configuration")
        else:
            return domain

    @cached_property
    def scheme(self):
        scheme = self._config.get('scheme', None)
        if scheme is None:
            scheme = getattr(settings, "DJANGO_SITES_DEFAULT_SCHEME", "")
        return scheme

    @cached_property
    def name(self):
        try:
            name = self._config.get("name")
        except AttributeError:
            raise exceptions.SitesNotConfigured("site has wrong configuration")
        else:
            return name


def memoize(function=None, args=0):
    """
    Decorator version of django memoize
    function.
    """

    if function is None:
        return partial(memoize, args=args)
    return _memoize(function, function.__dict__, args)


def _get_sites_config():
    sites = getattr(settings, "SITES", None)
    if not sites:
        raise exceptions.SitesNotConfigured("SITES settings not found")
    return sites


def get_site_from_settings():
    """
    Get site instance from settings
    configuration.
    """
    sites = _get_sites_config()

    try:
        current_site_id = getattr(settings, "SITE_ID")
    except AttributeError:
        raise exceptions.SitesNotConfigured()

    if current_site_id not in sites:
        raise exceptions.SitesNotConfigured()

    return Site(sites[current_site_id])


def get_current():
    """
    Get current site.
    """
    return get_site_from_settings()
