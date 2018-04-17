from django.conf.urls import url
from . import views


urlpatterns = [

    url(r'^$', views.index),
    url(r'^restfulusers/$', views.index),
    url(r'^restfulusers/add/$', views.add),
    url(r'^restfulusers/(?P<user_id>\d+)/edit/$', views.edit),
    url(r'^restfulusers/(?P<user_id>\d+)/$', views.show),
    url(r'^restfulusers/create/$', views.create),
    url(r'^restfulusers/(?P<user_id>\d+)/destroy/$', views.destroy),
    url(r'^restfulusers/update/$', views.update),
]