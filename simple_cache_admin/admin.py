from django.contrib import admin
from django.conf.urls import patterns, url

from .models import SimpleCache
from . import views


class SimpleCacheAdmin(admin.ModelAdmin):

    """SimpleCacheAdmin."""

    def has_add_permission(self, request):
        """has_add_permission."""
        return False

    def has_delete_permission(self, request):
        """has_delete_permission."""
        return False

    def get_urls(self):
        """get_urls."""
        urls = super(SimpleCacheAdmin, self).get_urls()
        urlpatterns = patterns(
            'simple_cache_admin.views',
            url(r'^$', self.admin_site.admin_view(views.simple_cache), name='simple_cache_view'),
        )
        return urlpatterns + urls


admin.site.register(SimpleCache, SimpleCacheAdmin)
