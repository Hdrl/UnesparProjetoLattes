from django.contrib import admin
from .models import Producao, Projeto, Pessoas

# Register your models here.
class PessoasAdmin(admin.ModelAdmin):
    list_display = ("nome", "titulo", "campus", "tipoVinculo", "formacao", "instituicaoEmQueSeFormou", "anoQueIngressouNoCampus", "descricao")

class ProducaoAdmin(admin.ModelAdmin):
    list_display = ("titulo", "ano", "informadoPor", "tipo", "tipoAgrupador")

class ProjetoAdmin(admin.ModelAdmin):
    list_display = ("nome", "idCurriculo", "anoInicio", "situacao", "tipo", "coordenador", "informadoPor")

admin.site.register(Producao, ProducaoAdmin)
admin.site.register(Projeto, ProjetoAdmin)
admin.site.register(Pessoas, PessoasAdmin)