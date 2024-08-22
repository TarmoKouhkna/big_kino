from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import ProfileUpdateForm, UserUpdateForm
from watchlists.models import Watchlist


@login_required
def profile(request):
    if request.method == 'POST':
        user_form = UserUpdateForm(request.POST, instance=request.user)
        profile_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            return redirect('profiles:profile')  # Redirect to avoid resubmission
    else:
        user_form = UserUpdateForm(instance=request.user)
        profile_form = ProfileUpdateForm(instance=request.user.profile)

    user_watchlists = Watchlist.objects.filter(user=request.user)

    context = {
        'user_form': user_form,
        'profile_form': profile_form,
        'user_watchlists': user_watchlists,
    }
    return render(request, 'userprofiles/profile.html', context)
