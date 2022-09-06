from django.urls import path
from mods_and_maps.views import ModsList, MapsList

urlpatterns = [
    path('mods/', ModsList.as_view(), name='mods'),
    path('maps/', MapsList.as_view(), name='maps'),
]
