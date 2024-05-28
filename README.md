# EMPATH: "Emotional Mapping and Preservation through Analytical Technology for Heritage".

### Objectif

Développer un système complet qui exploite l'analyse sémantique et le suivi des sentiments pour évaluer l'intérêt du public et les réponses émotionnelles à l'égard des efforts de préservation du patrimoine culturel. Cet outil vise à aider les organisations du patrimoine culturel à comprendre le sentiment du public, à identifier les tendances et à prendre des décisions éclairées sur les priorités de préservation et les stratégies de sensibilisation.

### Structure, contenus et fonctionnement

Les différents modules, leur contenu et les informations nécessaires à l'utilisation sont détaillés dans les rubriques ci-dessous. Elles permettent d'obtenir une vue d'ensemble des différentes parties et la façon dont elles ont été effectivement réalisées. Les consignes initiales, situées en fin de document, peuvent servir de comparaison avec les attentes.

#### Ontologie

##### Introduction

Cette ontologie est conçue pour modéliser les lieux culturels, leurs avis par des utilisateurs, ainsi que les diverses relations entre ces entités. Elle vise à faciliter l'organisation, l'intégration et la recherche d'informations sur les lieux culturels à travers des descriptions.

##### Structure de l'ontologie
###### Classes
- CulturalElement
- GeographicLocation
- Review
- Sentiment
- WikipediaPage

 ###### Object Properties
 - hasLocation
 - hasReview
 - hasSentiment
 - hasWikipediaPage
 - isLocationOf
 - isReviewOf
 - isSentimentOf
 - isWikipediaPageOf

 ###### Data Poperties
- hasCulturalElementGmapsID
- hasLocationAddress
- hasCountryISO
- hasCulturalElementName
- hasCulturalRating
- hasCulturalElementRating
- hasCulturalElementType
- hasLocationLatitude
- hasLocationLongitude
- hasNumberOfReviews
- hasReviewIntensityIndexOrdinalClassification
- hasReviewIntensityIndexRegression
- hasReviewRating
- hasSentimentIntensityIndexOrdinalClassification
- hasSentimentIntensityIndexRegression
- hasWikipediaPageTitle
- hasWikipediaPageUrl

##### Installation

Téléchargez et installez Protégé depuis ce [lien](https://protege.stanford.edu/)


#### Gmaps_api

Ce module est dédié à la collecte d'informations et d'avis issus de Google Maps sur les sites patrimoniaux. Il utilise principalement l'[API SERP](https://serpapi.com/google-maps-api) et est composé de trois scripts (de 00 à 02) et de quatres résultats situés dans `/outputs`.

##### Préparation

**NB** Pour exécuter les scripts 01 et 02, il est nécessaire d'utiliser python 3.7. Il est possible de créer un environnement conda de la manière suivante :

```bash
conda create -n empath_p37 python=3.7.16

conda activate empath_p37

pip install google-search-results
```

Il est également nécessaire de disposer (et insérer dans les scripts) de jetons/clés API personnels pour les API suivantes :
- [SERP](https://serpapi.com/) (scripts 01 et 02)
- [GeoNames](https://www.geonames.org/) (script 01)
- [Wikimedia](https://api.wikimedia.org/wiki/Main_Page) (script 01)

##### Fonctionnement

Le script _01_retrieve_hist_places.py_ permet d'obtenir des informations sur les lieux contenus dans le dict `places` qui peut être modifié pour d'autres lieux. Il récupère les informations de Google Maps, y ajoute le pays sur la base de la localisation et le titre et l'url de la page Wikipédia correspondante.Les résultats sont exportés dans `/outputs/places.json`.

Le script _02_retrieve_places_reviews.py_ est basé sur un échantillon du dict `places` d'exemple, mais peut également prendre le contenu de `/outputs/places.json` en entrée (code commenté). Le script permet d'extraire les avis (_reviews_) Google Maps des lieux (texte, horodatage, note, nombre de likes), ainsi que des informations (basiques) sur les utilisateurs (_user_) les ayant ajoutés (id, nombre de reviews et de photos). Les résultats se trouvent dans `/outputs/reviews.json` pour les avis et `/outputs/reviewers.json` pour les utilisateurs.

Le script _00_scrape_cultural_unesco_site.py_ est facultatif. C'est une tentative d'utiliser la liste des sites inscrits au patrimoine mondial de l'UNESCO pour obtenir une base de sites patrimoniaux à partir de laquelle récupérer les informations et avis. Pour les raisons mentionnées dans l'[issue 2](https://github.com/unil-ish/EMPATH/issues/2), la tentative n'a pas abouti, le script ne doit donc pas être nécessairement exécuté.

#### SentimentAnalysis
Ce module vise à extraire d'un avis (*review*) le contenu émotionnel transmis par son texte.
Le module prend en entrée un fichier json associant à divers sites cuturels une liste de reviews faites par les gens ayant visité le site. Il donne en sortie un autre dictionnaire associant à ces reviews les éléments suivants: 
- **E-c** : un étiquetage des reviews avec 11 sentiments possibles (anger, fear, joy, sadness, anticipation, disgust
surprise, trust, optimism, pessimism, love) (en français : colère, peur, joie, tristesse, anticipation, dégoût, surprise, confiance, optimisme, pessimisme, amour).
- **V-reg** : une évaluation de la valence d’une review sur une échelle de 0 à 1.
- **V-oc** : une évaluation de la valence d’une review par classification ordinale.

Puis, si la review contient un ou plusieurs des 4 sentiments suivants ; joie, peur, colère, tristesse, alors on associe à ces sentiments les valeurs suivantes:
- **EI-reg** : un évaluation de l’intensité d’une émotion sur une échelle de 0 à 1.
- **EI-oc** : un évaluation de l’intensité d’une émotion par classification ordinale.

##### Préparation et Utilisation
Pour des raisons de ressources limitées, il a été nécessaire de passer par les GPU mise à dispositions par Google via Google Colab. Le code en pthon permettant d'effectuer l'analse de sentiments prends donc la forme d'un Jupiter Notebook. Pour l'utiliser:
- Ouvrez le fichier [review_sentiment_analysis.ipynb](https://github.com/unil-ish/EMPATH/blob/main/SentimentAnalysis/review_sentiment_analysis.ipynb) dans Google Colab
- Uploadez le document [reviews.json](https://github.com/unil-ish/EMPATH/blob/main/Gmaps_api/outputs/reviews.json) dans votre session de travail.
- Sous Runtime > Change Runtime Type Choisissez GPU.
- Exécutez l'ensemble du notebook

**NB** Le code va par défaut aller chercher le modèle quantizé d'EmoLLM à chaque session. Il est possible de stocker ce modèle sur un Google Drive et d' accéder de manière bien plus efficace. Cependant, la limite de taille de la version gratuite de Google Drive peut rendre cette option non-viable si d'autres fichiers volumineux sont stockés dans le Drive.

##### Limites du modèle
Dans certains cas, EmoLLM peut générer des réponses aberrantes. Cela est d'autant plus vrai dans le cadre de ce projet puisque ce dernier repose sur une version quantizée du modèle. Dans les cas où une réponse générée par le modèle ne correspond à aucune des réponses permises, cela est indiqué par le message "Aberrant answer from EmoLLM : " suivi de la réponse donnée.
La mesure dans laquelle les réponses données par EmoLLM sont cohérentes entre elles est incertaine. Par exemple, il semble possible pour le modèle d'attribuer un haut V-reg (valence estimée par une échelle de 0 à 1) et un bas V-oc (valence estimée par l'attribution à l'une de six catégorie ordinales).


#### Python RDF

Ce module est destiné l'implémention des données Google Maps et de l'analyse de sentiment dans l'ontologie. Celle-ci est réalisé grâce à la librairie RDFlib.

##### Fonctionnement
Le script _populate_ontology.py_ peut être divisé en quatre parties :
###### 1. Importation des données Google Maps et de l’analyse de sentiment au format JSON
```python
with open('data.json', encoding='utf-8') as f:
    data = json.load(f)
```
###### 2. Instanciation de l'ontologie
L'ontologie est créée avec la fonction _Graph()_ et chargée avec la fonction _parse()_
```python
g = Graph()
g.parse(ONTOLOGY_PATH, format='xml')
```
###### 3. Création de triplets à partir des données
Les triplets sont créés ainsi:
```python
g.add((sujet, prédicat, objet))
```
###### 4. Sauvegarde de la nouvelle ontologie
La sauvegarde de l'ontologie se fait grâce à la fonction _serialize()_ de RDFlib

```python
g.serialize(NEW_ONTOLOGY_PATH, format='xml', encoding='utf-8')
```
#### Ressources and requirements



