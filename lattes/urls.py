from django.urls import path
from . import views

app_name = 'lattes'
urlpatterns=[
    path('', views.index, name="index"),
    path("producoes", views.producoes, name="producoes"),
    path("perfilProducao", views.perfilProducao, name="perfilProducao"),
    path("sair", views.logout_view, name="logout")
]