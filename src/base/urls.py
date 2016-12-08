from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^categories/(?P<category_id>[0-9]+)/$', views.Category_items_view.as_view(), name='category'),
    url(r'^categories/([0-9]+)/(?P<pk>[0-9]+)/$', views.Item_detail_view.as_view(), name='item'),
    url(r'^', views.Categories_view.as_view(), name='categories')
]
