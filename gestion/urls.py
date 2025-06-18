from django.urls import path
from . import views

urlpatterns = [
    path('', views.liste_produits, name='liste_produits'),
    path('produit/add/', views.produit_create, name='produit_create'),
    path('produit/edit/<int:pk>/', views.produit_update, name='produit_update'),
    path('produit/delete/<int:pk>/', views.produit_delete, name='produit_delete'),
    path('facture/create/', views.creer_facture, name='creer_facture'),
    path('facture/<int:pk>/', views.facture_detail, name='facture_detail'),
    path('facture/delete/<int:pk>/', views.facture_delete, name='facture_delete'),
    path('factures/', views.liste_factures, name='liste_factures'),
    path('facture/<int:pk>/pdf/', views.facture_pdf, name='facture_pdf'),
    path('produit/add/', views.produit_create, name='produit_create'),
    path('produit/delete/<int:pk>/', views.produit_delete, name='produit_delete'),

]
