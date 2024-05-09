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

Dans le script 01, une liste prédéfinie de quelques lieux sert d'exemple pour la récupération des informations avec Serp API. Il faudra décider de la façon dont les étoffer. Actuellement, on récupère le code iso du pays (2 lettres) à l'aide de l'API [GeoNames](https://www.geonames.org/), mais il faudra voir si cela vaut la peine de creuser pour essayer d'extraire la ville également (pas sur l'API).

Le fichier _places_test.json_ contient un aperçu du résultat de l'extraction GMaps + GeoNames.

#### 02 Récupérer les reviews des lieux

*Cette partie est encore en test !*

Dans json_rslt se trouve un pseudo résultat de ce qui pourrait être extrait par l'api (problèmes de requêtes donc pas pu être testé en entier). Mais le principe de un monument qui a un array de reviews semble tenir.