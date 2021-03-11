from django.shortcuts import render
from django.core.paginator import Paginator
from .models import Producao
from .filters import ProducaoFilter

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
    Producao_page=p.get_page(page_number)

    context["Producao_page"] = Producao_page
    context["producoes_filtradas"] = producoes_filtradas
    context["length"] = len(producoes_filtradas.qs)
    return render(request, "lattes/producoes.html", context)