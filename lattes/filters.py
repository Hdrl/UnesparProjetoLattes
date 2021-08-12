from django.forms import widgets
import django_filters
from django.forms.widgets import TextInput
from .models import Producao, Pessoas, Projeto

class ProducaoFilter(django_filters.FilterSet):
    titulo = django_filters.CharFilter(field_name='titulo', lookup_expr='contains', widget=TextInput(attrs={'placeholder': 'Digite titulo'}))
    informadoPor = django_filters.CharFilter(field_name='informadoPor', lookup_expr='contains', widget=TextInput(attrs={'placeholder': 'Digite quem informou'}))
    tipo = django_filters.CharFilter(field_name='tipo', lookup_expr='contains', widget=TextInput(attrs={'placeholder': 'Digite tipo'}))
    tipoAgrupador = django_filters.CharFilter(field_name='tipoAgrupador', lookup_expr='contains', widget=TextInput(attrs={'placeholder': 'Digite tipo agrupador'}))
    class Meta:
        model = Producao
        fields = {
            'ano': ['gte', 'lte']
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
        'anoQueIngressouNoCampus': ['exact']    
    }
    
situacao_choices = (
    ('CONCLUIDO', 'Concluido'),
    ('EM_ANDAMENTO', 'Em Andamento')
)

tipo_choices = (
    ('DESENVOLVIMENTO', 'Desenvolvimento'),
    ('EXTENSAO', 'Extensão'),
    ('PESQUISA', 'Pesquisa'),
    ('OUTRA', 'Outra')
)

class ProjetoFilter(django_filters.FilterSet):
    nome = django_filters.CharFilter(field_name='nome', lookup_expr='contains', widget=TextInput(attrs={'placeholder': 'Digite o nome'}))
    anoInicio = django_filters.NumberFilter(field_name='anoInicio', widget=TextInput(attrs={'placeholder': 'Digite ano de inicio'}))
    situacao = django_filters.ChoiceFilter(field_name='situacao', choices=situacao_choices)
    tipo = django_filters.ChoiceFilter(field_name='tipo', choices=tipo_choices)
    coordenador = django_filters.CharFilter(field_name='coordenador', lookup_expr='contains', widget=TextInput(attrs={'placeholder': 'Digite o coordenador'}))
    informadoPor = django_filters.CharFilter(field_name='informadoPor', lookup_expr='contains', widget=TextInput(attrs={'placeholder': 'Digite quem informou'}))