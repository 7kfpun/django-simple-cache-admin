# django-simple-cache-admin

This a simple cache manager for checking and updating cache value easily in admin.

## Installation

Put ``simple_cache_admin`` in your ``INSTALLED_APPS``.

That's all. Only admin-users with ``superuser`` permission can see.

## Permissions

To use this module, a user must have access to the Django admin panel and have *change* permissions on the
``simple_cache_admin | SimpleCache admin`` model.

Setting *add* or *delete* permissions has no effect, they are always false.

# Settings

In your ``settings.py`` file, you can add a dictionary called ``SIMPLE_CACHE_ADMIN``.

The following key/value settings are available:

TIMEOUT — integer
    The default timeout, in seconds, to use for the cache. This argument default is 3600 seconds (1 hour).

CACHES — string
    A dictionary containing the settings for all caches to be used with Django. It is a nested dictionary whose contents maps cache aliases to a dictionary containing the options for an individual cache. Default is the settings in **django.conf**.
    https://docs.djangoproject.com/en/dev/ref/settings/#std:setting-CACHES

## Screenshots

Overview of simple cache admin.
![django-simple-cache-admin](https://raw.githubusercontent.com/7kfpun/django-simple-cache-admin/master/simple_cache_admin.png)

## License

MIT

## Changelog

**0.1.0:**

    Initial Release.
