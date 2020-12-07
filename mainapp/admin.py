from django.contrib import admin
from .models import Usuario, Transporte, Imagen, Area

class TransporteAdmin(admin.ModelAdmin):
    readonly_fields = ('date',)

# Register your models here.
admin.site.register(Usuario)
admin.site.register(Imagen)
admin.site.register(Area)
admin.site.register(Transporte,TransporteAdmin)  