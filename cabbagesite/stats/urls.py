from django.urls import path

from stats.views import show_stat, redirect_to_stat

urlpatterns = [
    path('', redirect_to_stat, name='home'),
    path('stat/', show_stat, name='stats')
]
