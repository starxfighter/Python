from django.conf.urls import url 
from . import views

urlpatterns = [
    # login and registration routes
    url(r'^$', views.index),    
    url(r'^register_account/$', views.register_account), 
    url(r'^logout_user/$', views.logout),       
    url(r'^login2account/$', views.login),  
    # add and show routes    
    url(r'^add/$', views.add),      
    url(r'^addBook$', views.book_add),
    url(r'^addReview$', views.review_add),
    url(r'^home/$', views.home),
    # specific interaction routes
    url(r'^book/(?P<book_id>\d+)$', views.show_book), 
    url(r'^users/(?P<user_id>\d+)$', views.user_show),    
    url(r'^destroy/(?P<review_id>\d+)$', views.destroy),
    
]
