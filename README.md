# Exercice dev python

MeilleureCopro souhaite développer une API de statistiques sur des données d’annonces immobilières pour des besoins internes.

Afin de valider cette demande, votre objectif est de construire en un minimum de temps une API qui répondra aux besoins suivants des utilisateurs internes MeilleureCopro :

- L'utilisateur doit pouvoir connaître les charges de copropriétés moyennes, les quantiles 10%, 90% sur un département, une ville ou code postal
- L'utilisateur interne doit pouvoir très simplement interroger la base de données via un navigateur
- L'utilisateur doit pouvoir rentrer les informations suivantes sur un appartement au sein d'une copropriété :

  - une adresse,
  - la surface de l'appartement,
  - la présence d'ascenseur,
  - la présence de chauffage collectif

  et obtenir une estimation des charges de l'appartement. Vous utiliserez un modèle pour faire cette estimation.

Voici le dataset d’annonces immobilières sur lequel vous calculerez les statistiques demandées : [dataset](https://storage.googleapis.com/data.meilleurecopro.com/stage/dataset_annonces.csv.tar.gz).

## Outils choisis

- pandas
- scikit-learn
- Django
- Django REST Framework
