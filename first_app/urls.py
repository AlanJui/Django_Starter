from django.conf.urls import url
from first_app import views

# Template Tagging
app_name = 'first_app'

urlpatterns = [
    # url(r'^$', views.index, name='index'),
    # url(r'^users$', views.users, name='users' ),
    url(r'^users/new$', views.new_user, name='new_user' ),
    url(r'^users/list$', views.users_list, name='users_list'),
    url(r'^my_form$', views.my_form, name='my_form'),
    url(r'^contact$', views.contact, name='contact'),
    url(r'^relative$', views.relative, name='relative'),
    url(r'^others$', views.others, name='others'),
    url(r'^register/$', views.register, name='register'),
    url(r'^user_login/$', views.user_login, name='user_login'),
    url(r'^cbv/$', views.CBView.as_view()),
    url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'^school_list/$', views.SchoolListView.as_view(), name='school_list'),
    url(r'^school_list/(?P<pk>[-\w]+)/$', views.SchoolDetailView.as_view(), name='school_detail'),
]