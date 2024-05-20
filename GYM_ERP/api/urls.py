from django.urls import path, include
from rest_framework.routers import DefaultRouter
from api.views import *




# Create a router and register the viewsets
router = DefaultRouter()
router.register(r'members', MemberViewSet)
router.register(r'trainers', TrainerViewSet)
router.register(r'equipment', EquipmentViewSet)
router.register(r'workout-plans', WorkoutPlanViewSet)
router.register(r'memberships', MembershipViewSet)
router.register(r'gyms', GymViewSet)
router.register(r'software-memberships', SoftwareMembershipViewSet)
router.register(r'staff', StaffViewSet)

urlpatterns = [
    path('', include(router.urls)),
  
]
