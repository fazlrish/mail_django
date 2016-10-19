from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^users/$', views.UserListView.as_view(), name='users'),
    url(r'^users/(?P<user_id>[0-9]+)/$', views.showUserDetail, name='user'),
    url(r'^categories/$', views.CategoriesView.as_view(), name='categories'),
    url(r'^categories/(?P<category_id>[0-9]+)/$', views.showCategoryItems, name='category'),
    url(r'^category/(?P<item_id>[0-9]+)/$', views.showItemDetail, name='item'),
    url(r'^$', views.IndexView.as_view(), name='index')
]
