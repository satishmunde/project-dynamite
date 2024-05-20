from datetime import timezone
from rest_framework import serializers

from api.models import Gym,Member,Trainer,Equipment,WorkoutPlan,Membership,SoftwareMembership,Staff

from django.core.files.storage import default_storage


class MemberSerializer(serializers.ModelSerializer):

    def validate(self, data):
        print()
        print('--------------------')
        if not Gym.objects.filter(pk=data['gym'].gym_id).exists():
            raise serializers.ValidationError("Invalid gym ID")


        if data['member_age'] <= 16:
            raise serializers.ValidationError("Age must be a Greater than 16")
        

        return data
    
    
    def update(self, instance, validated_data):
        
        print('put called')
        print(instance.member_id)
        validated_data['member_id']= instance.member_id
            

        for field, value in validated_data.items():
            setattr(instance, field, value)
        # Save the instance
        instance.save()
        return instance
            
            
    class Meta:
        model = Member
        fields = ['user_name', 'member_id','gym', 'member_name', 'member_gender', 'member_age', 'member_weight', 'member_height', 
                'member_date_of_birth', 'member_address', 'member_photo', 'member_qr']
        read_only_fields = ['member_id','member_qr']

class TrainerSerializer(serializers.ModelSerializer):

    def validate(self, data):
        if not Gym.objects.filter(pk=data['gym'].gym_id).exists():
            raise serializers.ValidationError("Invalid gym ID")
        return data
    

    def update(self, instance, validated_data):
        
        print('put called')
        print(instance.trainer_id)
        
        # Iterate through the validated data and update the instance with each field
        for field, value in validated_data.items():
            setattr(instance, field, value)
        # Save the instance
        instance.save()
        return instance
            
    
    
    class Meta:
        model = Trainer
        fields = ['user_name','gym', 'trainer_id', 'trainer_name', 'speciality', 'years_of_experience', 'age', 'gender', 'certification',
                'address', 'profile_picture', 'trainer_qr']
        read_only_fields = ['trainer_id','trainer_qr']

class EquipmentSerializer(serializers.ModelSerializer):
    
    def validate(self, data):
        print()
        print('--------------------')
        if not Gym.objects.filter(pk=data['gym'].gym_id).exists():
            raise serializers.ValidationError("Invalid gym ID")


        if data['member_age'] <= 16:
            raise serializers.ValidationError("Age must be a Greater than 16")
        

        return data
    
    class Meta:
        model = Equipment
        fields = ['gym', 'name', 'description', 'quantity', 'category', 'manufacturer', 'purchase_date', 'warranty_expiry',
                  'condition', 'location', 'photo']

class WorkoutPlanSerializer(serializers.ModelSerializer):
    
    def validate(self, data):
        print()
        print('--------------------')
        if not Gym.objects.filter(pk=data['gym'].gym_id).exists():
            raise serializers.ValidationError("Invalid gym ID")


        if data['member_age'] <= 16:
            raise serializers.ValidationError("Age must be a Greater than 16")
        

        return data
    class Meta:
        model = WorkoutPlan
        fields = ['gym', 'title', 'description', 'trainer', 'duration_in_weeks', 'price', 'target_audience', 'difficulty_level',
                  'goals', 'included_equipment', 'created_at', 'updated_at', 'photo']

class MembershipSerializer(serializers.ModelSerializer):
    class Meta:
        model = Membership
        fields = ['gym', 'member', 'plan', 'start_date', 'end_date', 'price_paid', 'payment_method', 'is_active', 'notes']

class GymSerializer(serializers.ModelSerializer):
    
        

    def update(self, instance, validated_data):
        
        print('put called')
        print(instance.gym_id)
        validated_data['gym_id']= instance.gym_id
 
        # Iterate through the validated data and update the instance with each field
        for field, value in validated_data.items():
            setattr(instance, field, value)
        # Save the instance
        instance.save()
        return instance
    
    
    class Meta:
        model = Gym
        fields = ['user_name','gym_id', 'gym_name', 'owner_name', 'gym_address',  'establishment_date', 'website',
                  'description','logo','gym_qr']
        
        read_only_fields = ['gym_id','gym_qr']
            
class SoftwareMembershipSerializer(serializers.ModelSerializer):
    class Meta:
        model = SoftwareMembership
        fields = ['gym_owner', 'license_key', 'license_expiry_date', 'payment_method', 'billing_address', 'payment_confirmation',
                'gym_contact_number', 'gym_email', 'active_users_count', 'training_and_support_requests',
                'admin_email', 'admin_password', 'integration_preferences', 'usage_agreement', 'feedback_on_features',
                'improvement_suggestions']

class StaffSerializer(serializers.ModelSerializer):    


    def update(self, instance, validated_data):
        
        print('put called')
        print(instance.staff_id)
  
        # Iterate through the validated data and update the instance with each field
        for field, value in validated_data.items():
            setattr(instance, field, value)
        # Save the instance
        instance.save()
        return instance

    
    class Meta:
        model = Staff
        fields = ['user_name','gym', 'staff_id', 'staff_name', 'staff_address', 'staff_gender', 'staff_age',
                  'staff_position', 'staff_salary', 'staff_date_of_hire', 'staff_photo', 'staff_qr', 'shift']

        read_only_fields = ['user_name','staff_id','staff_qr']
