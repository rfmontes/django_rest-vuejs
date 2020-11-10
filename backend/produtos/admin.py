from django.contrib import admin

from produtos.models import Camisa, Chuteira


@admin.register(Camisa)
class CamisaAdmin(admin.ModelAdmin):
    list_display = ('id', 'time', 'cor', 'fabricante', 'preco', 'quantidade', 'created_at', 'ativo')


@admin.register(Chuteira)
class ChuteiraAdmin(admin.ModelAdmin):
    list_display = ('id', 'cor', 'fabricante', 'tipo', 'preco', 'quantidade', 'created_at', 'ativo')
