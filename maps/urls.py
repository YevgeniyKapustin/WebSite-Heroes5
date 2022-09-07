from django.urls import path
from maps.views import MapsList

urlpatterns = [
    path('', MapsList.as_view(), name='maps'),
]
