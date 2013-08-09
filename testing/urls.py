# -*- coding: utf-8 -*-

from django.conf.urls import patterns, include, url
from django.views.generic import View


urlpatterns = patterns('',
    url(r'foo$', View.as_view(), name="foo"),
)
