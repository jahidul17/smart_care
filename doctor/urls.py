from rest_framework.routers import DefaultRouter
from django.urls import path, include
from . import views


router = DefaultRouter() # amader router

router.register('specialization', views.SpecializationViewset) 
router.register('designation', views.DesignationViewset) 
router.register('availabletime', views.AvailableTimeViewset) 
router.register('list', views.DoctorViewset) 
router.register('review', views.ReviewViewset) 

urlpatterns = [
    path('', include(router.urls)),
]