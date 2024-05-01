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