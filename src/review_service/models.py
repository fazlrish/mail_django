from __future__ import unicode_literals

from django.db import models

# Create your models here.
class User(models.Model):
    name = models.CharField(max_length=255)
    createdAt = models.DateTimeField(auto_now_add=True, null=True, blank= True)

class Categories(models.Model):
    name = models.CharField(max_length=255)
    createdAt = models.DateTimeField(auto_now_add=True, null=True, blank= True)

class CategoryItem(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    createdAt = models.DateTimeField(auto_now_add=True, null=True, blank= True)
    category = models.ForeignKey(Categories, on_delete=models.CASCADE)


class Review(models.Model):
    text = models.TextField()
    publication_date = models.DateField()
    createdAt = models.DateTimeField(auto_now_add=True, null=True, blank= True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    categoryItem = models.ForeignKey(CategoryItem, on_delete=models.CASCADE, null=True, blank= True)

