from django.contrib import admin
from .models import Producao

# Register your models here.
class ProducaoAdmin(admin.ModelAdmin):
    list_display = ("ano", "informadoPor", "tipo", "tipoAgrupador", "titulo")

admin.site.register(Producao, ProducaoAdmin)
