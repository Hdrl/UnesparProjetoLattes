from django.shortcuts import render
from django.core.paginator import Paginator
from .models import Producao
from .filters import ProducaoFilter
from django.db.models import Count, Q

# Create your views here.
def index(request):
    return render(request, "lattes/index.html")


def producoes(request):
    context = {}

    producoes_filtradas = ProducaoFilter(
        request.GET,
        queryset=Producao.objects.all()
    )

    p = Paginator(producoes_filtradas.qs, 10)
    page_number = request.GET.get('page')
    Producao_page = p.get_page(page_number)

    context["Producao_page"] = Producao_page
    context["producoes_filtradas"] = producoes_filtradas
    context["length"] = len(producoes_filtradas.qs)
    return render(request, "lattes/producoes.html", context)


def perfilProducao(request):
    context = {}

    producoes_filtradas = ProducaoFilter(
        request.GET,
        queryset=Producao.objects.all()
    )

    query = producoes_filtradas.qs.values('ano').annotate(total=Count('id')).order_by('ano')
    context['anos'] = [dic['ano'] for dic in query]
    context['totalAno'] = [dic['total'] for dic in query]

    query = producoes_filtradas.qs.values('tipo').annotate(total=Count('id')).order_by('tipo').filter(tipoAgrupador='Produção bibliográfica')
    context['tiposB'] = [dic['tipo'] for dic in query]
    context['totalTipoB'] = [dic['total'] for dic in query]

    query = producoes_filtradas.qs.values('tipo').annotate(total=Count('id')).order_by('tipo').filter(tipoAgrupador='Produção técnica')
    context['tiposT'] = [dic['tipo'] for dic in query]
    context['totalTipoT'] = [dic['total'] for dic in query]

    query = producoes_filtradas.qs.values('tipo').annotate(total=Count('id')).order_by('tipo').filter(tipoAgrupador='Orientação em andamento')
    context['tiposO'] = [dic['tipo'] for dic in query]
    context['totalTipoO'] = [dic['total'] for dic in query]

    query = producoes_filtradas.qs.values('tipo').annotate(total=Count('id')).order_by('tipo').filter(tipoAgrupador='Produção artística/cultural')
    context['tiposA'] = [dic['tipo'] for dic in query]
    context['totalTipoA'] = [dic['total'] for dic in query]

    query = producoes_filtradas.qs.values('tipo').annotate(total=Count('id')).order_by('tipo').filter(Q(tipoAgrupador='Banca') | Q(tipoAgrupador='Evento') | Q(tipoAgrupador='Outro tipo de produção'))
    context['tiposE'] = [dic['tipo'] for dic in query]
    context['totalTipoE'] = [dic['total'] for dic in query]

    context["producoes_filtradas"] = producoes_filtradas
    return render(request, "lattes/perfilProducao.html", context)
