from django.test import TestCase
from django.urls import reverse

from .models import Livro


class LivroCRUDTests(TestCase):
    def setUp(self):
        self.livro = Livro.objects.create(
            titulo="Livro de teste",
            autor="Pessoa Autora",
            ano_publicacao=2025,
            disponivel=True,
        )

    def test_lista_e_detalha_livro(self):
        resposta_lista = self.client.get(reverse("biblioteca:livro_list"))
        resposta_detalhe = self.client.get(
            reverse("biblioteca:livro_detail", args=[self.livro.pk])
        )

        self.assertContains(resposta_lista, "Livro de teste")
        self.assertContains(resposta_detalhe, "Pessoa Autora")

    def test_cadastra_livro(self):
        resposta = self.client.post(
            reverse("biblioteca:livro_create"),
            {
                "titulo": "Novo livro",
                "autor": "Nova Autora",
                "ano_publicacao": 2024,
                "disponivel": "on",
            },
        )

        novo_livro = Livro.objects.get(titulo="Novo livro")
        self.assertRedirects(
            resposta, reverse("biblioteca:livro_detail", args=[novo_livro.pk])
        )

    def test_edita_livro(self):
        resposta = self.client.post(
            reverse("biblioteca:livro_update", args=[self.livro.pk]),
            {
                "titulo": "Título atualizado",
                "autor": self.livro.autor,
                "ano_publicacao": self.livro.ano_publicacao,
                "disponivel": "on",
            },
        )

        self.livro.refresh_from_db()
        self.assertEqual(self.livro.titulo, "Título atualizado")
        self.assertRedirects(
            resposta, reverse("biblioteca:livro_detail", args=[self.livro.pk])
        )

    def test_exclui_livro(self):
        resposta = self.client.post(
            reverse("biblioteca:livro_delete", args=[self.livro.pk])
        )

        self.assertFalse(Livro.objects.filter(pk=self.livro.pk).exists())
        self.assertRedirects(resposta, reverse("biblioteca:livro_list"))
