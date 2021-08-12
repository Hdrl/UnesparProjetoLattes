from django.contrib import admin
from .models import *

# Register your models here.
class PessoasAdmin(admin.ModelAdmin):
    list_display = ("nome", "titulo", "campus", "tipoVinculo", "formacao", "instituicaoEmQueSeFormou", "anoQueIngressouNoCampus", "descricao")

class ProducaoAdmin(admin.ModelAdmin):
    list_display = ("titulo", "ano", "informadoPor", "tipo", "tipoAgrupador")

class ProjetoAdmin(admin.ModelAdmin):
    list_display = ("nome", "idCurriculo", "anoInicio", "situacao", "tipo", "coordenador", "informadoPor")

class SetorAtividadeAdmin(admin.ModelAdmin):
    list_display = ("setor", "producao_id")

class PalavraChaveAdmin(admin.ModelAdmin):
    list_display = ("palavra", "producao_id")

class AreaConhecimentoAdmin(admin.ModelAdmin):
    list_display = ("subArea", "area", "grandeArea", "especialidade", "producao_id")


admin.site.register(Producao, ProducaoAdmin)
admin.site.register(Projeto, ProjetoAdmin)
admin.site.register(Pessoas, PessoasAdmin)
admin.site.register(SetorAtividade, SetorAtividadeAdmin)
admin.site.register(PalavraChave, PalavraChaveAdmin)
admin.site.register(AreaConhecimento, AreaConhecimentoAdmin)