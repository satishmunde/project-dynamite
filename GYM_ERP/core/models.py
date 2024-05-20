from django.contrib.auth.models import AbstractUser
from django.db import models

class LoginSystem(AbstractUser):
    USER_TYPE_CHOICES = [
        ('employee', 'Employee'),
        ('owner', 'Software Owner'),
        ('trainer', 'Trainer'),
        ('member', 'Member'),
        ('staff', 'Software Staff'),
        ('other', 'Other'),
    ]

    email = models.EmailField(unique=True)
    user_type = models.CharField(max_length=10, choices=USER_TYPE_CHOICES)
    phone_number = models.CharField(max_length=10, blank=True, null=True)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._meta.get_field('user_type').blank = False  # Make user_type field required
        self._meta.get_field('user_type').null = False
