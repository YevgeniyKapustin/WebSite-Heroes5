from django.urls import path

from reports.views import send_reports

urlpatterns = [
    path('send/', send_reports, name='send_report')
]
