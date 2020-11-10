from rest_framework import serializers
from django.contrib.auth.models import User
from produtos.models import Camisa, Chuteira


class CamisaSerializer(serializers.ModelSerializer):
    preco_dolar = serializers.SerializerMethodField()

    class Meta:
        model = Camisa
        fields = ['id', 'time', 'cor', 'fabricante', 'preco', 'preco_dolar', 'quantidade', 'created_at', 'ativo']
        # fields = '__all__'

    def get_preco_dolar(self, obj):
        dolar = 5.32
        preco_dolar = obj.preco / dolar
        return round(preco_dolar, 2)


class ChuteiraSerializer(serializers.ModelSerializer):
    preco_dolar = serializers.SerializerMethodField()

    class Meta:
        model = Chuteira
        fields = ['id', 'cor', 'fabricante', 'tipo', 'preco', 'preco_dolar', 'quantidade', 'created_at', 'ativo']
        # fields = '__all__'

    def get_preco_dolar(self, obj):
        dolar = 5.32
        preco_dolar = obj.preco / dolar
        return round(preco_dolar, 2)
