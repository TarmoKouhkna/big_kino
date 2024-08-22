from django.urls import path
from .views import profile

app_name = 'profiles'  # This is the namespace you need

urlpatterns = [
    path('dashboard/', profile, name='profile'),
]
