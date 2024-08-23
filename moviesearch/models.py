from django.db import models

class Movie(models.Model):
    title = models.CharField(max_length=255)
    release_date = models.DateField(null=True, blank=True)  # Update this line
    overview = models.TextField(null=True, blank=True)  # Optional but recommended for flexibility
    vote_average = models.FloatField(null=True, blank=True)  # Optional but recommended for flexibility
    runtime = models.IntegerField(null=True, blank=True)  # Optional but recommended for flexibility
    poster_path = models.CharField(max_length=255, null=True, blank=True)  # Optional but recommended for flexibility

    def __str__(self):
        return self.title
