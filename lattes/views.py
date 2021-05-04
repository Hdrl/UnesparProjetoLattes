from django.shortcuts import render, reverse
from django.core.paginator import Paginator
from django.db.models import Count, Q
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from .models import Producao, Pessoas
from .filters import ProducaoFilter, PessoasFilter

# Create your views here.
@login_required
def index(request):
    return render(request, "lattes/index.html")

@login_required
def pessoas(request):
    context = {}

    pessoas_filtradas = PessoasFilter(
        request.GET,
        queryset=Pessoas.objects.all()
    )
    p = Paginator(pessoas_filtradas.qs, 10)
    page_number = request.GET.get('page')
    Pessoas_page = p.get_page(page_number)

    context["Pessoas_page"] = Pessoas_page
    context["pessoas_filtradas"] = pessoas_filtradas
    context["length"] = len(pessoas_filtradas.qs)

    return render(request, "lattes/pessoas/pessoas.html")

@login_required
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

@login_required
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

def login_view(request):
    if request.method == "POST":
        username=request.POST["username"]
        password=request.POST["password"]
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("lattes:index"))
        else:
            return render(request, "lattes/login.html",{
                "message":"usuário ou senha errado."
            })
    return render(request, "lattes/login.html")

@login_required
def logout_view(request):
    logout(request)
    return render(request, "lattes/login.html")