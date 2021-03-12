import django_filters
from .models import Producao

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