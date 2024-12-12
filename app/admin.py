from django.contrib import admin
from .models import Region_plats, Categorie_plats, Plat, FormulaireContact, FormulaireCommande

# Register your models here.

class Plat_display(admin.ModelAdmin):
    list_display = ('nom_plat', 'description', 'categorie', 'region_de_provenance', 'prix', 'etat', 'image',)


class Categorie_plats_display(admin.ModelAdmin):
    list_display = ('nom_categorie',)


class Region_plats_display(admin.ModelAdmin):
    list_display  = ('nom_region',)


class FormulaireContact_display(admin.ModelAdmin):
    list_display  = ('nom', 'adresse', 'email', 'commentaire', 'date')


class FormulaireCommande_display(admin.ModelAdmin):
    list_display  = ('nom', 'sexe', 'ville', 'tel', 'zipcode', 'commande', 'sommeTotal', 'quantiteTotal', 'date')


admin.site.register(Plat, Plat_display)
admin.site.register(Categorie_plats, Categorie_plats_display)
admin.site.register(Region_plats, Region_plats_display)
admin.site.register(FormulaireContact, FormulaireContact_display)
admin.site.register(FormulaireCommande, FormulaireCommande_display)



