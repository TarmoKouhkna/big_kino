from django.shortcuts import render
import requests

# moviesearch/views.py
from django.shortcuts import render
import requests


def search_movies(request):
    query = request.GET.get('q')  # Capturing the query parameter
    results = []

    if query:
        api_key = 'f3b973b04d9ca01a370a90afe12d30fa'
        url = f'https://api.themoviedb.org/3/search/movie?api_key={api_key}&query={query}'
        response = requests.get(url)
        if response.status_code == 200:
            results = response.json().get('results', [])

    return render(request, 'moviesearch/search.html', {'movies': results, 'query': query})


def home(request):
    return render(request, 'moviesearch/home.html')