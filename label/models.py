from django.db import models


# Create your models here.
class FolhaEtiqueta(models.Model):
    BOLOS = 'BOLOS'
    LANCHES = 'LANCHES'
    MODELO_CHOICES = [
        (BOLOS, 'Bolos'),
        (LANCHES, 'Lanches'),
    ]
    nome = models.CharField('Nome', max_length=100)
    modelo = models.CharField('Modelo', max_length=20, choices=MODELO_CHOICES, default=BOLOS)

    class Meta:
        ordering = ('nome',)
        verbose_name = 'folha de etiqueta'
        verbose_name_plural = 'folhas de etiquetas'

    def __str__(self):
        return self.nome


class FolhaEtiquetaItens(models.Model):
    SUAVE = 1
    MEDIA = 2
    MEGA = 3
    DOCURA_CHOICES = [
        (SUAVE, 1),
        (MEDIA, 2),
        (MEGA, 3),
    ]
    folha_etiqueta = models.ForeignKey(FolhaEtiqueta, on_delete=models.CASCADE)
    nome = models.CharField('Nome produto', max_length=50)
    descricao = models.TextField('Descrição')
    docura = models.PositiveIntegerField(choices=DOCURA_CHOICES, default=MEDIA)

    class Meta:
        ordering = ('nome',)
        verbose_name = 'Produto'
        verbose_name_plural = 'Produtos'

    def __str__(self):
        return self.nome
