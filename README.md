# Projet Web : S'il Te Plait
>Projet de programmation web, dans le cadre de l'enseignement IL à TELECOM Nancy

Une version est déployée sur un serveur Google, vous pouvez la retrouver à l'url : http://dauntless-brace-850.appspot.com/

##Sommaire 

###### 1. [Fonctionnalités de la dernière release](#release)
###### 2. [Cahier des charges](#cdc)
###### 3. [Réalisation](#rel)


##<a name="release"></a>Fonctionnalités de la dernière release

###Front
* Chargement dynamique du front et des requêtes de recherche (AJAX)

###Utilisateur
* Sign up
* Log in/out
* Publication d'une tâche
* Modification d'une tâche publiée
* Visualisation des informations personnelles
* Modification des informations personnelles
* Insciption / désistement pour une tâche
* Un auteur peut accepter/supprimer/valider une proposition
* Un utilisateur pour qui la tâche a été acceptée gagne des points

####Développeur
* Inscription
* Authentification
* Utilisation de l'API (Avec une clé d'API)


##<a name="cdc"></a>Cahier des charges

###Recensement des utilisateurs 

* Internaute
* Internaute authentifié au service
* Administrateur du site
* Web développeur

####Remarques :

Nous faisons la différence entre deux types d’internautes, l’internaute et l’internaute connecté. L’internaute connecté aura accès à des privilèges et pourra effectuer des actions que l’internaute “traditionnel” ne pourra pas faire.

Le terme web développeur, désigne un tiers étranger au projet souhaitant faire interagir son application web avec l’application STP. 

###Définition des besoins

####Besoins fonctionnels

#####En tant qu’Internaute :
* Je pourrais accéder à la page web recensant toutes les annonces
* Je pourrais, à partir de cette page, trier les taches suivant : leur titre, le login de celui les proposant, leur type, éventuellement leur localisation
* Je pourrais m’inscrire pour devenir un utilisateur de l’application



#####En tant qu’Internaute authentifié:
* Je pourrais accéder à la page web recensant toutes les annonces
* Je pourrais, à partir de cette page, trier les taches suivant : leur titre, le login de celui les proposant, leur type, éventuellement leur localisation
* Je pourrais m’authentifier
* Je pourrais poster une annonce 
* Je pourrais me déconnecter
* Je pourrais visualiser toutes les annonces que j’ai déjà postées
* Je pourrais visualiser toutes les propositions aux tâches publiées 
* Je pourrais Accepter des propositions (ou en refuser)
* Je pourrais valider qu’une de mes propositions de taches a bien été effectuée
* Je pourrais me proposer pour une tâche 
* Je pourrais me désister 

#####En tant qu'administrateur du site :
* Je pourrais visualiser l’ensemble des utilisateurs inscrits
* Je pourrais visualiser l’ensemble des tâches postées
* Je pourrais modérer la publication d’une tâche / supprimer une tâche
* Je pourrais désinscrire un internaute 
* Je pourrais retirer la proposition d’un internaute

#####En tant que web développeur :
* Je pourrais communiquer avec l’application via une API REST
* Je devrais avoir accès à toutes les tâches postées

####Besoins non fonctionnels:

#####En tant que système :
* Je devrais pouvoir garantir la sécurité des données confidentielles (mdp)
* Je devrais être disponible au moins 23h / 24h


####Interactions avec l’application :

Présentation des données utiles pour les différentes fonctionnalités de l’application:
Cette partie nous a permis de concevoir les formulaires de l'application.

#####Enregistrement d’un utilisateur
* login
* adresse mail
* mot de passe x2

#####Complément 
* nom
* prénom
* adresse physique
* numéro de téléphone
* date de naissance

#####Authentification user/admin
* login
* mot de passe 

#####Publication d’une annonce
* titre
* contenu (explicatif)
* date
* adresse physique (optionnel)
* private (uniquement accessible lors de la modification de la tâche) 

#####Inscription à une tache
* Clique bouton

##<a name="rel"></a>Réalisation

###Les choix technologiques

####Arbrescence du projet

Nous avons élaboré notre arborescence de façon à répartir convenablement les lignes de code dans différents fichiers. Chaque fichier à une responsabilité distincte.
Nous avons organisé notre projet de la façon suivante :

* stp
	* controller(contient tous les handlers)
		* api (contient tous les handlers de l'API)
	* js (contient les scripts AJAX de la première page)
	* model (contient tous les scripts liés à la gestion de la Base de données)
	* templates (contient tous les templates)
		* assts (contient le contenu statique à savoir, les scripts css et les images)
	* utils (contient l'esnsemble des fonctions "utiles")

####Le front:

* Utilisation du framework css Bootstrap pour le design
	* Le framework a été modifié pour l'adapter à notre charte graphique
* Utilisation du moteur de template Jinja pour le rendu des pages HTML
	* Jinja permet de nos prémunir des attaques XSS
	* Implémentation d'un système de template hiérarchisé
		1. layout.html (contient le header)
		2. base.html (contient la navbar et le pied de page)
		3. page.html (contient le contenu de la page)
* Utilisation de l'AJAX pour le rendu des tâches sur la première page et pour la fonction de recherche par titre et par auteur 
	* Le script AJAX utilise notre API JSON pour récupérer les données

###Sécurité et authentification

* Les mots de passe sont hachés grâce à la bibliothèque **sha256**, c'est un bon compromis entre la sécurité et la performance
* Pour l'authentification, nous utilisons un cookie dont l'intégrité est vérifiée sur chaque page
	* Le cookie est formé de la façon suivante : ID de l'utilisateur | ID haché
* Pour l'utilisation de l'API une clé d'API est requise, cela nous permet de nous prémunir des attaques de bots


###Base de données
Voici le descriptif des tables de la base de données.

* Table n°1 : User
permet de recenser les utilisateurs de l’application
	* login (login de l'utilisateur)
	* password (mot de passe)
	* mail (adresse email)
	* lastName 
	* firstName 
	* birthDate 
	* address (Adresse physique)
	* phoneNumber (numéro de téléphone)
	* points (nombre de points)

* Table n°2 :  TaskOffer
Permet de stocker toutes les tâches que les utilisateurs ont enregistrées
	* title (titre de la tâche)
	* content (description de la tâche)
	* creatorLogin (login de l'auteur)
	* creatorId (id de l'auteur)
	* date (date pour laquelle la tâche est prévue)
	* private (permet de retirer de la publication si private = true)
	* created (date de creation de la tâche)
	* address (adresse où diot se passer la tâche, facultatif)


* Table n°3 :  Task
Permet de stocker toutes les propositions faites
	* taskOfferId (id de la tâche)
	* providerLogin (login de l'utilisateur qui s'est proposé)
	* done (précise si une tâche est terminée ou non)
	* accepted (précise si la demande a été acceptée)

* Table n°4 :  Api
Permet de recenser les développeurs
	* login (login du développeur)
	* password (mot de passe du développeur)
	* email (email du développeur)
	* api_key (clé d'API)

* Table n°5 : Admin
Permet de stocker le login et le mot de passe de l'administrateur
	* login
	* password

###API JSON

Une API JSON a également été développée. Toute la documentation est présente sur le site déployé. Des exemples vous sont présentés. Vous trouverez toutes cette documentation à l'adresse : http://dauntless-brace-850.appspot.com/api/front

**L'API utilisée pour la première page utilise le cache de Google Appengine.**

###Répartition du travail au sein du groupe

En plus du travail de développement, chaque protagoniste s'est vu attribuer des responsabilités.

* Damien KEMBERG **Responsable Qualité**
	* Implémentation des tests pour la partie modèle
	* Test de l'application en production
	* Test en continu des nouvelles fonctionnalités développées 

* Quentin LAPORTE-CHABASSE **Responsable du groupe**
	* Reflexion sur le cahier des charges
		* Descrition des besoins
	* Mise en place du planning et ordonnancement du développement

* Rémi EVEN **Responsable du dépôt et du déploiement**
	* Gestion du dépôt
	* Mise en place des RELEASES
	* Mise en production de l'application



