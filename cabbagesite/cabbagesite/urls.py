from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('stats.urls')),
    path('download_game', include('download_game.urls')),
    path('reports/', include('reports.urls')),
    path('kateusta', include('kateusta.urls')),
    path('guides', include('guides.urls')),
    path('maps', include('maps.urls')),
    path('mods', include('mods.urls')),
    path('online_game', include('online_game.urls')),
    path('', include('register.urls')),
    path('api/', include('api.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    import socket
    hostname, _, ips = socket.gethostbyname_ex(socket.gethostname())
    INTERNAL_IPS = [ip[: ip.rfind(".")] + ".1" for ip in ips] + ["127.0.0.1", "10.0.2.2"]
