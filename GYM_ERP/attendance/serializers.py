from datetime import timezone
from rest_framework import serializers
from attendance.models import *



class StaffAttendanceSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = StaffAttendance
        fields = ['gym', 'staff', 'date', 'is_present']


class MemberAttendanceSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = MemberAttendance
        fields = ['gym', 'member', 'date', 'is_present']
