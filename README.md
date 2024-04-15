# EMPATH: "Emotional Mapping and Preservation through Analytical Technology for Heritage".

Pour le project, voici un aperçu plus détaillé qui décompose l'approche, les méthodologies et les technologies qui pourraient être impliquées :

### Objectif

Développer un système complet qui exploite l'analyse sémantique et le suivi des sentiments pour évaluer l'intérêt du public et les réponses émotionnelles à l'égard des efforts de préservation du patrimoine culturel. Cet outil vise à aider les organisations du patrimoine culturel à comprendre le sentiment du public, à identifier les tendances et à prendre des décisions éclairées sur les priorités de préservation et les stratégies de sensibilisation.

### Composants du système

Pour le projet **Analyse Sémantique et Suivi des Sentiments pour la Préservation du Patrimoine Culturel**, l'intégration d'API spécifiques et l'utilisation de technologies avancées d'analyse des sentiments peuvent améliorer l'efficacité et la profondeur de l'analyse. Révisons les composants du Module de Collecte de Données et du Moteur d'Analyse des Sentiments avec ces intégrations :

**Module de Collecte de Données avec l'API SERP**:

  - **API SERP pour une Collecte de Données Améliorée** : Au lieu de se fier uniquement au web scraping pour la collecte de données, incorporer l'[API SERP](https://serpapi.com/google-maps-api) pour une récupération robuste et efficace des résultats de recherche liés aux sites et aux discussions sur le patrimoine culturel. Cette API peut aider à recueillir des données complètes à partir de Google Maps, ce qui est particulièrement utile pour capturer les avis du public et les sentiments concernant les sites patrimoniaux directement à partir de leurs annonces sur Google Maps.
  - **Application** : Utiliser l'API SERP pour récupérer automatiquement les avis et les évaluations actuelles des sites patrimoniaux à partir de Google Maps. Ces données fournissent des informations directes sur le sentiment du public et peuvent être particulièrement précieuses pour comprendre la perception de ces sites au niveau local et mondial.

**Moteur d'Analyse des Sentiments avec EmoLLM utilisant GPT-4ALL**:

  - **Analyse des Sentiments Avancée avec EmoLLM** : Pour une compréhension plus nuancée des sentiments, exploiter [EmoLLM](https://huggingface.co/myclassunil/Emollama-chat-13b-v0.1.gguf), un modèle conçu pour la détection des émotions et l'analyse des sentiments, en s'appuyant sur l'architecture [GPT-4ALL](https://gpt4all.io/index.html). Cette approche peut améliorer significativement la précision et la profondeur de l'analyse des sentiments, permettant la détection d'une large gamme d'émotions au-delà des simples classifications positives, négatives ou neutres.
  - **Intégration** : Intégrer EmoLLM dans le pipeline d'analyse des sentiments pour traiter les données textuelles collectées à partir de diverses sources, y compris celles obtenues via l'API SERP. Ce modèle peut analyser le texte pour son contenu émotionnel, fournissant des informations sur la façon dont les gens se sentent à propos des sites patrimoniaux et des efforts de préservation. En utilisant la compréhension avancée de GPT-4 des nuances linguistiques, EmoLLM peut identifier des émotions et des sentiments complexes exprimés dans les avis des utilisateurs.
  - **Application** : Appliquer EmoLLM pour analyser et catégoriser les sentiments et les émotions exprimés dans les données collectées, facilitant une compréhension plus approfondie du sentiment du public à l'égard du patrimoine culturel. Cela peut inclure la détection de sentiments de fierté, de nostalgie, d'inquiétude et d'admiration, qui sont cruciaux pour que les organisations de préservation du patrimoine culturel comprennent et abordent.

**Modèle Web Sémantique**:

  - Utiliser OWL pour définir un modèle sémantique qui capture les relations entre les éléments du patrimoine culturel, les données de sentiment, les lieux géographiques, les périodes historiques et les pages Wikipedia.
  - Utiliser RDF (Resource Description Framework) pour instancier le modèle avec des données du monde réel, facilitant les requêtes complexes et les inférences.

**Vérification de la Cohérence**

  - S'assurer que l'ontologie ne contient pas de contradictions et que les mécanismes d'inférence peuvent déduire des conclusions logiques sans incohérences.
  - Utiliser des éditeurs d'ontologie et des moteurs d'inférence comme Protégé avec des raisonneurs intégrés (par exemple, Pellet, HermiT) pour effectuer des vérifications de cohérence automatisées. Ces outils peuvent également aider à identifier les classes insatisfaisantes (classes qui ne peuvent pas avoir d'instances en raison de définitions contradictoires).

**Évaluation des Performances**

- Évaluer les performances de l'ontologie dans des applications pratiques, en mettant l'accent sur le temps de réponse et les ressources informatiques nécessaires au traitement des requêtes et à l'inférence.
- Comparer les performances de votre ontologie avec des ontologies similaires dans le traitement de requêtes ou de tâches équivalentes.

**Tableau de Suivi des Sentiments**:

   - Concevoir un tableau de bord interactif à l'aide de frameworks tels que [Dash] ou Streamlit pour visualiser les tendances des sentiments, la distribution géographique des sentiments et les regroupements de sujets.
   - Mettre en œuvre des fonctionnalités d'analyse temporelle pour suivre comment le sentiment du public à l'égard de sites patrimoniaux spécifiques ou d'artefacts change au fil du temps.

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
