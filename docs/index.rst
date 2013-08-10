django-sites
============

Alternative implementation of django "sites" framework based on
settings instead of models.

The main motivation for make this package is solve in a simple way to make urls
with correspondig domain in each environment (production, development, etc...)

Also, I consider that use database for store a site configuration, is slighty overkill.

This package do same or similar thing that original "sites" framework of django,
but does not intends to solve the same use cases.


How to install?
---------------

You can install it with pip:

.. code-block:: shell

    pip install django-sites


QuickStart
----------


Put 'django_sites' on your settings.py as first step:

.. code-block:: python

    # settings.py
    INSTALLED_APPS = [
        # ...
        'django_sites',
    ]


As second step, configure your sites and default site id:

.. code-block:: python

    # settings.py
    SITES = {
        1: {"domain": "localhost:8000", "scheme": "http"},
        2: {"domain": "somehost.com", "scheme": "https"},
    }

    # settings_development.py
    # defaut site id for development environment
    SITE_ID = 1

    # settings_production.py
    # defaut site id for production environment
    SITE_ID = 2



Internal documentation
----------------------


.. py:class:: django_sites.Site

    Class that represents a site.

    :var domain: Contains a domain name for this site instance
    :var scheme: Contains a scheme for this site instance


.. py:function:: django_sites.get_current()

    Returns a current site instance, depending
    on :py:attr:`settings.SITE_ID`

    :returns: Site instance
    :rtype: :py:class:`~django_sites.Site`


.. py:function:: django_sites.reverse

    Same as django's reverse but returns a full url
    with domain name and corresponding scheme for current
    configured site.

    .. code-block:: python

        >>> from django_sites import reverse as sites_reverse
        >>> sites_reverse('ns:foo')
        'http://example.com/foo'


Additional notes
----------------

* This package is compatible with django-jinja and automaticaly exposes
  `sites_url` global function on jinja templates context.
