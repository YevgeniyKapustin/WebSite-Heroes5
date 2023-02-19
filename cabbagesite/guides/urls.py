from django.urls import path

from guides.views import GuidesMain, GuideDetailMain

urlpatterns = [
    path('', GuidesMain.as_view(), name='guides'),
    path('<slug:slug>/', GuideDetailMain.as_view(), name='guide'),
]
