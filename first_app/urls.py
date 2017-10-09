from django.conf.urls import url
from first_app import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^users/$', views.users, name='users' ),
    url(r'^my_form/$', views.my_form, name='myForm')
]