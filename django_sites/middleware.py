# -*- coding: utf-8 -*-

from . import base


class SitesMiddleware(object):
    """
    Sites middleware. Attach current site instance to
    current request.
    """

    def process_request(self, request):
        request.site = base.get_current()
