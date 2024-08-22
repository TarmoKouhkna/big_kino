from django.urls import path
from .views import movie_detail

app_name = 'moviedetails'

urlpatterns = [
    path('<int:movie_id>/', movie_detail, name='movie_detail'),
]
