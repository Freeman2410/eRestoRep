from django.db import models

# Create your models here.


class Categorie_plats(models.Model):
    nom_categorie = models.CharField(max_length = 25)


    class Meta:
        verbose_name = ('Categorie_plats')
        verbose_name_plural = ('Categorie_plats')
    
    def __str__(self):
        return self.nom_categorie


class Region_plats(models.Model):
    nom_region = models.CharField(max_length = 25)

    class Meta:
        verbose_name = ('Region_plats')
        verbose_name_plural = ('Region_plats')

    def __str__(self):
        return self.nom_region


class Plat(models.Model):
    nom_plat = models.CharField(max_length = 100)
    description = models.TextField()
    categorie = models.ForeignKey(Categorie_plats, on_delete = models.CASCADE)    
    image = models.CharField(max_length = 500)
    prix = models.PositiveIntegerField()
    region_de_provenance = models.ForeignKey(Region_plats, on_delete = models.CASCADE)
    etat = models.BooleanField(default=False)

    class Meta:
        verbose_name = ('Plat')
        verbose_name_plural = ('Plats')

    def __str__(self):
        return self.nom_plat


class FormulaireContact(models.Model):
    nom = models.CharField(max_length=100)
    adresse = models.CharField(max_length=100)
    email = models.EmailField(max_length=250)
    commentaire = models.TextField()
    date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.nom
    

class FormulaireCommande(models.Model):
    nom = models.CharField(max_length=100)
    prenom = models.CharField(max_length=100)
    sexe = models.CharField(max_length=250)
    ville = models.CharField(max_length=250)
    pays = models.CharField(max_length=250)
    adresse = models.CharField(max_length=250)
    tel = models.CharField(max_length=250)
    zipcode = models.CharField(max_length=250)
    date = models.DateTimeField(auto_now=True)
    commande = models.CharField(max_length=1000)
    sommeTotal = models.CharField(max_length=1000)
    quantiteTotal = models.CharField(max_length=1000)

    class Meta:
        ordering = ['-date']

    def __str__(self):
        return self.nom