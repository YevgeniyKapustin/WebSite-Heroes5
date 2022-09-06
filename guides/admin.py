from django.contrib import admin

from guides.models import Guides


class GuidesAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug')
    prepopulated_fields = {'slug': ('title',)}


admin.site.register(Guides, GuidesAdmin)
