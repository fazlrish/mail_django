from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'new_review/',views.new_review_view, name='new_review'),
    url(r'^review_edit/(?P<review_id>[0-9]+)/$', views.review_edit_view, name='review_edit'),
]
