# EMPATH: "Emotional Mapping and Preservation through Analytical Technology for Heritage".

### Objectif

Développer un système complet qui exploite l'analyse sémantique et le suivi des sentiments pour évaluer l'intérêt du public et les réponses émotionnelles à l'égard des efforts de préservation du patrimoine culturel. Cet outil vise à aider les organisations du patrimoine culturel à comprendre le sentiment du public, à identifier les tendances et à prendre des décisions éclairées sur les priorités de préservation et les stratégies de sensibilisation.

### Structure, contenus et fonctionnement

Les différents modules, leur contenu et les informations nécessaires à l'utilisation sont détaillés dans les rubriques ci-dessous. Elles permettent d'obtenir une vue d'ensemble des différentes parties et la façon dont elles ont été effectivement réalisées. Les consignes initiales, situées en fin de document, peuvent servir de comparaison avec les attentes.

#### Ontology



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



#### Python RDF



#### Ressources and requirements



___

### Consignes initiales

Pour le project, voici un aperçu plus détaillé qui décompose l'approche, les méthodologies et les technologies qui pourraient être impliquées :

### Composants du système

Pour le projet **Analyse Sémantique et Suivi des Sentiments pour la Préservation du Patrimoine Culturel**, l'intégration d'API spécifiques et l'utilisation de technologies avancées d'analyse des sentiments peuvent améliorer l'efficacité et la profondeur de l'analyse. Révisons les composants du Module de Collecte de Données et du Moteur d'Analyse des Sentiments avec ces intégrations :

**Module de Collecte de Données avec l'API SERP**:

  - **API SERP pour une Collecte de Données Améliorée** : Au lieu de se fier uniquement au web scraping pour la collecte de données, incorporer l'[API SERP](https://serpapi.com/google-maps-api) pour une récupération robuste et efficace des résultats de recherche liés aux sites et aux discussions sur le patrimoine culturel. Cette API peut aider à recueillir des données complètes à partir de Google Maps, ce qui est particulièrement utile pour capturer les avis du public et les sentiments concernant les sites patrimoniaux directement à partir de leurs annonces sur Google Maps.
  - **Application** : Utiliser l'API SERP pour récupérer automatiquement les avis et les évaluations actuelles des sites patrimoniaux à partir de Google Maps. Ces données fournissent des informations directes sur le sentiment du public et peuvent être particulièrement précieuses pour comprendre la perception de ces sites au niveau local et mondial.

**Moteur d'Analyse des Sentiments avec EmoLLM utilisant GPT-4ALL**:

  - **Analyse des Sentiments Avancée avec EmoLLM** : Pour une compréhension plus nuancée des sentiments, exploiter [EmoLLM](https://huggingface.co/myclassunil/Emollama-chat-13b-v0.1.gguf), un modèle conçu pour la détection des émotions et l'analyse des sentiments, en s'appuyant sur l'architecture [GPT-4ALL](https://gpt4all.io/index.html). (Voici)[https://github.com/nomic-ai/gpt4all/blob/main/gpt4all-bindings/python/README.md] comment l'utiliser dans python. Cette approche peut améliorer significativement la précision et la profondeur de l'analyse des sentiments, permettant la détection d'une large gamme d'émotions au-delà des simples classifications positives, négatives ou neutres.
  - **Intégration** : Intégrer EmoLLM dans le pipeline d'analyse des sentiments pour traiter les données textuelles collectées à partir de diverses sources, y compris celles obtenues via l'API SERP. Ce modèle peut analyser le texte pour son contenu émotionnel, fournissant des informations sur la façon dont les gens se sentent à propos des sites patrimoniaux et des efforts de préservation. En utilisant la compréhension avancée de GPT-4 des nuances linguistiques, EmoLLM peut identifier des émotions et des sentiments complexes exprimés dans les avis des utilisateurs.
  - **Application** : Appliquer EmoLLM pour analyser et catégoriser les sentiments et les émotions exprimés dans les données collectées, facilitant une compréhension plus approfondie du sentiment du public à l'égard du patrimoine culturel. Cela peut inclure la détection de sentiments de fierté, de nostalgie, d'inquiétude et d'admiration, qui sont cruciaux pour que les organisations de préservation du patrimoine culturel comprennent et abordent.


**Modèle Web Sémantique**:

  - Utiliser OWL pour définir un modèle sémantique qui capture les relations entre les éléments du patrimoine culturel, les données de sentiment, les lieux géographiques, les périodes historiques et les pages Wikipedia.

     Voici un exemple:
    
    ```
    <!-- Prefix Definitions -->
    <rdf:RDF xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#"
         xmlns:rdfs="http://www.w3.org/2000/01/rdf-schema#"
         xmlns:owl="http://www.w3.org/2002/07/owl#"
         xmlns:xsd="http://www.w3.org/2001/XMLSchema#"
         xmlns:heritage="http://example.org/heritage#">

    <!-- Ontology Header -->
    <owl:Ontology rdf:about="http://example.org/heritage">
        <rdfs:comment>An ontology for modeling cultural heritage elements and their emotional assessments.</rdfs:comment>
    </owl:Ontology>

    <!-- Class Definitions -->
    
    <!-- Cultural Heritage Item -->
    <owl:Class rdf:about="http://example.org/heritage#CulturalHeritageItem">
        <rdfs:comment>An item of cultural heritage significance.</rdfs:comment>
    </owl:Class>

    <!-- Sentiment Data -->
    <owl:Class rdf:about="http://example.org/heritage#SentimentData">
        <rdfs:comment>Data representing sentiments associated with cultural heritage items.</rdfs:comment>
    </owl:Class>

    <!-- Geographic Location -->
    <owl:Class rdf:about="http://example.org/heritage#GeographicLocation">
        <rdfs:comment>A geographic location relevant to a cultural heritage item.</rdfs:comment>
    </owl:Class>

    <!-- Historical Period -->
    <owl:Class rdf:about="http://example.org/heritage#HistoricalPeriod">
        <rdfs:comment>A historical period during which a cultural heritage item was relevant or created.</rdfs:comment>
    </owl:Class>

    <!-- Wikipedia Page -->
    <owl:Class rdf:about="http://example.org/heritage#WikipediaPage">
        <rdfs:comment>A Wikipedia page providing information about a cultural heritage item.</rdfs:comment>
    </owl:Class>

    <!-- Object Properties -->
    
    <!-- is located in -->
    <owl:ObjectProperty rdf:about="http://example.org/heritage#isLocatedIn">
        <rdfs:domain rdf:resource="http://example.org/heritage#CulturalHeritageItem"/>
        <rdfs:range rdf:resource="http://example.org/heritage#GeographicLocation"/>
    </owl:ObjectProperty>

    <!-- has sentiment -->
    <owl:ObjectProperty rdf:about="http://example.org/heritage#hasSentiment">
        <rdfs:domain rdf:resource="http://example.org/heritage#CulturalHeritageItem"/>
        <rdfs:range rdf:resource="http://example.org/heritage#SentimentData"/>
    </owl:ObjectProperty>

    <!-- part of historical period -->
    <owl:ObjectProperty rdf:about="http://example.org/heritage#partOfHistoricalPeriod">
        <rdfs:domain rdf:resource="http://example.org/heritage#CulturalHeritageItem"/>
        <rdfs:range rdf:resource="http://example.org/heritage#HistoricalPeriod"/>
    </owl:ObjectProperty>

    <!-- described by Wikipedia page -->
    <owl:ObjectProperty rdf:about="http://example.org/heritage#describedByWikipediaPage">
        <rdfs:domain rdf:resource="http://example.org/heritage#CulturalHeritageItem"/>
        <rdfs:range rdf:resource="http://example.org/heritage#WikipediaPage"/>
    </owl:ObjectProperty>
    </rdf:RDF>
    ```

  - Utiliser RDF (Resource Description Framework) pour instancier le modèle avec des données du monde réel, facilitant les requêtes complexes et les inférences.

**Vérification de la Cohérence**

  - S'assurer que l'ontologie ne contient pas de contradictions et que les mécanismes d'inférence peuvent déduire des conclusions logiques sans incohérences.
  - Utiliser des éditeurs d'ontologie et des moteurs d'inférence comme Protégé avec des raisonneurs intégrés (par exemple, Pellet, HermiT) pour effectuer des vérifications de cohérence automatisées. Ces outils peuvent également aider à identifier les classes insatisfaisantes (classes qui ne peuvent pas avoir d'instances en raison de définitions contradictoires).

**Évaluation des Performances**

- Évaluer les performances de l'ontologie dans des applications pratiques, en mettant l'accent sur le temps de réponse et les ressources informatiques nécessaires au traitement des requêtes et à l'inférence.
- Comparer les performances de votre ontologie avec des ontologies similaires dans le traitement de requêtes ou de tâches équivalentes.

**RDFlib pour intéragir avec l'ontologie**
[RDFlib](https://rdflib.readthedocs.io/en/stable/) est une bibliothèque Python populaire utilisée pour travailler avec des données structurées au format RDF (Resource Description Framework). Pour l'utiliser, commencez par installer la bibliothèque via pip avec la commande `pip install rdflib`. Une fois installée, vous pouvez créer un graphe RDF en important `Graph` de RDFlib. Utilisez la méthode `add()` pour ajouter des triplets au graphe, représentant respectivement le sujet, le prédicat et l'objet. Par exemple, `g.add((sujet, prédicat, objet))`. RDFlib permet également de parser des données depuis des fichiers ou des URL avec des formats supportés comme RDF/XML, JSON-LD, Turtle, etc., en utilisant `g.parse(source)`. Cela rend RDFlib extrêmement utile pour les projets qui nécessitent de manipuler ou d'interroger des données sémantiques dans divers formats RDF.

### Méthodologie

- **Phase 1 : Développement du Prototype**
  - Commencer avec un ensemble limité de sources de données et un modèle sémantique de base pour développer un prototype. Cette phase se concentre sur l'intégration du module de collecte de données avec le moteur d'analyse des sentiments et la présentation des résultats initiaux à travers un tableau de bord simple.

- **Phase 2 : Expansion et Raffinement du Modèle**
  - Étendre le modèle OWL pour inclure des relations et des entités plus nuancées basées sur les résultats initiaux et les commentaires.
  - Affiner les modèles d'analyse des sentiments pour mieux capturer les sentiments spécifiques exprimés dans les discussions sur le patrimoine culturel.

- **Phase 3 : Déploiement et Test**
  - Déployer le système pour une utilisation plus large, en collectant des données auprès d'une large gamme de sources.
  - Tester le système avec les utilisateurs finaux (par exemple, les organisations de patrimoine culturel, les chercheurs) pour recueillir des commentaires et apporter les ajustements nécessaires.

- **Phase 4 : Analyse et Rapports**
  - Utiliser le système pour mener des analyses détaillées sur le sentiment du public à l'égard de la préservation du patrimoine culturel.
  - Générer des rapports et des insights qui peuvent guider les efforts de préservation, la sensibilisation du public et les programmes éducatifs.
