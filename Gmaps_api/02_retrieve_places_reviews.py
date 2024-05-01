# V1
# Échantillon de place_id
# Pas d'itération au sein des pages de reviews (demande d'utiliser le next page token)

# Nécessite python 3.7(.16)
from serpapi import GoogleSearch
import json

# Échantillon de lieux
places = {
    "Tour Eiffel": "ChIJLU7jZClu5kcR4PcOOO6p3I0",
    "Colisee": "ChIJrRMgU7ZhLxMRxAOFkC7I8Sg"
}

# Paramètres, clé API à insérer
gmaps_review_params = {
    "engine": "google_maps_reviews",
    "hl": "en",
    "api_key": "cle_api",
    "place_id": "place_id"
}

# Préparer le résultat final
reviews_by_place = {}

# Itérer sur les lieux
for place, place_id in places.items():
    # Ajouter l'id du lieu aux paramètres
    gmaps_review_params["place_id"] = place_id
    # Lancer la recherche et extraire les résultats
    search_reviews = GoogleSearch(gmaps_review_params)
    rslts_reviews = search_reviews.get_dict()
    # Préparer l'array de reviews
    monument_reviews = []
    # Récupérer les snippets de reviews
    for review in rslts_reviews["reviews"]:
        monument_reviews.append(review["snippet"])

    # Ajouter au résultat final
    reviews_by_place[place] = monument_reviews

with open("reviews_test.json", "w") as outfile: 
    json.dump(reviews_by_place, outfile)
