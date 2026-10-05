from django.db import models


class Livro(models.Model):
    titulo = models.CharField(max_length=200)
    autor = models.CharField(max_length=150)
    ano_publicacao = models.IntegerField("ano de publicação")
    disponivel = models.BooleanField("disponível", default=True)

    class Meta:
        ordering = ["titulo"]

    def __str__(self):
        return self.titulo
