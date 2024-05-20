from django.conf import settings
from django.db import models
from django.conf import settings
from PIL import Image
from pathlib import Path
import qrcode

def generate_qr_code(data):
    # Generate QR code based on the provided data
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=3,
        border=1,
    )
    qr.add_data(data)   
    qr.make(fit=True)
    img = qr.make_image(fill_color="black", back_color="white")
    
    # Determine the directory and filename based on the data
    qr_code_directory = 'media/'  # Adjust this path as needed
    if 'member_id' in data:
        qr_code_directory += 'member_qr/'
        filename = f"{data['member_id']}.jpg"
    elif 'trainer_id' in data:
        qr_code_directory += 'trainer_qr/'
        filename = f"{data['trainer_id']}.jpg"
    elif 'staff_id' in data:
        qr_code_directory += 'staff_qr/'
        filename = f"{data['staff_id']}.jpg"
    elif 'gym_id' in data:
        qr_code_directory += 'gym_qr/'
        filename = f"{data['gym_id']}.jpg"
    else:
        # Handle the case where none of the IDs are present in the data
        return None
    
    # Create directory if it doesn't exist
    qr_code_path = Path(qr_code_directory)
    qr_code_path.mkdir(parents=True, exist_ok=True)

    # Save the QR code image
    img.save(qr_code_path / filename)
    
    # Return the path to the saved QR code imageprin
    
    print(qr_code_path / filename)
    
    
    return str(qr_code_path / filename)


    
def generate_gym_id():
    latest_gym = Gym.objects.order_by('gym_id').last()
    if latest_gym:
        latest_number = int(latest_gym.gym_id[3:]) + 1
    else:
        latest_number = 1
    return f"GYM{latest_number:05}"


class Gym(models.Model):
    user_name = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.PROTECT, null=True, blank=True)
    gym_id = models.CharField(primary_key=True, max_length=8,default=generate_gym_id)
    gym_name = models.CharField(max_length=100)
    owner_name = models.CharField(max_length=250)
    gym_address = models.TextField()
    establishment_date = models.DateField()
    website = models.URLField(null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    logo = models.ImageField(upload_to='gym_logos/',null=True, blank=True)
    gym_qr = models.ImageField(upload_to='gym_qr/', blank=True)  # Field to store the path to the QR code image


    
    
    def save(self, *args, **kwargs):
        data_dict = {field.attname: getattr(self, field.attname) for field in self._meta.fields}
        qr_code_path = generate_qr_code(data_dict)
        if qr_code_path:
            self.gym_qr = qr_code_path.replace('media', '')

        super().save(*args, **kwargs)

    def __str__(self):
        return self.gym_name

def generate_member_id():
    latest_mem = Member.objects.order_by('member_id').last()
    if latest_mem:
        latest_number = int(latest_mem.member_id[3:]) + 1
        print(latest_number)
    else:
        latest_number = 1
    return f"MEM{latest_number:05}"

class Member(models.Model):
    user_name = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.PROTECT,null=True, blank=True)

    member_id = models.CharField(max_length=8,primary_key=True,default=generate_member_id)
    gym = models.ForeignKey(Gym, on_delete=models.PROTECT)
    member_name = models.CharField(max_length=250)
    GENDER_CHOICES = [
        ('M', 'Male'),
        ('F', 'Female'),
        ('O', 'Other'),
    ]
    member_gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    member_age = models.IntegerField()
    member_weight = models.FloatField()
    member_height = models.IntegerField()
    member_date_of_birth = models.DateField()
    member_address = models.CharField(max_length=100)
    # member_phone_number = models.CharField(max_length=15)
    # member_email = models.EmailField()
    member_photo = models.ImageField(upload_to='member_photos/')
    member_qr = models.ImageField(upload_to='member_qr/')

    def __str__(self):
        return self.member_name


    
    def save(self, *args, **kwargs):
        print('calling save function ')
        data_dict = {field.attname: getattr(self, field.attname) for field in self._meta.fields}
        print(data_dict)
        qr_code_path = generate_qr_code(data_dict)
        if qr_code_path:
            self.member_qr = qr_code_path.replace('media', '')

        super().save(*args, **kwargs)

def generate_trainer_id():
    latest_trainer = Trainer.objects.order_by('trainer_id').last()
    if latest_trainer:
        latest_number = int(latest_trainer.trainer_id[3:]) + 1
        print(latest_number)
    else:
        latest_number = 1
    return f"TRN{latest_number:05}"

class Trainer(models.Model):
    user_name = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.PROTECT,null=True, blank=True)
    trainer_id = models.CharField(max_length=8,primary_key=True,default=generate_trainer_id)
    gym = models.ForeignKey(Gym, on_delete=models.PROTECT)
    trainer_name = models.CharField(max_length=250)
    speciality = models.CharField(max_length=100)
    years_of_experience = models.IntegerField()
    age = models.PositiveIntegerField()
    GENDER_CHOICES = [
        ('M', 'Male'),
        ('F', 'Female'),
        ('O', 'Other'),
    ]
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    certification = models.CharField(max_length=250)
    contact_number = models.CharField(max_length=20)
    # email = models.EmailField()
    address = models.CharField(max_length=250)

    profile_picture = models.ImageField(upload_to='trainer_profile_pics/', null=True, blank=True)
    trainer_qr = models.ImageField(upload_to='trainer_qr/', null=True, blank=True)

    def __str__(self):
        return self.trainer_name
    
    def save(self, *args, **kwargs):
        print('calling save function ')
        data_dict = {field.attname: getattr(self, field.attname) for field in self._meta.fields}
        print(data_dict)
        qr_code_path = generate_qr_code(data_dict)
        if qr_code_path:
            self.trainer_qr = qr_code_path.replace('media', '')

        super().save(*args, **kwargs)

class Equipment(models.Model):
    gym = models.ForeignKey(Gym, on_delete=models.PROTECT,null=True, blank=True)
    name = models.CharField(max_length=100)
    description = models.TextField()
    quantity = models.IntegerField()
    category = models.CharField(max_length=100)
    manufacturer = models.CharField(max_length=100)
    purchase_date = models.DateField()
    warranty_expiry = models.DateField(null=True, blank=True)
    CONDITION_CHOICES = [
        ('New', 'New'),
        ('Used', 'Used'),
    ]
    condition = models.CharField(max_length=4, choices=CONDITION_CHOICES)
    location = models.CharField(max_length=150, null=True, blank=True)
    photo = models.ImageField(upload_to='equipment_photos/', null=True, blank=True)

    def __str__(self):
        return self.name

class WorkoutPlan(models.Model):
    gym = models.ForeignKey(Gym, on_delete=models.PROTECT,null=True, blank=True)
    title = models.CharField(max_length=100)
    description = models.TextField()
    trainer = models.ForeignKey(Trainer, on_delete=models.PROTECT)
    duration_in_weeks = models.IntegerField()
    price = models.DecimalField(max_digits=8, decimal_places=2)
    target_audience = models.CharField(max_length=100)
    difficulty_level = models.CharField(max_length=50)
    goals = models.TextField()
    included_equipment = models.ManyToManyField(Equipment, related_name='workout_plans')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    photo = models.ImageField(upload_to='workout_plan_photos/', null=True, blank=True)

    def __str__(self):
        return self.title

class Membership(models.Model):
    gym = models.ForeignKey(Gym, on_delete=models.PROTECT)
    member = models.ForeignKey(Member, on_delete=models.PROTECT)
    plan = models.ForeignKey(WorkoutPlan, on_delete=models.PROTECT)
    start_date = models.DateField()
    end_date = models.DateField()
    price_paid = models.DecimalField(max_digits=8, decimal_places=2)
    payment_method = models.CharField(max_length=50)
    is_active = models.BooleanField(default=True)
    notes = models.TextField(null=True, blank=True)

    def __str__(self):
        return f"{self.member.user.username}'s membership"

class SoftwareMembership(models.Model):
    gym_owner = models.ForeignKey(Gym, on_delete=models.PROTECT)
    license_key = models.CharField(max_length=50)
    license_expiry_date = models.DateField()
    payment_method = models.CharField(max_length=50)
    billing_address = models.TextField()
    payment_confirmation = models.FileField(upload_to='payment_confirmations/')
    gym_contact_number = models.CharField(max_length=20)
    gym_email = models.EmailField()
    active_users_count = models.IntegerField()
    training_and_support_requests = models.TextField()
    admin_username = models.CharField(max_length=50)
    admin_email = models.EmailField()
    admin_password = models.CharField(max_length=50)
    integration_preferences = models.TextField(blank=True)
    usage_agreement = models.FileField(upload_to='usage_agreements/')
    feedback_on_features = models.TextField(blank=True)
    improvement_suggestions = models.TextField(blank=True)

    def __str__(self):
        return f"{self.gym_owner.gym_name}'s Software Membership"


def generate_staff_id():
    latest_staff = Staff.objects.order_by('staff_id').last()
    if latest_staff:
        latest_number = int(latest_staff.staff_id[3:]) + 1
        print(latest_number)
    else:
        latest_number = 1
    return f"EMP{latest_number:05}"

class Staff(models.Model):
    gym = models.ForeignKey('Gym', on_delete=models.PROTECT,null=True, blank=True)
    staff_id = models.CharField(max_length=8,primary_key=True ,default=generate_staff_id)
    staff_name = models.CharField(max_length=250)
    staff_address = models.CharField(max_length=250)
    user_name = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.PROTECT, null=True, blank=True)
    # staff_phone_number = models.CharField(max_length=15)
    # staff_email = models.EmailField()
    GENDER_CHOICES = [
        ('M', 'Male'),
        ('F', 'Female'),
        ('O', 'Other'),
    ]
    staff_gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    staff_age = models.IntegerField()
    staff_position = models.CharField(max_length=100)
    staff_salary = models.DecimalField(max_digits=10, decimal_places=2)
    staff_date_of_hire = models.DateField()
    staff_photo = models.ImageField(upload_to='staff_photos/', null=True, blank=True)
    staff_qr = models.ImageField(upload_to='staff_qr/',)
    SHIFT_CHOICES = [
        ('Morning', 'Morning'),
        ('Afternoon', 'Afternoon'),
        ('Evening', 'Evening'),
        ('Night', 'Night'),
    ]
    shift = models.CharField(max_length=10, choices=SHIFT_CHOICES)

    def __str__(self):
        return f"{self.staff_name} - {self.gym.gym_name}"
    
    def save(self, *args, **kwargs):
        print('calling save function ')
        data_dict = {field.attname: getattr(self, field.attname) for field in self._meta.fields}
        print(data_dict)
        qr_code_path = generate_qr_code(data_dict)
        if qr_code_path:
            self.staff_qr = qr_code_path.replace('media', '')

        super().save(*args, **kwargs)