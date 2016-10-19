from django.db.models.sql.query import Query
from django.shortcuts import render
from django.views import generic
from django.views.generic.base import TemplateView
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


def showCategoryItems(request, category_id):
    template_name = "review_service/category.html"
    listOfItems = CategoryItem.objects.filter(category_id=category_id)
    return render(request, template_name, {'categoryItemList': listOfItems})


def showItemDetail(request, item_id):
    template_name = "review_service/itemDetail.html"
    item = CategoryItem.objects.get(pk=item_id)
    reviews = Review.objects.filter(categoryItem=item_id)
    return render(request, template_name, {'item': item,'reviews':reviews})

def showUserDetail(request, user_id):
    template_name = "review_service/userDetail.html"
    user = User.objects.get(pk=user_id)
    reviews = Review.objects.filter(user=user_id)
    return render(request, template_name, {'user': user,'reviews':reviews})

# def addReview(request, item_id):
#     item = CategoryItem.objects.get(pk = item_id)
#     try:
#         newReview = item.review_set.get()
