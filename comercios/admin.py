from django.contrib import admin
from .models import SocialMedia, Comercio

# Register your models here.

class ComercioAdmin(admin.ModelAdmin):
    list_display = ('categoria', 'nombre_comercio', 'direccion','telefono', 'email')
    ordering = ('categoria','nombre_comercio')
    search_fields = ('categoria','nombre_comercio')

    class Meta:
        model = Comercio

class SocialMediaAdmin(admin.ModelAdmin):   
    list_display = ('comercio', 'social_media', 'estado')
    ordering = ('comercio','social_media')
    search_fields = ('comercio','social_media')
    list_filter = ('comercio',)
    list_per_page = 10


admin.site.register(SocialMedia, SocialMediaAdmin)
admin.site.register(Comercio, ComercioAdmin)

