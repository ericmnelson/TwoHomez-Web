from django.conf.urls import url

from . import views

urlpatterns = [
    # ex: /homes/5/
    url(r'^homes/(?P<home_id>[0-9]+)/details/$', views.home_detail, name='home_detail'),
    # ex: /search_listings
    url(r'^search_listings/$', views.search_listings, name='search_listings'),
    # ex: /
    url(r'^$', views.index, name='index'),
]
