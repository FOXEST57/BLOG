from django.urls import path
from .views import register, manage_profile

urlpatterns = [
    path('register/', register, name='register'),
    path('profile/', manage_profile, name='manage_profile'),
]