from django.urls import path
from mods.views import ModsList

urlpatterns = [
    path('', ModsList.as_view(), name='mods'),
]
