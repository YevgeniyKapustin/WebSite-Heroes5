from django.contrib import admin
from .models import Home, DownloadGame, Mods, Maps, Online, Fractions, Report


class HomeAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_at')
    list_display_links = ('title',)
    search_fields = ('title', 'content')


class ReportAdmin(admin.ModelAdmin):
    list_display = ('victory', 'myself', 'opponent', 'fraction_myself', 'fraction_opponent', 'created_at')
    list_display_links = ('myself',)
    search_fields = ('myself', 'created_at')


class OtherAdmin(admin.ModelAdmin):
    list_display_links = ('title',)
    search_fields = ('title', 'content')


admin.site.register(Home, HomeAdmin)
admin.site.register(DownloadGame)
admin.site.register(Mods)
admin.site.register(Maps)
admin.site.register(Online)
admin.site.register(Fractions)
admin.site.register(Report, ReportAdmin)
admin.site.site_header = 'Управление'
