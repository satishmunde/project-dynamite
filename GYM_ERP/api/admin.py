from django.contrib import admin
from api.models import Gym,Member,Trainer,Equipment,WorkoutPlan,Membership,SoftwareMembership,Staff


from django.contrib.auth.admin import UserAdmin




@admin.register(Member)
class MemberAdmin(admin.ModelAdmin):
    list_display = ('member_id','member_name', 'member_gender', 'member_age', 'member_address')
    
    readonly_fields = ('member_qr','member_id')

@admin.register(Trainer)
class TrainerAdmin(admin.ModelAdmin):
    list_display = ('trainer_name', 'speciality', 'years_of_experience', 'gender', 'certification')
    readonly_fields = ('trainer_qr','trainer_id')

@admin.register(Equipment)
class EquipmentAdmin(admin.ModelAdmin):
    list_display = ('name', 'quantity', 'category', 'manufacturer', 'condition')

@admin.register(WorkoutPlan)
class WorkoutPlanAdmin(admin.ModelAdmin):
    list_display = ('title', 'trainer', 'duration_in_weeks', 'price', 'target_audience', 'difficulty_level')

@admin.register(Membership)
class MembershipAdmin(admin.ModelAdmin):
    list_display = ('member', 'plan', 'start_date', 'end_date', 'price_paid', 'payment_method', 'is_active')

@admin.register(Gym)
class GymAdmin(admin.ModelAdmin):
    list_display = ( 'gym_name', 'owner_name', 'establishment_date', 'website')
    # search_fields = ['gym_id', 'gym_name', 'owner_name']
    # list_filter = ('establishment_date',)
    readonly_fields = ('gym_qr','gym_id')
    
    
@admin.register(SoftwareMembership)
class SoftwareMembershipAdmin(admin.ModelAdmin):
    list_display = ('gym_owner', 'license_key', 'license_expiry_date', 'payment_method', 'active_users_count')


@admin.register(Staff)
class StaffAdmin(admin.ModelAdmin):
    list_display = ('staff_name', 'staff_gender', 'staff_age', 'staff_position', 'staff_salary', 'staff_date_of_hire', 'gym')
    readonly_fields = ('staff_qr','staff_id')



