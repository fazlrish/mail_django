from django.contrib import admin

# Register your models here.
from base.models import Categories, Category_item

admin.site.register(Categories)
admin.site.register(Category_item)
