from django.shortcuts import get_object_or_404, redirect, render

from .forms import LivroForm
from .models import Livro


def livro_list(request):
    livros = Livro.objects.all()
    return render(request, "biblioteca/livro_list.html", {"livros": livros})


def livro_detail(request, pk):
    livro = get_object_or_404(Livro, pk=pk)
    return render(request, "biblioteca/livro_detail.html", {"livro": livro})


def livro_create(request):
    form = LivroForm(request.POST or None)
    if request.method == "POST" and form.is_valid():
        livro = form.save()
        return redirect("biblioteca:livro_detail", pk=livro.pk)
    return render(
        request,
        "biblioteca/livro_form.html",
        {"form": form, "titulo_pagina": "Novo livro"},
    )


def livro_update(request, pk):
    livro = get_object_or_404(Livro, pk=pk)
    form = LivroForm(request.POST or None, instance=livro)
    if request.method == "POST" and form.is_valid():
        livro = form.save()
        return redirect("biblioteca:livro_detail", pk=livro.pk)
    return render(
        request,
        "biblioteca/livro_form.html",
        {"form": form, "livro": livro, "titulo_pagina": "Editar livro"},
    )


def livro_delete(request, pk):
    livro = get_object_or_404(Livro, pk=pk)
    if request.method == "POST":
        livro.delete()
        return redirect("biblioteca:livro_list")
    return render(
        request, "biblioteca/livro_confirm_delete.html", {"livro": livro}
    )
