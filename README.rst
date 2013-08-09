django-sites
============

Alternative implementation of django "sites" framework based on
settings instead of models.

The main motivation for make this package is solve in a simple way make urls
with correspondig domain in each environment (production, development, etc...)
Also, use database for store a site configuration, I this that is sligty overkill.

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
        'django_sities',
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

.. py:function:: django_sites.get_current()

    Returns a current site instance, depending
    on :py:attr:`settings.SITE_ID`

    :returns: Site instance
    :rtype: :py:class:`~django_sites.Site`
