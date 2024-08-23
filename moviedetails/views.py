from django.shortcuts import redirect
import requests
from django.shortcuts import render, get_object_or_404
from django.http import Http404
from moviesearch.models import Movie
from django.contrib.auth.decorators import login_required
from watchlists.models import Watchlist


@login_required
def movie_detail(request, movie_id):
    try:
        # Try to get the movie from the local database first
        movie = get_object_or_404(Movie, id=movie_id)
    except Http404:
        # If the movie is not found locally, fetch it from the external API
        api_key = 'f3b973b04d9ca01a370a90afe12d30fa'
        url = f'https://api.themoviedb.org/3/movie/{movie_id}?api_key={api_key}'
        response = requests.get(url)
        if response.status_code == 200:
            movie_data = response.json()

            # Create the movie instance
            movie, created = Movie.objects.get_or_create(
                id=movie_id,
                defaults={
                    'title': movie_data.get('title', 'No Title'),
                    'release_date': movie_data.get('release_date', None),
                    'overview': movie_data.get('overview', 'No overview available'),
                    'vote_average': movie_data.get('vote_average', 0),
                    'runtime': movie_data.get('runtime', 0),
                    'poster_path': movie_data.get('poster_path', None),  # Make sure poster_path is saved
                }
            )
        else:
            raise Http404("Movie not found.")

    # Fetch the user’s watchlists
    watchlists = Watchlist.objects.filter(user=request.user)

    return render(request, 'moviedetails/detail.html', {'movie': movie, 'watchlists': watchlists})


@login_required
def add_to_watchlist(request, movie_id):
    if request.method == "POST":
        watchlist_id = request.POST.get('watchlist')
        watchlist = get_object_or_404(Watchlist, id=watchlist_id, user=request.user)

        # Check if the movie already exists in the database
        movie, created = Movie.objects.get_or_create(id=movie_id)

        # If created is True, the movie was just added to the database, otherwise it already existed

        watchlist.movies.add(movie)
        return redirect('moviedetails:movie_detail', movie_id=movie_id)
    else:
        return redirect('moviedetails:movie_detail', movie_id=movie_id)
