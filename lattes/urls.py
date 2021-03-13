from django.urls import path
from . import views

app_name = 'lattes'
urlpatterns=[
    path("producoes", views.producoes, name="producoes"),
    path("perfilProducao", views.perfilProducao, name="perfilProducao")
]