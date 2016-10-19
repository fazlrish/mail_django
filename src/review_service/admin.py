from django.contrib import admin
from models import *
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
# Register your models here.
admin.site.register(User)
admin.site.register(Categories)
admin.site.register(CategoryItem)
admin.site.register(Review)
