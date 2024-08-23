from django.contrib import admin
from django.urls import path, include
from moviesearch.views import home  # Import the home view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),  # Home view
    path('moviesearch/', include('moviesearch.urls')),  # Moviesearch functionality
    path('moviedetails/', include('moviedetails.urls')),  # Moviedetails functionality
    path('accounts/', include('accounts.urls')),  # User accounts
    path('profiles/', include('userprofiles.urls')),  # Profiles
    path('watchlists/', include('watchlists.urls')),  # Watchlists
]
