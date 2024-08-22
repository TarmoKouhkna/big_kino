import requests
from django.shortcuts import render
from .forms import MovieSearchForm

API_KEY = 'f3b973b04d9ca01a370a90afe12d30fa'
BASE_URL = 'https://api.themoviedb.org/3/search/movie'


def home(request):
    return render(request, 'home.html')


def search_movies(request):
    form = MovieSearchForm()
    results = []

    if request.method == 'POST':
        form = MovieSearchForm(request.POST)
        if form.is_valid():
            query = form.cleaned_data['query']
            response = requests.get(BASE_URL, params={
                'api_key': API_KEY,
                'query': query
            })
            if response.status_code == 200:
                results = response.json().get('results', [])

    return render(request, 'moviesearch/search.html', {'form': form, 'results': results})
