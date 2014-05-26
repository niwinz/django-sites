# -*- coding: utf-8 -*-

from django.core.exceptions import ImproperlyConfigured


class SitesNotConfigured(ImproperlyConfigured):
    pass


class SiteNotFound(ImproperlyConfigured):
    pass
