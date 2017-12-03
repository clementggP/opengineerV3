from django.conf.urls import url
from . import views
from django.contrib.sitemaps.views import sitemap
from home.sitemaps import StaticSitemap

sitemaps = {'static': StaticSitemap}
urlpatterns = [
    url(r'^$', views.home, name='home_url'),
    url(r'^sitemap.xml$', sitemap, {'sitemaps': sitemaps}, name='django.contrib.sitemaps.views.sitemap')
]
#test
