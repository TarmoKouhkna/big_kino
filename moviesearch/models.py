from django.db import models


class Movie(models.Model):
    title = models.CharField(max_length=255)
    release_date = models.DateField()
    overview = models.TextField()
    poster_path = models.CharField(max_length=255)

    def __str__(self):
        return self.title
