from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseForbidden
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
