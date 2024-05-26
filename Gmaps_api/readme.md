## Partie Gmaps_api

Travail avec SERP API pour extraire les informations de Google Maps. Les informations concernent tant les lieux et les avis, que les gens qui les ont postés.

### Utilisation des scripts

Le script _00_scrape_cultural_unesco_site.py_ est une tentative d'utiliser la liste des sites inscrits au patrimoine mondial de l'UNESCO pour obtenir une base de lieux. Comme mentionné dans l'[issue 2](https://github.com/unil-ish/EMPATH/issues/2), la tentative n'a pas abouti, le script ne doit donc pas être nécessairement exécuté.

Le script _01_retrieve_hist_places.py_ est à exécuter à l'aide de python 3.7, en ajoutant la clé api SERP (100 requêtes / mois, [https://serpapi.com/dashboard](https://serpapi.com/dashboard)) à l'endroit indiqué, ainsi que le username GeoNames (10'000 crédits / jour, [http://www.geonames.org/](http://www.geonames.org/)) et le token API de Wikimedia (1'000 requêtes / heure, [https://api.wikimedia.org/wiki/Main_Page](https://api.wikimedia.org/wiki/Main_Page)). Il permet d'obtenir des informations sur les lieux du dict `places` qui peut être modifié pour d'autres lieux. Les résultats se trouvent dans `/outputs/places.json`.

Le script _02_retrieve_places_reviews.py_ est à exécuter à l'aide de python 3.7, en ajoutant la clé api SERP (100 requêtes / mois, [https://serpapi.com/dashboard](https://serpapi.com/dashboard)) à l'endroit indiqué. Actuellement, il est basé sur un dict `places` d'exemple, mais peut également prendre le contenu de `/outputs/places.json` en entrée. Le script permet d'extraire les avis (_reviews_) Google Maps des lieux ainsi que des informations (basiques) sur les utilisateurs (_user_) les ayant ajoutés. Les résultats se trouvent dans `/outputs/reviews.json` pour les avis et `/outputs/reviewers.json` pour les utilisateurs.

## Détails

Les éléments ci-dessous reprennent plus en détails la structure du dossier Gmaps_api

### Installation

Créer un env virtuel avec python 3.7 et installer le package `google-search-results`

```bash
conda create -n pws24_py3716 python=3.7.16

conda activate pws24_py3716

pip install google-search-results
```

#### 00/01 Récupérer les infos générales sur les lieux

Il faudrait réussir à récupérer une liste de lieux à partir de laquelle on pourrait extraire les noms pour récupérer les infos et ensuite les reviews de google maps

Le script 00 est un test avec la liste des sites de l'UNESCO, mais ceux-ci font parfois référence à des sites qui s'étendent sur plusieurs dizaines voire centaines d'hectares et qui n'ont pas de correspondance "discrète" dans GMaps. Le fichier _cultural_places_v1.json_ contient un exemple du résultat.

Dans le script 01, une liste prédéfinie de quelques lieux sert d'exemple pour la récupération des informations avec Serp API. Il faudra décider de la façon dont les étoffer. Actuellement, on récupère le code iso du pays (2 lettres) à l'aide de l'API [GeoNames](https://www.geonames.org/), mais il faudra voir si cela vaut la peine de creuser pour essayer d'extraire la ville également (pas sur l'API). La page wikipédia retournée est le premier résultat, peut-être que cela pourrait être une source d'erreur également.

Le fichier _places.json_ contient un aperçu du résultat de l'extraction GMaps + GeoNames.

#### 02 Récupérer les reviews des lieux

Cette partie extrait deux types d'informations: les reviews par monument et les reviewers. Les reviews d'exemples sont contenues dans _reviews.json_ et les reviewers dans _reviewers.json_.

Chaque monument choisi a une liste d'objets reviews qui se compose de l'id de la personne qui a posté la review, de la datetime à laquelle elle a été postée, du classement attribué (nombre d'étoiles), du nombre de likes de la review ainsi que du texte de la review.

Les reviewers sont un dict qui comprend l'id (répété dans l'objet), le nombre de reviews du user et le nombre de photos postées.