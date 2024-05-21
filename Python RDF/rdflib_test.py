import json
import re
from rdflib import Graph, Literal, RDF, URIRef, Namespace
from rdflib.namespace import OWL, RDFS, XSD

# Load Json results
with open('Gmaps_api/places_test.json', encoding='utf-8') as f:
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
    
    cultural_element = URIRef(namespace+'CulturalElement_'+items['place_id'])
    g.add((cultural_element, RDF.type, NS.CulturalElement))
    g.add((cultural_element, RDFS.label, Literal(re.sub('\s+|\'|-','_',items['name']))))
    g.add((cultural_element, NS.CulturalElementGmapsID, Literal(items['place_id'], datatype=XSD.string)))
    g.add((cultural_element, NS.hasCulturalElementName, Literal(items['name'], datatype=XSD.string)))
    g.add((cultural_element, NS.hasCulturalElementRating, Literal(items['rating'], datatype=XSD.float)))
    g.add((cultural_element, NS.hasNumberOfReviews, Literal(items['num_reviews'], datatype=XSD.integer)))
    for type in items['type_ids']:
        g.add((cultural_element, NS.hasCulturalElementType, Literal(type, datatype=XSD.string))) 
    
    location = URIRef(namespace+'LocationOf_'+items['place_id'])
    g.add((location, RDF.type, NS.GeographicLocation))
    g.add((location, RDFS.label, Literal(re.sub('\s+|\'|-','_',items['name']+'_Location'))))
    g.add((location, NS.hasLocationLatitude, Literal(items['latitude'], datatype=XSD.float)))
    g.add((location, NS.hasLocationLongitude, Literal(items['longitude'], datatype=XSD.float)))
    g.add((location, NS.hasLocationAddress, Literal(items['adresse'], datatype=XSD.string)))
    g.add((location, NS.hasCountryISO, Literal(items['country_iso'], datatype=XSD.string)))
    
    g.add((cultural_element, NS.hasLocation, location))
    g.add((location, NS.isLocationOf, cultural_element))

g.serialize('Ontology/ontology_from_python.rdf', format='xml', encoding='utf-8')
print(g.serialize(format='xml'))