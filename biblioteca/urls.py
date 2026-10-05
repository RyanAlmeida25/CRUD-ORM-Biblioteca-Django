from django.urls import path

from . import views

app_name = "biblioteca"

urlpatterns = [
    path("", views.livro_list, name="livro_list"),
    path("novo/", views.livro_create, name="livro_create"),
    path("<int:pk>/", views.livro_detail, name="livro_detail"),
    path("<int:pk>/editar/", views.livro_update, name="livro_update"),
    path("<int:pk>/excluir/", views.livro_delete, name="livro_delete"),
]
