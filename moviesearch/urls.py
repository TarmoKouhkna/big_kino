# moviesearch/urls.py
from django.urls import path
from . import views

app_name = 'moviesearch'

urlpatterns = [
    path('', views.search_movies, name='search_movies'),  # This should match the URL used in your form
]
