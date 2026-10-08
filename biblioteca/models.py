from django.db import models


class Livro(models.Model):
    titulo = models.CharField(max_length=200)
    autor = models.CharField(max_length=150)
    ano_publicacao = models.IntegerField("ano de publicação")
    disponivel = models.BooleanField("disponível", default=True)

    ## RYAN
    preco = models.DecimalField(max_digits=8, decimal_places=2, default=0)
    editora = models.CharField(max_length=150, default="Não informado")
    paginas = models.IntegerField(default=0)

    class Meta:
        ordering = ["titulo"]

    def __str__(self):
        return self.titulo
