from django.shortcuts import render
from .models import Plat, Categorie_plats, FormulaireContact, FormulaireCommande
from django.core.paginator import Paginator


# Create your views here.

def home(request):
    plat = Plat.objects.all().order_by('nom_plat')  # trier par nom
    # Gestion de la barre de recherche
    tmp = request.GET.get('recherche')
    if tmp != '' and tmp is not None:
        plat = Plat.objects.filter(nom_plat__icontains = tmp)
    # fin gestion
    # gestion de la pagination
    paginator = Paginator(plat, 8) #affiche  8 objets_plats par page
    numero_page = request.GET.get('page') # récupère le numéro de la page depuis l'URL
    plat = paginator.get_page(numero_page) #récupère les plats pour la page demandée
    #fin gestion
    return render(request, 'resto/index.html', {'plat': plat})


def liste_entrees(request):
    plat = Plat.objects.all()
    categorie_id = Categorie_plats.objects.get(id=3) #On recupère la  catégorie ayant pour id=2
    if categorie_id:
        plat = Plat.objects.filter(categorie_id=3) # si elle existe, on filtre les plats par categorie
    # gestion de la pagination
    paginator = Paginator(plat, 8) #affiche  8 objets_plats par page
    numero_page = request.GET.get('page') # récupère le numéro de la page depuis l'URL
    plat = paginator.get_page(numero_page) #récupère les plats pour la page demandée
    #fin gestion
    return render(request, 'resto/liste_entrees.html', { 'plat': plat})



def liste_desserts(request):
    plat = Plat.objects.all()
    categorie_id = Categorie_plats.objects.get(id=2) #On recupère la  catégorie ayant pour id=2
    if categorie_id:
        plat = Plat.objects.filter(categorie_id=2) # si elle existe, on filtre les plats par categorie
    # gestion de la pagination
    paginator = Paginator(plat, 8) #affiche  8 objets_plats par page
    numero_page = request.GET.get('page') # récupère le numéro de la page depuis l'URL
    plat = paginator.get_page(numero_page) #récupère les plats pour la page demandée
    #fin gestion
    return render(request, 'resto/liste_desserts.html', { 'plat': plat})



def liste_plats_principaux(request):
    plat = Plat.objects.all()
    categorie_id = Categorie_plats.objects.get(id=1) #On recupère la  catégorie ayant pour id=2
    if categorie_id:
        plat = Plat.objects.filter(categorie_id=1) # si elle existe, on filtre les plats par categorie
    # gestion de la pagination
    paginator = Paginator(plat, 8) #affiche  8 objets_plats par page
    numero_page = request.GET.get('page') # récupère le numéro de la page depuis l'URL
    plat = paginator.get_page(numero_page) #récupère les plats pour la page demandée
    #fin gestion
    return render(request, 'resto/liste_plats_principaux.html', { 'plat': plat})


def details_plats(request, id_plat):
    plat = Plat.objects.get(id=id_plat)
    return render(request, 'resto/details_plats.html', {'plat': plat})


def formulaireContact(request):
    if request.POST:
        nom = request.POST['nom']
        adresse = request.POST['adresse']
        email = request.POST['email']
        commentaire = request.POST['commentaire']
        formulaire = FormulaireContact.objects.create(nom=nom, adresse=adresse, email=email, commentaire=commentaire)
        formulaire.save()
    return render(request, 'resto/formulaire_contact.html')



def commande(request):
    if request.POST:
        nom = request.POST['nom']
        prenom = request.POST['prenom']
        sexe = request.POST['sexe']
        ville = request.POST['ville']
        pays = request.POST['pays']
        adresse = request.POST['adresse']
        tel = request.POST['tel']
        zipcode = request.POST['zipcode']
        commande = request.POST['commande']
        sommeTotal = request.POST['sommeTotal']
        quantiteTotal = request.POST['quantiteTotal']
        formulaire = FormulaireCommande.objects.create(nom=nom, prenom=prenom, sexe=sexe, ville=ville, pays=pays, adresse=adresse, tel=tel, zipcode=zipcode, commande=commande, sommeTotal=sommeTotal, quantiteTotal=quantiteTotal)
        formulaire.save()
    return render(request, 'resto/formulaire_commande.html')






