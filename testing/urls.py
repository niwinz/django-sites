# -*- coding: utf-8 -*-

from django.conf.urls import url
from django.views.generic import View


urlpatterns = [
    url(r'foo$', View.as_view(), name="foo"),
]
