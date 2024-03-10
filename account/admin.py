from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser

class CustomUserAdmin(UserAdmin):
    # Add customizations for UserAdmin as needed
    pass

admin.site.register(CustomUser, CustomUserAdmin)
