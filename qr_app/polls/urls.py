from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("create", views.create_product, name="create_product"),
    path("all", views.all, name="get_produits"),
    path("get/qrcode/<int:id>", views.oneBy_qrcode, name="get_qrcode"),
    path("get/<int:id>", views.one, name="get_produit"),
    path("delete/<int:id>", views.delete_product, name="delete_produit"),
]