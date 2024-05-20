from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib import admin
from core.models import *

@admin.register(LoginSystem)
class LoginSystemAdmin(BaseUserAdmin):

    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'password1', 'password2', 'email', 'phone_number','user_type', 'is_active')}
        ),
    )
    list_display = ('username', 'user_type','email', 'first_name', 'last_name')
    search_fields = ('username', 'email','user_type' ,'first_name', 'last_name')
    ordering = ('username',)