from django.conf.urls import url 
from . import views

urlpatterns = [
    url(r'^$', views.index),    #done
    url(r'^register_account/$', views.register_account), #done
    url(r'^logout_user/$', views.logout),       #done
    url(r'^login2account/$', views.login),      #done
    url(r'^add/$', views.add),      #done
    url(r'^addBook$', views.book_add),
    url(r'^addReview$', views.review_add),
    url(r'^book/(?P<book_id>\d+)$', views.show_book), #done
    url(r'^users/(?P<user_id>\d+)$', views.user_show),    
    url(r'^destroy/(?P<review_id>\d+)$', views.destroy),
    url(r'^home/$', views.home),
]
