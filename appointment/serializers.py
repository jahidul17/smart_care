from rest_framework import serializers
from .import models

class AppointmentSerializer(serializers.ModelSerializer):
    
    patient=serializers.StringRelatedField(many=False)
    doctor=serializers.StringRelatedField(many=False)
    time=serializers.StringRelatedField(many=False) # one time chose thats way false
    
    class Meta:
        model=models.Appointment
        fields='__all__'
        

       

