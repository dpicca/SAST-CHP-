import json
from rdflib import Graph, Literal, RDF, URIRef, Namespace
from rdflib.namespace import OWL, XSD

# Load Json results
with open('Gmaps_api/places_test.json', encoding='utf8') as f:
    place_data = json.load(f)

# Load Ontology
ontology_path = 'Ontology/ontologie_empath.rdf'
g = Graph()
g.parse(ontology_path, format='xml')

# Define the namespace
namespace = 'http://www.semanticweb.org/wimve/ontologies/2024/3/ontology_empath#'
NS = Namespace(namespace)
g.bind('base', NS)
g.bind('owl', OWL)

# create triples from Gmaps data
for key,items in place_data.items():
    
    cultural_element = URIRef(namespace+key.replace(' ', '_')+'_'+items['place_id'])
    g.add((cultural_element, RDF.type, NS.CulturalElement))
    g.add((cultural_element, NS.hasCulturalElementID, Literal(items['place_id'], datatype=XSD.string)))
    g.add((cultural_element, NS.hasCulturalElementName, Literal(items['name'], datatype=XSD.string)))
    g.add((cultural_element, NS.hasCulturalElementRating, Literal(items['rating'], datatype=XSD.float)))
    g.add((cultural_element, NS.hasNumberOfReviews, Literal(items['num_reviews'], datatype=XSD.integer)))
    for type in items['type_ids']:
        g.add((cultural_element, NS.hasCulturalElementType, Literal(type))) 
    
    location = URIRef(namespace+'Loc_of_'+items['place_id'])
    g.add((location, RDF.type, NS.GeographicLocation))
    g.add((location, NS.hasLocationLatitude, Literal(items['latitude'], datatype=XSD.float)))
    g.add((location, NS.hasLocationLongitude, Literal(items['longitude'], datatype=XSD.float)))
    g.add((location, NS.hasLocationAddress, Literal(items['adresse'], datatype=XSD.string)))
    g.add((location, NS.hasCountryISO, Literal(items['country_iso'], datatype=XSD.string)))
    
    g.add((cultural_element, NS.hasLocation, location))
    g.add((location, NS.isLocationOf, cultural_element))

g.serialize('Ontology/ontology_from_python.rdf', format='xml')
# print(g.serialize(format='xml'))