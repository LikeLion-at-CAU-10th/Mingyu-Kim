from django.urls import path
from . import views

urlpatterns = [
    path('create_category/', views.create_category, name = "create_category"),   
    path('get_category_all/', views.get_category_all, name = "get_category_all"),
    path('get_category/', views.get_category, name ="get_category"),
]