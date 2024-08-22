from django.urls import path
from .views import search_movies

app_name = 'moviesearch'

urlpatterns = [
    path('', search_movies, name='search_movies'),
]
