from django.contrib import admin
from models import Review
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
# Register your models here.
admin.site.register(Review)
