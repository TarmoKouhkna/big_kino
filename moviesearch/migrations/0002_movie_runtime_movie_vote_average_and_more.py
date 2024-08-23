# Generated by Django 5.1 on 2024-08-22 16:20

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("moviesearch", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="movie",
            name="runtime",
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name="movie",
            name="vote_average",
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name="movie",
            name="overview",
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name="movie",
            name="poster_path",
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name="movie",
            name="release_date",
            field=models.DateField(blank=True, null=True),
        ),
    ]
