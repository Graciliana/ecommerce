from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic.list import ListView
from django.views import  View


class ListaProdutos(View):
    def get(self, *args, **kwargs):
        return HttpResponse("Listar Produtos")
class DetalheProduto(View):
    def get(self, *args, **kwargs):
        return HttpResponse("Detalhe Produto")


class AdicionarAoCarrinho(View):
    def get(self, *args, **kwargs):
        return HttpResponse("Adicionar ao Carinho")


class RemoverDoCarrinho(View):
    def get(self, *args, **kwargs):
        return HttpResponse("Remover Do Carrinho")


class Carrinho(View):
    def get(self, *args, **kwargs):
        return HttpResponse("Carrinho")


class Finalizar(View):
    def get(self, *args, **kwargs):
        return HttpResponse("Finalizar")