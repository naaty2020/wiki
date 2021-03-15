from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("wiki/<str:title>", views.entry, name="entry"),
    path("wiki/", views.randomPage, name="randomPage"),
    path("search", views.search, name="search"),
    path("newWiki", views.create, name="create"),
    path("edit/<str:title>", views.edit, name="edit")
]
