#encoding: utf-8

from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from seek import views


urlpatterns = [
    url(r'^maps/list/$', views.MapsList.as_view()),
    url(r'^maps/(?P<string>[\w\-]+)/$', views.MapsCustom.as_view()),

    url(r'^routes/list/$', views.RoutesList.as_view()),
    url(r'^routes/(?P<pk>[0-9]+)/$', views.RoutesCustomName.as_view()),

    url(r'^routes/price_route/$','seek.views.price_route',name='price_route'),
]

urlpatterns = format_suffix_patterns(urlpatterns)