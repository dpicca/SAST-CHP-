# Nécessite python 3.7(.16)
from serpapi import GoogleSearch

# Effectuer une recherche sur un lieu précis
params = {
  "engine": "google_maps",
  "type": "search",
  "q": "Coliseum", # query
  "ll": "@40.7455096,-74.0083012,14z", # lat, long, zoom
  "google_domain": "google.com",
  "hl": "en",
  "api_key": "cle_api" # cle api
}

search = GoogleSearch(params) # Effectuer la recherche
results = search.get_dict()


# Récupération des reviews à l'aide d'un place_id
reviews_colisee = {
  "engine": "google_maps_reviews",
  "hl": "en",
  "place_id": "ChIJrRMgU7ZhLxMRxAOFkC7I8Sg",
  "api_key": "cle_api"
}

search_reviews_colisee = GoogleSearch(reviews_colisee)
results_reviews_colisee = search_reviews_colisee.get_dict()