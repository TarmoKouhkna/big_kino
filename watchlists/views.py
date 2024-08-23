import requests
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.http import Http404
from moviesearch.models import Movie
from .models import Watchlist
from .forms import WatchlistForm


@login_required
def watchlist_list(request):
    watchlists = Watchlist.objects.filter(user=request.user)
    return render(request, 'watchlists/watchlist_list.html', {'watchlists': watchlists})


@login_required
def watchlist_create(request):
    if request.method == 'POST':
        form = WatchlistForm(request.POST)
        if form.is_valid():
            watchlist = form.save(commit=False)
            watchlist.user = request.user
            watchlist.save()
            return redirect('watchlists:watchlist_list')
    else:
        form = WatchlistForm()
    return render(request, 'watchlists/watchlist_form.html', {'form': form})


@login_required
def watchlist_update(request, pk):
    watchlist = get_object_or_404(Watchlist, pk=pk, user=request.user)
    if request.method == 'POST':
        form = WatchlistForm(request.POST, instance=watchlist)
        if form.is_valid():
            form.save()
            return redirect('watchlists:watchlist_list')
    else:
        form = WatchlistForm(instance=watchlist)
    return render(request, 'watchlists/watchlist_form.html', {'form': form})


@login_required
def watchlist_delete(request, pk):
    watchlist = get_object_or_404(Watchlist, pk=pk, user=request.user)
    if request.method == 'POST':
        watchlist.delete()
        return redirect('watchlists:watchlist_list')
    return render(request, 'watchlists/watchlist_confirm_delete.html', {'watchlist': watchlist})


@login_required
def add_to_watchlist(request, movie_id):
    if request.method == "POST":
        # Check if the movie already exists in the database
        movie, created = Movie.objects.get_or_create(id=movie_id)

        # If the movie was created (not already in the database), fetch the details from the API
        if created:
            api_key = 'f3b973b04d9ca01a370a90afe12d30fa'  # Replace with your actual TMDb API key
            url = f'https://api.themoviedb.org/3/movie/{movie_id}?api_key={api_key}'
            response = requests.get(url)
            if response.status_code == 200:
                movie_data = response.json()

                # Populate the movie instance with the necessary data
                movie.title = movie_data.get('title', 'No Title')
                movie.release_date = movie_data.get('release_date', '') or None
                movie.overview = movie_data.get('overview', 'No overview available')
                movie.vote_average = movie_data.get('vote_average', 0)
                movie.runtime = movie_data.get('runtime', 0) or None
                movie.poster_path = movie_data.get('poster_path', None)  # Assuming you have a poster_path field

                # Save the movie instance to the database
                movie.save()
            else:
                raise Http404("No Movie matches the given query.")

        # Add the movie to the selected watchlist
        watchlist_id = request.POST.get('watchlist')
        watchlist = get_object_or_404(Watchlist, id=watchlist_id, user=request.user)
        watchlist.movies.add(movie)

        return redirect('moviedetails:movie_detail', movie_id=movie_id)
