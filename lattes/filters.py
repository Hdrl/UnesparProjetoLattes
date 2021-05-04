import django_filters
from .models import Producao, Pessoas

class ProducaoFilter(django_filters.FilterSet):
    class Meta:
        model = Producao
        fields = {
            'ano': ['gte', 'lte'],
            'tipo': ['contains'],
            'tipoAgrupador': ['contains'],
            'informadoPor': ['contains'],
            'titulo': ['contains']
        }

class PessoasFilter(django_filters.FilterSet):
    model = Pessoas
    fields = {
        'nome': ['contains'],
        'campus': ['contains'],
        'titulo': ['contains'],
        'tipoVinculo': ['contains'],
        'formacao': ['contains'],
        'instituicaoEmQueSeFormou': ['contains'],
        'anoQueIngressouNoCampus': ['exacts']      
   
    }