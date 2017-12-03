from django.core.urlresolvers import reverse
from django.contrib.sitemaps import Sitemap


class StaticSitemap(Sitemap):
    """Reverse 'static' views for XML sitemap."""

    def items(self):
        # Return list of url names for views to include in sitemap
        return ['home_url']

    def location(self, item):
        return reverse(item)
