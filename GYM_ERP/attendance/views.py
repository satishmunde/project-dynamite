from rest_framework import viewsets, permissions
from rest_framework.authentication import SessionAuthentication
from rest_framework.permissions import IsAuthenticated
from .models import *
from .serializers import *

class StaffAttendanceViewSet(viewsets.ModelViewSet):
    queryset = StaffAttendance.objects.all()
    serializer_class = StaffAttendanceSerializer
    lookup_field = 'pk'
    # permission_classes = [IsAuthenticated]
    # authentication_classes = [SessionAuthentication]

class MemberAttendanceViewSet(viewsets.ModelViewSet):
    queryset = MemberAttendance.objects.all()
    serializer_class = MemberAttendanceSerializer
    lookup_field = 'pk'
    # permission_classes = [IsAuthenticated]
    # authentication_classes = [SessionAuthentication]



