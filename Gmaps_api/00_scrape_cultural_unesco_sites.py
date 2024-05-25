"""
Essais pour avoir une liste de lieux culturels / patrimoniaux
basée sur l'UNESCO.

Extrait les informations relatives aux lieux contenus dans la liste
des sites de l'UNESCO. Récupère le nom, la description, les coordonnées
(lat et long), la region, le pays, et le caractère transnational liés
aux lieux culturels.

Le résultat est exporté dans un fichier cultural_places_v1.json

N'a pas été utilisé car la majorité des lieux n'a pas de 
correspondance ponctuelle dans Google Maps.
"""

import xml.etree.ElementTree as ET
import json
import requests

# La liste des sites de l'UNESCO est dispo en XML en ligne (en plusieurs langues)
response = requests.get("https://whc.unesco.org/en/list/xml", timeout=5000)
xml_data = response.text

# Extraire le XML
root = ET.fromstring(xml_data)

# Initialiser la liste pour les lieux
cultural_places = []

# Itérer sur les lignes/rows du XML
for row in root.findall('row'):
    # Récupérer la catégorie (culturel, naturel, mixte)
    category = row.find('category').text
    # Pour l'instant, limiter aux lieux culturels
    if category == 'Cultural':
        cultural_place = {}
        cultural_place['name'] = row.find('site').text
        latitude = row.find('latitude').text
        longitude = row.find('longitude').text
        # Évite un problème si les coordonnées sont manquantes
        if latitude is not None and longitude is not None:
            cultural_place['latitude'] = float(latitude)
            cultural_place['longitude'] = float(longitude)
        else:
            # Manque des coordonnées pour les sites funéraires de la 1è GM
            print("Coords manquantes : ", cultural_place['name'])
            continue

        cultural_place['description'] = row.find('short_description').text.strip()
        cultural_place['region'] = row.find('region').text
        cultural_place['transborder'] = bool(int(row.find('transboundary').text))
        # Récupère le(s) pays
        cultural_place['states'] = [state.strip() for state in row.find('states').text.split(',')]
        # Ajouter aux lieux culturels
        cultural_places.append(cultural_place)


# Écrire un json avec les lieux
with open('cultural_places_v1.json', 'w', encoding="utf-8") as f:
    json.dump(cultural_places, f)
