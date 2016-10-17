from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^users', views.UserListView.as_view(), name='users'),
    url(r'^categories', views.CategoriesView.as_view(), name='categories'),
    url(r'^categories/^(?P<pk>[0-9]+)/$', views.CategoriesView.as_view(), name='categories'),
    url(r'^$', views.IndexView.as_view(), name='index')

]
