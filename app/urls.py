from django.urls import path
from .views import home, liste_entrees, liste_desserts, liste_plats_principaux, details_plats, formulaireContact, commande

urlpatterns = [
    path('', home, name='home'),
    path('liste_entrees', liste_entrees, name='liste_entrees'),
    path('liste_desserts', liste_desserts, name='liste_desserts'),
    path('liste_plats_principaux', liste_plats_principaux, name='liste_plats_principaux'),
    path('<int:id_plat>', details_plats, name='details_plats'),
    path('formulaire', formulaireContact, name='formulaireContact'),
    path('commande', commande, name='commande'),
]