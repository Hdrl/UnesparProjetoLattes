from django.shortcuts import render
from django.core.paginator import Paginator
from .models import Producao
from .filters import ProducaoFilter
from django.db.models import Count

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
    context ={}
    query = Producao.objects.values('ano').annotate(total=Count('id')).order_by('ano')
    context['anos'] = [dic['ano'] for dic in query]
    context['total'] = [dic['total'] for dic in query]
    return render(request, "lattes/perfilProducao.html", context)
