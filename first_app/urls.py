from django.conf.urls import url
from first_app import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    # url(r'^users$', views.users, name='users' ),
    url(r'^users/new$', views.new_user, name='New User' ),
    url(r'^users/list$', views.users_list, name='users_list'),
    url(r'^my_form$', views.my_form, name='my_form'),
    url(r'^contact$', views.contact, name='contact')
]