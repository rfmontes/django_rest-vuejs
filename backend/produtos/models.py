from django.db import models


class Camisa(models.Model):
    time = models.CharField('Time', max_length=200, null=True, blank=True)
    cor = models.CharField('Cor predominante', max_length=200)
    fabricante = models.CharField('Fabricante', max_length=200)
    preco = models.FloatField()
    quantidade = models.IntegerField('Quantidade')
    created_at = models.DateTimeField(auto_now_add=True)
    ativo = models.BooleanField(default=True)

    class Meta:
        verbose_name = 'Camisa'
        verbose_name_plural = 'Camisas'
        ordering = ['id']

    def __str__(self):
        return f'Camisa do {self.time}'


class Chuteira(models.Model):
    cor = models.CharField('Cor predominante', max_length=200)
    fabricante = models.CharField('Fabricante', max_length=200)
    tipo = models.CharField('Tipo', max_length=100)
    preco = models.FloatField()
    quantidade = models.IntegerField('Quantidade')
    created_at = models.DateTimeField(auto_now_add=True)
    ativo = models.BooleanField(default=True)

    class Meta:
        verbose_name = 'Chuteira'
        verbose_name_plural = 'Chuteiras'
        ordering = ['id']

    def __str__(self):
        return f'Chuteira da {self.fabricante}'
