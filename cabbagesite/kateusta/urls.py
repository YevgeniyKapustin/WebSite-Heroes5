from django.urls import path

from kateusta.views import show_kateusta

urlpatterns = [
    path('', show_kateusta, name='kateusta')
]
