from django.db.models.sql.query import Query
from django.shortcuts import render
from django.views import generic
from .models import *

class IndexView(generic.ListView):
    template_name = "review_service/index.html"
    context_object_name = "userList"

    def get_queryset(self):
        return User.objects.all()

