from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^add/$', views.add),
    url(r'^remove/$',views.remove),
    url(r'^show/$', views.show),
    url(r'^checkout/$', views.checkout),
    url(r'^clear/$', views.clear)
]