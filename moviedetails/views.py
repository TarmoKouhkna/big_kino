import requests
from django.shortcuts import render, get_object_or_404
from django.http import Http404
from moviesearch.models import Movie
from django.conf import settings


def movie_detail(request, movie_id):
    try:
        # First, try to fetch the movie from the local database
        movie = get_object_or_404(Movie, id=movie_id)
    except Http404:
        # If the movie is not found locally, fetch it from the external API
        api_key = 'f3b973b04d9ca01a370a90afe12d30fa'  # Replace with your actual API key
        url = f'https://api.themoviedb.org/3/movie/{movie_id}?api_key={api_key}'
        response = requests.get(url)
        if response.status_code == 200:
            movie = response.json()
        else:
            raise Http404("No Movie matches the given query.")

    # Render the movie details page
    return render(request, 'moviedetails/detail.html', {'movie': movie})
