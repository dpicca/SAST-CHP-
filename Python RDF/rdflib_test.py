import json
import re
from rdflib import Graph, Literal, RDF, URIRef, Namespace
from rdflib.namespace import OWL, RDFS, XSD

# Load Json results
with open('Gmaps_api/places_test.json', encoding='utf-8') as f:
    place_data = json.load(f)

with open('SentimentAnalysis/placeholder_sentiment_analysis_data.json', encoding='utf-8') as f:
    sentiment_data = json.load(f)

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
    element_name = re.sub('\s+|\'|-','_',items['name'])
    
    cultural_element = URIRef(namespace+'CulturalElement_'+items['place_id'])
    g.add((cultural_element, RDF.type, NS.CulturalElement))
    g.add((cultural_element, RDFS.label, Literal(element_name)))
    g.add((cultural_element, NS.CulturalElementGmapsID, Literal(items['place_id'], datatype=XSD.string)))
    g.add((cultural_element, NS.hasCulturalElementName, Literal(items['name'], datatype=XSD.string)))
    g.add((cultural_element, NS.hasCulturalElementRating, Literal(items['rating'], datatype=XSD.float)))
    g.add((cultural_element, NS.hasNumberOfReviews, Literal(items['num_reviews'], datatype=XSD.integer)))
    for t in items['type_ids']:
        g.add((cultural_element, NS.hasCulturalElementType, Literal(t, datatype=XSD.string))) 
    
    location = URIRef(namespace+'LocationOf_'+items['place_id'])
    g.add((location, RDF.type, NS.GeographicLocation))
    g.add((location, RDFS.label, Literal(re.sub('\s+|\'|-','_',items['name']+'_Location'))))
    g.add((location, NS.hasLocationLatitude, Literal(items['latitude'], datatype=XSD.float)))
    g.add((location, NS.hasLocationLongitude, Literal(items['longitude'], datatype=XSD.float)))
    g.add((location, NS.hasLocationAddress, Literal(items['adresse'], datatype=XSD.string)))
    g.add((location, NS.hasCountryISO, Literal(items['country_iso'], datatype=XSD.string)))

    g.add((cultural_element, NS.hasLocation, location))
    g.add((location, NS.isLocationOf, cultural_element))
    
    if key in sentiment_data:
        for sentiment, items in sentiment_data[key].items():

            review = URIRef(namespace+element_name+'_'+sentiment)
            g.add((review, RDF.type, NS.Review))
            # g.add((review, RDFS.label, Literal(sentiment)))
            g.add((review, NS.hasReviewIntensityIndexOrdinalClassification,
                   Literal(items['v_oc'], datatype=XSD.string))) #re.findall(r'^.+(?=:)',items['v_oc'])[0] si on veut un integer
            g.add((review, NS.hasReviewIntensityIndexRegression, Literal(items['v_reg'], datatype=XSD.float)))
            # g.add((review, NS.hasReviewRating, Literal(items['rating'], datatype=XSD.float)))

            sentiment_dict = {'anger':NS.AngerSentimentType,
                              'anticipation': NS.AnticipationSentimentType,
                              'disgust': NS.DisgustSentimentType,
                              'fear': NS.FearSentimentType,
                              'joy': NS.JoySentimentType,
                              'love': NS.LoveSentimentType,
                              'optimism': NS.OptimismSentimentType,
                              'pessimism': NS.PessimismSentimentType,
                              'sadness': NS.SadnessSentimentType,
                              'surprise': NS.SurpriseSentimentType,
                              'trust': NS.TrustSentimentType}
            
            merged_oc = {k: v for d in items['ei_oc'] for k, v in d.items()}
            merged_reg = {k: v for d in items['ei_reg'] for k, v in d.items()}
            
            
            for sentiment_type in items['e_c']:

                sentiment = URIRef(namespace+element_name+'_'+'sentiment_type_'+sentiment_type)
                g.add((sentiment, RDF.type, sentiment_dict[sentiment_type]))
                g.add((review, NS.hasSentiment, sentiment))
                g.add((sentiment, NS.isSentimentOf, review))

                if sentiment_type in ('joy', 'anger', 'fear', 'sadness'):
                    
                    g.add((sentiment, NS.hasSentimentIntensityIndexOrdinalClassification, Literal(merged_oc[sentiment_type], datatype=XSD.string)))
                    g.add((sentiment, NS.hasSentimentIntensityIndexRegression, Literal(merged_reg[sentiment_type], datatype=XSD.float)))                
            
            g.add((review, NS.isReviewOf, cultural_element))
            g.add((cultural_element, NS.hasReview, review))

g.serialize('Ontology/ontology_from_python.rdf', format='xml', encoding='utf-8')
# print(g.serialize(format='xml'))