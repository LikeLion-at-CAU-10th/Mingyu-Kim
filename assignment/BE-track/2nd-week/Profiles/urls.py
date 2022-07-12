from django.urls import path
from .views import *

urlpatterns = [
    path('create_profile/',create_profile, name = "create_profile"),   
    path('get_profile/<int:id>', get_profile, name= "get_profile"),
    path('get_profile_all/', get_profile_all ,name = "get_profile_all"),
]