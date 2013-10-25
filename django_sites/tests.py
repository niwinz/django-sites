# -*- coding: utf-8 -*-

import unittest

from django.test.utils import override_settings
from django_sites.exceptions import SitesNotConfigured
from django_sites import base
from django_sites import utils


class BasicSitesTests(unittest.TestCase):
    @override_settings(SITES=None)
    def test_get_sites_config_01(self):
        with self.assertRaises(SitesNotConfigured):
            config = base._get_sites_config()

    def test_get_sites_config_02(self):
        config = base._get_sites_config()
        self.assertEqual(config,
            {
                1: {'domain': 'example1.com', 'name': 'example1.com', 'scheme': 'https'},
                2: {'domain': 'example2.com', 'name': 'example2.com'}
            })

    @override_settings(SITES=None)
    def test_get_current_site_01(self):
        with self.assertRaises(SitesNotConfigured):
            site = base.get_current()

    @override_settings(SITE_ID=1)
    def test_get_current_site_02(self):
        site = base.get_current()
        self.assertEqual(site.domain, "example1.com")
        self.assertEqual(site.name, "example1.com")

    @override_settings(SITE_ID=1)
    def test_get_current_site_03(self):
        site = base.get_current()
        self.assertEqual(site.scheme, "https")

    @override_settings(SITE_ID=2)
    def test_get_current_site_04(self):
        site = base.get_current()
        self.assertEqual(site.domain, "example2.com")
        self.assertEqual(site.name, "example2.com")

    @override_settings(SITE_ID=2)
    def test_get_current_site_05(self):
        site = base.get_current()
        self.assertEqual(site.scheme, "")

    @override_settings(SITE_ID=2, DJANGO_SITES_DEFAULT_SCHEME="http")
    def test_get_current_site_06(self):
        site = base.get_current()
        self.assertEqual(site.scheme, "http")


class ReverseTests(unittest.TestCase):
    @override_settings(SITE_ID=2)
    def test_reverse_01(self):
        url = utils.reverse("foo")
        self.assertEqual(url, "//example2.com/foo")

    @override_settings(SITE_ID=2, DJANGO_SITES_DEFAULT_SCHEME="http")
    def test_reverse_02(self):
        url = utils.reverse("foo")
        self.assertEqual(url, "http://example2.com/foo")

    @override_settings(SITE_ID=1, DJANGO_SITES_DEFAULT_SCHEME="http")
    def test_reverse_03(self):
        url = utils.reverse("foo")
        self.assertEqual(url, "https://example1.com/foo")
