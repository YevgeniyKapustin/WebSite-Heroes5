from django.contrib import admin
from reports.models import Report, Fractions, PlayerData


class ReportAdmin(admin.ModelAdmin):
    list_display = ('victory', 'myself', 'opponent', 'fraction_myself',
                    'fraction_opponent', 'created_at')
    list_display_links = ('myself',)
    search_fields = ('myself', 'created_at')


admin.site.register(Report, ReportAdmin)
admin.site.register(Fractions)
admin.site.register(PlayerData)
