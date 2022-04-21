from django.contrib import admin
from forms.models import Gum, Sgum, SocEk
from django.utils.safestring import mark_safe


class Template(admin.ModelAdmin):
    list_display = ('name', 'attached', 'get_url')
    list_editable = ('attached',)
    fields = ('name', 'get_url', 'subm', 'attached', )
    readonly_fields = ('get_url', 'subm', 'name')
    
    class Meta:
        abstract = True


class GumAdmin(Template, admin.ModelAdmin):
    def get_url(self, object):
        return mark_safe(f"<a href='{'../' * 10}1/{object.slug}/'>{object.slug}</a>")
    
    get_url.short_description = 'ID'


class SgumAdmin(Template, admin.ModelAdmin):
    def get_url(self, object):
        return mark_safe(f"<a href='{'../' * 10}2/{object.slug}/'>{object.slug}</a>")
    
    get_url.short_description = 'ID'


class SocEkAdmin(Template, admin.ModelAdmin):
    def get_url(self, object):
        return mark_safe(f"<a href='{'../' * 10}3/{object.slug}/'>{object.slug}</a>")
    
    get_url.short_description = 'ID'


admin.site.register(Gum, GumAdmin)
admin.site.register(Sgum, SgumAdmin)
admin.site.register(SocEk, SocEkAdmin)
