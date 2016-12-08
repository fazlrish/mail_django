from django.db import models
from accounts.models import User
from base.models import Category_item
# Create your models here.


class Review(models.Model):
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True, null=True, blank= True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    category_item = models.ForeignKey(Category_item, on_delete=models.CASCADE, null=True, blank= True)

