from django.contrib import admin
from . models import Gum
from django.utils.safestring import mark_safe


class GumAdmin(admin.ModelAdmin):
    list_display = ('name', 'get_url')
    fields = ('name', 'subm', 'get_url')
    readonly_fields = ('get_url',)

    def get_url(self, object):
        return mark_safe(f"<a href='../../../../../../../../1/{object.slug}/'>Просмотреть {object.slug}</a>")
    
    get_url.short_description = 'ID'


admin.site.register(Gum, GumAdmin)
