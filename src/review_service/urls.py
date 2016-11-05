from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^users/$', views.UserListView.as_view(), name='users'),
    url(r'^users/(?P<user_id>[0-9]+)/$', views.UserDetailView, name='user'),
    url(r'^$', views.CategoriesView.as_view(), name='categories'),
    url(r'^categories/(?P<category_id>[0-9]+)/$', views.CategoryItemsView.as_view(), name='category'),
    url(r'^categories/(?P<category_id>[0-9]+)/(?P<pk>[0-9]+)/$', views.ItemDetailView, name='item'),
    url(r'^registration/$', views.registration_view, name='registration'),
    url(r'^authorization/$', views.AuthorizationView, name='authorization'),
    url(r'^logout/$', views.LogOutView, name='logout'),
    url(r'^index/$', views.IndexView, name='index')
]
