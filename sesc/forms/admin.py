from core.admin import FormsAdminTemplate as Template
from django.contrib.admin import site, ModelAdmin
from django.utils.safestring import mark_safe
from forms.models import Gum, Sgum, SocEk, MatInf, FizMat, FizTech, Him, Bio


class GumAdmin(Template, ModelAdmin):
    def get_url(self, object):
        return mark_safe(f"<a href='{'../' * 10}1/{object.slug}/'>{object.slug}</a>")
    
    get_url.short_description = 'ID'


class SgumAdmin(Template, ModelAdmin):
    def get_url(self, object):
        return mark_safe(f"<a href='{'../' * 10}2/{object.slug}/'>{object.slug}</a>")
    
    get_url.short_description = 'ID'


class SocEkAdmin(Template, ModelAdmin):
    def get_url(self, object):
        return mark_safe(f"<a href='{'../' * 10}3/{object.slug}/'>{object.slug}</a>")
    
    get_url.short_description = 'ID'


class MatInfAdmin(Template, ModelAdmin):
    def get_url(self, object):
        return mark_safe(f"<a href='{'../' * 10}4/{object.slug}/'>{object.slug}</a>")
    
    get_url.short_description = 'ID'


class FizMatAdmin(Template, ModelAdmin):
    def get_url(self, object):
        return mark_safe(f"<a href='{'../' * 10}5/{object.slug}/'>{object.slug}</a>")
    
    get_url.short_description = 'ID'


class FizTechAdmin(Template, ModelAdmin):
    def get_url(self, object):
        return mark_safe(f"<a href='{'../' * 10}6/{object.slug}/'>{object.slug}</a>")
    
    get_url.short_description = 'ID'


class HimAdmin(Template, ModelAdmin):
    def get_url(self, object):
        return mark_safe(f"<a href='{'../' * 10}7/{object.slug}/'>{object.slug}</a>")
    
    get_url.short_description = 'ID'


class BioAdmin(Template, ModelAdmin):
    def get_url(self, object):
        return mark_safe(f"<a href='{'../' * 10}8/{object.slug}/'>{object.slug}</a>")
    
    get_url.short_description = 'ID'


site.register(Gum, GumAdmin)
site.register(Sgum, SgumAdmin)
site.register(SocEk, SocEkAdmin)
site.register(MatInf, MatInfAdmin)
site.register(FizMat, FizMatAdmin)
site.register(FizTech, FizTechAdmin)
site.register(Him, HimAdmin)
site.register(Bio, BioAdmin)
