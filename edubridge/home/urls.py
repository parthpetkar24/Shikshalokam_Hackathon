from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_page, name='home'), 
    path('teacher_dashboard/', views.teacher_dashboard, name='teacher_dashboard'),  
    path('diet_dashboard/', views.diet_dashboard, name='diet_dashboard'),  
]