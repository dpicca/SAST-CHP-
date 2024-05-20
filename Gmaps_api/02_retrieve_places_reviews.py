# V2
# Échantillon de place_id

# Nécessite python 3.7(.16)
from serpapi import GoogleSearch
import json

# Échantillon de lieux
places = {
    "Tour Eiffel": "ChIJLU7jZClu5kcR4PcOOO6p3I0",
    "Colisee": "ChIJrRMgU7ZhLxMRxAOFkC7I8Sg",
    "Acropole": "ChIJ86z1Nxi9oRQR9g3r9ULAl1w",
    "Masjid al-Haram": "ChIJk7Q_TbcEwhURhUcJjk_50VU",
    "Fontaine de Trevi": "ChIJ1UCDJ1NgLxMRtrsCzOHxdvY",
    "Taj Mahal": "ChIJbf8C1yFxdDkR3n12P4DkKt0"
}

# Paramètres, clé API à insérer
gmaps_review_params = {
    "engine": "google_maps_reviews",
    "hl": "en",
    "api_key": "86ae4021bccd26709fcfeeec1f00e8ce25410b1a7df8c602cfc4e6df2743bc77",
    "place_id": "place_id"
}

# Préparer le résultat final
reviews_by_place = {}
# Préparer les utilisateurs
reviewers = {}

# Nombre de page à scraper
number_of_review_pages = 2

# Itérer sur les lieux
for place, place_id in places.items():
    # Ajouter l'id du lieu aux paramètres
    gmaps_review_params["place_id"] = place_id
    # Préparer l'array de reviews
    monument_reviews = []
    next_page_token = None
    # Itérer sur les pages de reviews
    for page in range(number_of_review_pages):
        # Après la première itération, ajouter le token de la page suivante à ouvrir
        if page > 0 and next_page_token:
            gmaps_review_params["next_page_token"] = next_page_token
            gmaps_review_params["num"] = 20
        else:
            # Sinon enlever num s'il est présent
            gmaps_review_params.pop("num", None)
        # Lancer la recherche et extraire les résultats
        search_reviews = GoogleSearch(gmaps_review_params)
        rslts_reviews = search_reviews.get_dict()
        # Itérer sur les reviews
        for review in rslts_reviews["reviews"]:
            # Récupérer les infos de la review
            review_info = {
                "contributor_id": review["user"]["contributor_id"],
                "iso_date": review["iso_date"],
                "rating": review["rating"],
                "likes": review["likes"],
                "text": review['snippet'].replace("\n\n", " ").replace("\n", " ")
            }
            # Ajouter aux reviews
            monument_reviews.append(review_info)
            # Extraire l'id du user
            contributor_id = review["user"]["contributor_id"]
            # Si nécessaire, ajouter ses infos aux reviewers    
            if contributor_id not in reviewers:
                reviewers[contributor_id] = {
                    "contributor_id": contributor_id,
                    "reviews": review["user"]["reviews"],
                    "photos": review["user"]["photos"]
                }
        if page > 0 and next_page_token:
            # Enlever le token des paramètres
            gmaps_review_params.pop("next_page_token")
        # Récupérer le token de la prochaine page    
        next_page_token = rslts_reviews["serpapi_pagination"]["next_page_token"]
        # Arrêter le loop s'il n'y en a plus
        if not next_page_token:
            break
    # Ajouter au résultat final
    reviews_by_place[place] = monument_reviews

# Sauvegarder les reviews dans un JSON
with open("reviews_test.json", "w", encoding="utf-8") as outfile:
    json.dump(reviews_by_place, outfile, ensure_ascii=False)

# Sauvegarder les reviewers dans un JSON
with open("reviewers_test.json", "w") as outfile: 
    json.dump(reviewers, outfile)
