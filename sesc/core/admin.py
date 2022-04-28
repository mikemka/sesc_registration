from django.contrib import admin


class FormsAdminTemplate(admin.ModelAdmin):
    list_display = ('name', 'attached', 'get_url')
    list_editable = ('attached',)
    fields = ('name', 'get_url', 'subm', 'attached', )
    readonly_fields = ('get_url', 'subm', 'name')
    
    class Meta:
        abstract = True
