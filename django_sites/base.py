# -*- coding: utf-8 -*-

from django.conf import settings
from django.utils.functional import cached_property

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


def get_by_id(id):
    """
    Get site instance from settings configuration.
    """
    sites = _get_sites_config()

    try:
        return Site(sites[id])
    except KeyError:
        raise exceptions.SiteNotFound("Site with id '{}' not found".format(id))


def get_current():
    """
    Get current site.
    """
    return get_site_from_settings()
