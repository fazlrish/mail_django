from django.conf.urls import url
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    url(r'^users/$', views.UserListView.as_view(), name='users'),
    url(r'^users/(?P<user_id>[0-9]+)/$', views.UserDetailView, name='user'),
    url(r'^registration/$', views.registration_view, name='registration'),
    url(r'^login/$', auth_views.login, {'template_name':'accounts/login.html'}, name='login'),
    url(r'^logout/$', auth_views.logout, {'template_name':'accounts/logout.html'}, name='logout'),
]
