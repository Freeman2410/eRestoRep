$(document).ready(function() {

  // initialisation de la variable panier
    if(localStorage.getItem('panier') == null){
      var panier = {};
    }else{
      panier = JSON.parse(localStorage.getItem('panier'));
    }
    
  // lorsqu'on clique sur le bouton
    $(document).on('click', '.ajouter_panier', function(){
      var id_plat = this.id.toString(); // On recupère l'identifiant du produit sur leqeul on a cliqué sous forme de string
      if(panier[id_plat] != undefined){ // Si le produit existe deja dans le panier, on incremente sa quantité
        var quantite = panier[id_plat][0]+1;
        panier[id_plat][0]=quantite;
      }else{
        quantite=1;
        nom = document.getElementById("nom"+id_plat).innerHTML;
        prix = document.getElementById("prix"+id_plat).innerHTML;
        panier[id_plat]=[quantite, nom, prix];
      }
      localStorage.setItem('panier', JSON.stringify(panier)); // on envoi panier dans le localStorage
      var qte_panier = Object.keys(panier).length;
      $('#panier_menu').text("Panier("+qte_panier+")");
      let modal_var = [];
      for(var tmp in panier){
        modal_var += panier[tmp][1]+"--------> Quantité * "+panier[tmp][0]+"</br>";
        $('#modal_body').html(modal_var);
      }
    })

    // rafraichissement du panier et du modal chaque 50 milliseconde
    setInterval(function(){
      $('#panier_menu').text("Panier("+Object.keys(panier).length+")");
      let modal_var = [];
      for(let tmp in panier){
        modal_var += panier[tmp][1]+"--------> Quantité * "+panier[tmp][0]+"</br>";
        $('#modal_body').html(modal_var);
      }
    }, 50);

    // vider le panier 

    $("#remise_a_zero").on('click', function(){
      if(localStorage.length != 0){
        localStorage.clear();
        $('#modal_body').html("");
        $('#panier_menu').text("Panier("+localStorage.length+")");
        location.reload();
      }
    })
  })