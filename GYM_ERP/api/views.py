from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework import viewsets, permissions
from rest_framework.authentication import SessionAuthentication
from rest_framework.permissions import IsAuthenticated

from core.serializers import LoginSystemSerializer
from api.models import Gym,Member,Trainer,Equipment,WorkoutPlan,Membership,SoftwareMembership,Staff

from api.serializers import MemberSerializer,TrainerSerializer,EquipmentSerializer,WorkoutPlanSerializer,MembershipSerializer,GymSerializer,SoftwareMembershipSerializer,StaffSerializer

class MemberViewSet(viewsets.ModelViewSet):
    queryset = Member.objects.all()
    serializer_class = MemberSerializer
    lookup_field = 'pk'  

    @action(detail=False)
    def me(self, request):
        user_serializer = LoginSystemSerializer(request.user)
        (member_data,created) = Member.objects.get_or_create(username = request.user.username)
        response_data = {
            'user': user_serializer.data,
            'member': member_data.data,
        }
        
        # Return the combined data in the response
        return Response(response_data)


class TrainerViewSet(viewsets.ModelViewSet):
    queryset = Trainer.objects.all()
    serializer_class = TrainerSerializer
    lookup_field = 'pk'
    # permission_classes = [IsAuthenticated]
    # authentication_classes = [SessionAuthentication]

class EquipmentViewSet(viewsets.ModelViewSet):
    queryset = Equipment.objects.all()
    serializer_class = EquipmentSerializer
    lookup_field = 'pk'
    # permission_classes = [IsAuthenticated]
    # authentication_classes = [SessionAuthentication]



class WorkoutPlanViewSet(viewsets.ModelViewSet):
    queryset = WorkoutPlan.objects.all()
    serializer_class = WorkoutPlanSerializer
    lookup_field = 'pk'
    # permission_classes = [IsAuthenticated]
    # authentication_classes = [SessionAuthentication]



class MembershipViewSet(viewsets.ModelViewSet):
    queryset = Membership.objects.all()
    serializer_class = MembershipSerializer
    lookup_field = 'pk'
    # permission_classes = [IsAuthenticated]
    # authentication_classes = [SessionAuthentication]


class GymViewSet(viewsets.ModelViewSet):
    queryset = Gym.objects.all()
    serializer_class = GymSerializer
    lookup_field = 'pk'
    # permission_classes = [IsAuthenticated]
    # authentication_classes = [SessionAuthentication]



class SoftwareMembershipViewSet(viewsets.ModelViewSet):
    queryset = SoftwareMembership.objects.all()
    serializer_class = SoftwareMembershipSerializer
    lookup_field = 'pk'
    # permission_classes = [IsAuthenticated]
    # authentication_classes = [SessionAuthentication]


class StaffViewSet(viewsets.ModelViewSet):
    queryset = Staff.objects.all()
    serializer_class = StaffSerializer
    lookup_field = 'pk'
    # permission_classes = [IsAuthenticated]
    # authentication_classes = [SessionAuthentication]

