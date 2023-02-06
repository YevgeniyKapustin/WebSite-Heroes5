from django.urls import path

from maps.views import maps_install, maps_single, maps_multiplayer

urlpatterns = [
    path('-single', maps_single, name='maps_single'),
    path('-multiplayer', maps_multiplayer, name='maps_multiplayer'),
    path('-install', maps_install, name='maps_install'),
]
