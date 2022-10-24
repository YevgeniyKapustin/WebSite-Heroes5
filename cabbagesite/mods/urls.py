from django.urls import path
from mods.views import ModsList, mods_install

urlpatterns = [
    path('-multiplayer', ModsList.as_view(), name='mods'),
    path('-install', mods_install, name='mods_install'),
]
