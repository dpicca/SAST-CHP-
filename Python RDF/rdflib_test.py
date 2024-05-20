import json
from rdflib import Graph, Literal, RDF, URIRef, Namespace
from rdflib.namespace import OWL, RDFS, XSD

# Json Provisoire pour des tests
# place_data = {
#     "Tour Eiffel": {
#         "name": "Eiffel Tower", 
#         "place_id": "ChIJLU7jZClu5kcR4PcOOO6p3I0", 
#         "description": "Landmark 330m-high 19th-century tower. Gustave Eiffel's iconic, wrought-iron 1889 tower, with steps and elevators to observation decks.", 
#         "latitude": 48.85837, 
#         "longitude": 2.29448, 
#         "rating": 4.7, 
#         "num_reviews": 394895, 
#         "adresse": "Av. Gustave Eiffel, 75007 Paris, France", 
#         "country_iso": "FR"
#     },
#     "Colisee": {
#         "name": "Colosseum", 
#         "place_id": "ChIJrRMgU7ZhLxMRxAOFkC7I8Sg", 
#         "description": "Monumental 3-tiered Roman amphitheater once used for gladiatorial games, with guided tour option.", 
#         "latitude": 41.89021, 
#         "longitude": 12.49223, 
#         "rating": 4.7, 
#         "num_reviews": 397388, 
#         "adresse": "Piazza del Colosseo, 1, 00184 Roma RM, Italy", 
#         "country_iso": "IT"
#     },
#     "Acropole": {
#         "name": "Acropolis of Athens", 
#         "place_id": "ChIJ86z1Nxi9oRQR9g3r9ULAl1w", 
#         "description": "Ruins of iconic 5th-century B.C. temple complex on Athens' rocky hilltop undergoing restoration.", 
#         "latitude": 37.97153, 
#         "longitude": 23.72575, 
#         "rating": 4.8, 
#         "num_reviews": 121721, 
#         "adresse": "Athens 105 58, Greece", 
#         "country_iso": "GR"
#     }
# }

# Load Json results
with open('Gmaps_api/places_test.json', encoding='utf8') as f:
    place_data = json.load(f)

# Load Ontology
g = Graph()
g.parse('Ontology/ontologie_empath.rdf', format='xml')

namespace = 'http://www.semanticweb.org/wimve/ontologies/2024/3/ontology_empath#'
NS = Namespace(namespace)
g.bind('base', NS)
g.bind('owl', OWL)

# # Load the ontology
# ontology_uri = URIRef(namespace)
# g.add((ontology_uri, RDF.type, OWL.Ontology))

for key,items in place_data.items():
    
    cultural_element = URIRef(namespace + key.replace(' ', '_'))
    g.add((cultural_element, RDF.type, NS.CulturalElement))
    g.add((cultural_element, NS.hasCulturalElementID, Literal(items['place_id'], datatype=XSD.string)))
    g.add((cultural_element, NS.hasCulturalElementName, Literal(items['name'], datatype=XSD.string)))
    g.add((cultural_element, NS.hasCulturalElementRating, Literal(items['rating'], datatype=XSD.float)))
    g.add((cultural_element, NS.hasNumberOfReviews, Literal(items['num_reviews'], datatype=XSD.integer)))
    #hasCulturalElementType ?
    
    location = URIRef(namespace +items['place_id'])
    g.add((location, RDF.type, NS.GeographicLocation))
    g.add((location, NS.hasLocationLatitude, Literal(items['latitude'], datatype=XSD.float)))
    g.add((location, NS.hasLocationLongitude, Literal(items['longitude'], datatype=XSD.float)))
    g.add((location, NS.hasLocationAddress, Literal(items['adresse'], datatype=XSD.string)))
    g.add((location, NS.hasCountryISO, Literal(items['country_iso'], datatype=XSD.string)))
    
    g.add((cultural_element, NS.hasLocation, location))
    g.add((location, NS.isLocationOf, cultural_element))

g.serialize('Ontology/ontology_from_python.rdf', format='xml')
print(g.serialize(format='xml'))