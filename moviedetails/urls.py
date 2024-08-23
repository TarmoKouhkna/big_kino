from django.urls import path
from .views import movie_detail, add_to_watchlist

app_name = 'moviedetails'

urlpatterns = [
    path('<int:movie_id>/', movie_detail, name='movie_detail'),
    path('<int:movie_id>/add_to_watchlist/', add_to_watchlist, name='add_to_watchlist'),
]
