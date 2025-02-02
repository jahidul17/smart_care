from django.shortcuts import render
from rest_framework import  filters,viewsets,pagination
from . import models
from . import serializers
from rest_framework.permissions import IsAuthenticated,IsAuthenticatedOrReadOnly 




class SpecializationViewset(viewsets.ModelViewSet):
    queryset = models.Specialization.objects.all()
    serializer_class = serializers.SpecializationSerializer
    
    
class DesignationViewset(viewsets.ModelViewSet):
    queryset = models.Designation.objects.all()
    serializer_class = serializers.DesignationSerializer
    

class AvailableTimeForSpecificDoctor(filters.BaseFilterBackend):
    def filter_queryset(self, request, queryset, view):
        doctor_id=request.query_params.get("doctor_id")
        if doctor_id:
            return queryset.filter(doctor=doctor_id) #here, doctor from class model name Doctor as doctor
        return queryset
    
class AvailableTimeViewset(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated] #api link permit which are authentice user
    # permission_classes = [IsAuthenticatedOrReadOnly]    
    queryset = models.AvailableTime.objects.all()
    serializer_class = serializers.AvailableTimeSerializer
    filter_backends=[AvailableTimeForSpecificDoctor]
    
    
    
class DoctorPagination(pagination.PageNumberPagination):
    page_size=1 #1 item per page
    page_size_query_param=page_size
    max_page_size=100   
    
    
class DoctorViewset(viewsets.ModelViewSet):
    queryset = models.Doctor.objects.all()
    serializer_class = serializers.DoctorSerializer
    filter_backends=[filters.SearchFilter]
    pagination_class=DoctorPagination
    search_fields = ['user__first_name', 'user__email', 'designation__name', 'specialization__name']
    
    
class ReviewViewset(viewsets.ModelViewSet):
    queryset = models.Review.objects.all()
    serializer_class = serializers.ReviewSerializer