from rest_framework import serializers
from . import models

class SpecializationSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Specialization
        fields = '__all__'
        
        
class DesignationSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Designation
        fields = '__all__'
        
        
class AvailableTimeSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.AvailableTime
        fields = '__all__'
        
        
class DoctorSerializer(serializers.ModelSerializer):
    
    user=serializers.StringRelatedField(many=False) #when single vaue then many = false
    designation=serializers.StringRelatedField(many=True) #when multiple value then many = true
    specialization=serializers.StringRelatedField(many=True)
    available_time=serializers.StringRelatedField(many=True)
    
    # When above stringRelatedField hide user input multiple list show in api link
    
    class Meta:
        model = models.Doctor
        fields = '__all__'
        
        
class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Review
        fields = '__all__'
        
        