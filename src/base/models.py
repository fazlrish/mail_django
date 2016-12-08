from django.db import models

# Create your models here.
class Categories(models.Model):
    name = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True, null=True, blank= True)
    def __unicode__(self):
        return self.name


class Category_item(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True, null=True, blank= True)
    category = models.ForeignKey(Categories, on_delete=models.CASCADE)
    def __unicode__(self):
        return self.name
