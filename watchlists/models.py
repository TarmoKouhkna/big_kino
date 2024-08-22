from django.db import models
from django.contrib.auth.models import User
from moviesearch.models import Movie  # Assuming you have a Movie model for your API data


class Watchlist(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    movies = models.ManyToManyField(Movie)

    def __str__(self):
        return self.name
