from django.urls import path, include
from rest_framework.routers import DefaultRouter

from attendance.views import *


# Create a router and register the viewsets
router = DefaultRouter()

router.register(r'staff-attendance', StaffAttendanceViewSet)
router.register(r'member-attendance', MemberAttendanceViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
