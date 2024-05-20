from django.db import models
from api.models import Gym,Member,Staff

# Create your models here.

class StaffAttendance(models.Model):
    gym = models.ForeignKey(Gym, on_delete=models.PROTECT)
    staff = models.ForeignKey(Staff, on_delete=models.PROTECT)
    date = models.DateField()
    is_present = models.BooleanField(default=False)


    def __str__(self):
        return f"{self.staff.staff_name} - {self.date} - Present: {self.is_present}"

class MemberAttendance(models.Model):
    gym = models.ForeignKey(Gym, on_delete=models.PROTECT)
    member = models.ForeignKey(Member, on_delete=models.PROTECT)
    date = models.DateField()
    is_present = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.member.member_name} - {self.date} - Present: {self.is_present}"