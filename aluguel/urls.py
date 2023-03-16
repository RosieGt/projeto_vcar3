"""vcar URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path
from .views import index, lista_carros, realizar_aluguel, detalhar_carro, realizar_aluguel_carro, cadastrar_carro, cadastrar_cliente, detalhar_cliente, listar_cliente, atualizar_cliente, deletar_cliente


urlpatterns = [
    path('', index, name='index'),
    path('cliente/', listar_cliente, name='listar_cliente'),
    path('cliente/atualizar/<int:pk>', atualizar_cliente, name='atualizar_cliente'),
    path('cliente/deletar/<int:pk>', deletar_cliente, name='deletar_cliente'),
    path('carros/', lista_carros, name='listar_carros'),
    path('carros/cadastrar', cadastrar_carro, name='cadastrar_carro'),
    path('clientes/cadastrar', cadastrar_cliente, name='cadastrar_cliente'),
    path('cliente/<int:pk>', detalhar_cliente, name='detalhar_cliente'),
    path('carros/<int:pk>', detalhar_carro, name='detalhar_carro'),
    path('carros/aluguel/<int:carro_pk>', realizar_aluguel_carro, name='realizar_aluguel_carro' ),
    path('aluguel/add', realizar_aluguel, name='realizar_aluguel'),
]
