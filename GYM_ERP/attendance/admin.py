from django.contrib import admin
from .models import *   
from django.contrib.auth.admin import UserAdmin



# Register your models here.
@admin.register(StaffAttendance)
class StaffAttendanceAdmin(admin.ModelAdmin):
    list_display = ['gym','staff', 'date', 'is_present']

@admin.register(MemberAttendance)
class MemberAttendanceAdmin(admin.ModelAdmin):
    list_display = ['gym','member', 'date', 'is_present']

