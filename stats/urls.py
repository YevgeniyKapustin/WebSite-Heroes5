from django.urls import path
from stats.views import show_stat

urlpatterns = [
    path('show/', show_stat, name='show_stat')
]
