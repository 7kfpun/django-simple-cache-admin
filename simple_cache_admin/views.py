from django import forms
from django.conf import settings
from django.core.cache import caches, get_cache
from django.shortcuts import render

import logging
import os

logger = logging.getLogger(__name__)

SETTINGS = {
    'TIMEOUT': 60 * 60,
    'CACHES': settings.CACHES,
}
if hasattr(settings, 'SIMPLE_CACHE_ADMIN'):
    SETTINGS = dict(SETTINGS.items() + settings.SIMPLE_CACHE_ADMIN.items())


class SimpleCacheForm(forms.Form):

    """SimpleCacheForm."""

    ACTIONS = (
        ('GET', 'GET'),
        ('UPDATE', 'UPDATE'),
        ('DELETE', 'DELETE'),
        ('FLUSH', 'FLUSH'),
    )
    CACHE_POOLS = ((pool, pool) for pool in sorted(SETTINGS['CACHES']))

    pool = forms.ChoiceField(choices=CACHE_POOLS)
    action = forms.ChoiceField(choices=ACTIONS)
    key = forms.CharField(label='Cache key', required=False, max_length=100)
    timeout = forms.IntegerField(initial=SETTINGS['TIMEOUT'], min_value=0)
    value = forms.CharField(label='New value', widget=forms.Textarea, required=False)


def _flush(client):
    try:
        client._cache.flush_all()
    except:
        pass

    try:
        for dirname in client._list_cache_files():
            os.remove(dirname)
    except:
        pass


def simple_cache(request, *args, **kwargs):
    """Cache_admin view."""
    form = SimpleCacheForm()
    show_value = ''

    if request.method == 'POST':
        pool = request.POST.get('pool')
        action = request.POST.get('action')
        key = request.POST.get('key')
        value = request.POST.get('value')
        timeout = int(request.POST.get('timeout'))

        if action == 'GET':
            caches[pool].get(key)
        elif action == 'UPDATE':
            caches[pool].set(key, value, timeout)
        elif action == 'DELETE':
            caches[pool].delete(key)
        elif action == 'FLUSH':
            client = get_cache(pool)
            _flush(client)

        show_value = caches[pool].get(key)
        logging.debug(show_value)

        form = SimpleCacheForm(request.POST)

    return render(request, 'simple_cache_admin/index.html', {
        'form': form,
        'value': show_value,
    })
