from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework import viewsets, permissions
from rest_framework.authentication import SessionAuthentication
from rest_framework.permissions import IsAuthenticated

from core.serializers import LoginSystemSerializer
from .models import *

from api.serializers import MemberSerializer,TrainerSerializer,EquipmentSerializer,WorkoutPlanSerializer,MembershipSerializer,GymSerializer,SoftwareMembershipSerializer,StaffSerializer

# Create your views here.
class LoginSystemViewSet(viewsets.ModelViewSet):
    queryset = LoginSystem.objects.all()
    serializer_class = LoginSystemSerializer
    lookup_field = 'pk'
    # permission_classes = [IsAuthenticated]
    # authentication_classes = [SessionAuthentication]

