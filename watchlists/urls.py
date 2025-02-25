from django.urls import path
from . import views
from .views import watchlist_list, watchlist_create, watchlist_update, watchlist_delete

app_name = 'watchlists'

urlpatterns = [
    path('', watchlist_list, name='watchlist_list'),
    path('create/', watchlist_create, name='watchlist_create'),
    path('<int:pk>/update/', watchlist_update, name='watchlist_update'),
    path('<int:pk>/delete/', views.watchlist_delete, name='delete_watchlist'),
]
