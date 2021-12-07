# -*- coding: utf-8 -*-

import unittest

import django

from django_sites import base, utils
from django_sites.exceptions import SitesNotConfigured

if django.VERSION[:2] < (1, 7):
    from django.test.utils import override_settings
else:
    from django.test import override_settings

if django.VERSION[:2] >= (1, 8):
    from django.template import engines
    env = engines["jinja2"]
else:
    from django_jinja.base import env


class BasicSitesTests(unittest.TestCase):
    @override_settings(SITES=None)
    def test_get_sites_config_01(self):
        with self.assertRaises(SitesNotConfigured):
            base._get_sites_config()

    def test_get_sites_config_02(self):
        config = base._get_sites_config()
        self.assertEqual(config, {
                "foo": {'domain': 'example1.com', 'name': 'example1.com', 'scheme': 'https'},
                "bar": {'domain': 'example2.com', 'name': 'example2.com'}
            })

    @override_settings(SITES=None)
    def test_get_current_site_01(self):
        with self.assertRaises(SitesNotConfigured):
            base.get_current()

    @override_settings(SITE_ID="foo")
    def test_get_current_site_02(self):
        site = base.get_current()
        self.assertEqual(site.domain, "example1.com")
        self.assertEqual(site.name, "example1.com")

    @override_settings(SITE_ID="foo")
    def test_get_current_site_03(self):
        site = base.get_current()
        self.assertEqual(site.scheme, "https")

    @override_settings(SITE_ID="bar")
    def test_get_current_site_04(self):
        site = base.get_current()
        self.assertEqual(site.domain, "example2.com")
        self.assertEqual(site.name, "example2.com")

    @override_settings(SITE_ID="bar")
    def test_get_current_site_05(self):
        site = base.get_current()
        self.assertEqual(site.scheme, "")

    @override_settings(SITE_ID="bar", DJANGO_SITES_DEFAULT_SCHEME="http")
    def test_get_current_site_06(self):
        site = base.get_current()
        self.assertEqual(site.scheme, "http")

    def test_get_by_id(self):
        site = base.get_by_id("bar")
        self.assertEqual(site.domain, "example2.com")
        self.assertEqual(site.name, "example2.com")


class JinjaTemplateTests(unittest.TestCase):
    @override_settings(SITE_ID="bar", DJANGO_SITES_DEFAULT_SCHEME="http")
    def test_template_sites_url_functions(self):
        url = env.from_string("{{ sites_url('foo') }}").render({})
        self.assertEqual(url, "http://example2.com/foo")

        url = env.from_string("{{ sites_url('foo', site_id='foo') }}").render({})
        self.assertEqual(url, "https://example1.com/foo")

    @override_settings(SITE_ID="bar", DJANGO_SITES_DEFAULT_SCHEME="http")
    def test_template_static_url_functions(self):
        url = env.from_string("{{ sites_static('lib.js') }}").render({})
        self.assertEqual(url, "http://example2.com/static/lib.js")

        url = env.from_string("{{ sites_static('libs.js', site_id='foo') }}").render({})
        self.assertEqual(url, "https://example1.com/static/libs.js")


class ReverseTests(unittest.TestCase):
    @override_settings(SITE_ID="bar")
    def test_reverse_01(self):
        url = utils.reverse("foo")
        self.assertEqual(url, "//example2.com/foo")

    @override_settings(SITE_ID="bar", DJANGO_SITES_DEFAULT_SCHEME="http")
    def test_reverse_02(self):
        url = utils.reverse("foo")
        self.assertEqual(url, "http://example2.com/foo")

    @override_settings(SITE_ID="foo", DJANGO_SITES_DEFAULT_SCHEME="http")
    def test_reverse_03(self):
        url = utils.reverse("foo")
        self.assertEqual(url, "https://example1.com/foo")

    def test_reverse_04(self):
        url = utils.reverse("foo", site_id="foo")
        self.assertEqual(url, "https://example1.com/foo")
        url = utils.reverse("foo", site_id="bar")
        self.assertEqual(url, "//example2.com/foo")
