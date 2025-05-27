from django.contrib import admin
from .models import ItemPedido, Pedido
from . import models


class ItemPedidoInline(admin.TabularInline):
    model = models.ItemPedido
    extra = 1


class ProdutoAdmin(admin.ModelAdmin):
    inlines = [ItemPedidoInline]


admin.site.register(Pedido, ProdutoAdmin)
admin.site.register(ItemPedido)