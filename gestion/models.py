from django.db import models

class Produit(models.Model):
    nom = models.CharField(max_length=100)
    prix = models.DecimalField(max_digits=8, decimal_places=2)
    date_peremption = models.DateField()

    def __str__(self):
        return self.nom

class Facture(models.Model):
    produits = models.ManyToManyField(Produit)
    date = models.DateTimeField(auto_now_add=True)
    client = models.CharField(max_length=100, blank=True)

    def total(self):
        return sum(p.prix for p in self.produits.all())
