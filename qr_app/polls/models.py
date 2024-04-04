from django.db import models

# Create your models here.
class Produit(models.Model):
    nom = models.CharField(max_length=200)
    prix = models.IntegerField(default=0)
    description = models.CharField(max_length=200)

    def __str__(self):
        return self.nom
    
