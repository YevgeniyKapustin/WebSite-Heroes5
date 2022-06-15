from django.urls import path
from .views import *

urlpatterns = [
    path('', HomeMain.as_view(), name='home'),
    path('download_game/', GameMain.as_view(), name='download_game'),
    path('mods/', ModsMain.as_view(), name='mods'),
    path('maps/', MapsMain.as_view(), name='maps'),
    path('online_game/', OnlineMain.as_view(), name='online_game'),
    path('register/', register, name='register'),
    path('login/', user_login, name='login'),
    path('logout/', user_logout, name='logout'),
    path('report/', report, name='report'),
]
