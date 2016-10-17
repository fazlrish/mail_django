from django.db.models.sql.query import Query
from django.shortcuts import render
from django.views import generic
from .models import *

class IndexView(generic.View):
    template_name = "review_service/index.html"

class UserListView(generic.ListView):
    template_name = "review_service/userList.html"
    context_object_name = "userList"
    def get_queryset(self):
        return User.objects.all()

class CategoriesView(generic.ListView):
    template_name = "review_service/categories.html"
    context_object_name = "categories"
    def get_queryset(self):
        return Categories.objects.all()

