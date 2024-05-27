"""
Populates the EMPATH OWL ontology with de data recovered from the serpAPI and
the Sentiment Analysis.
"""

#Packages importaion
import json
import re
from rdflib import Graph, Literal, RDF, URIRef, Namespace
from rdflib.namespace import OWL, RDFS, XSD

# Load Json results of the Gmaps infos
with open('Gmaps_api/outputs/places.json', encoding='utf-8') as f:
    place_data = json.load(f)

# Load Json results of the sentiment analysis
with open('SentimentAnalysis/placeholder_sentiment_analysis_data.json',
          encoding='utf-8') as f:
    sentiment_data = json.load(f)

# Load Ontology
ONTOLOGY_PATH = 'Ontology/ontologie_empath.rdf'
g = Graph()
g.parse(ONTOLOGY_PATH, format='xml')

# Define the namespace
NAMESPACE = 'http://www.semanticweb.org/wimve/ontologies/2024/3/ontology_empath#'
NS = Namespace(NAMESPACE)
g.bind('base', NS)
g.bind('owl', OWL)

# create triples fromGmaps data
# works like this => g.add(subject, predicate, object)
for key,items in place_data.items():

    # Recode the name of the cultural element
    element_name = re.sub(r'\s+|\'|-','_',items['name'])

    # Define CulturalElement URI, Class and Label of CulturalElement
    cultural_element = URIRef(NAMESPACE+'CulturalElement_'+items['place_id'])
    g.add((cultural_element, RDF.type, NS.CulturalElement))
    g.add((cultural_element, RDFS.label, Literal(element_name)))

    # Triples from DataProperties with CulturalElement as Domain
    g.add((cultural_element, NS.CulturalElementGmapsID,
           Literal(items['place_id'], datatype=XSD.string)))
    g.add((cultural_element, NS.hasCulturalElementName,
           Literal(items['name'], datatype=XSD.string)))
    g.add((cultural_element, NS.hasCulturalElementRating,
           Literal(items['rating'], datatype=XSD.float)))
    g.add((cultural_element, NS.hasNumberOfReviews,
           Literal(items['num_reviews'], datatype=XSD.integer)))
    for elem_type in items['type_ids']:
        g.add((cultural_element, NS.hasCulturalElementType,
               Literal(elem_type, datatype=XSD.string)))

    # Define Location URI, Class and Label of Location
    location = URIRef(NAMESPACE+'LocationOf_'+items['place_id'])
    g.add((location, RDF.type, NS.GeographicLocation))
    g.add((location, RDFS.label, Literal(element_name+'_Location')))

    # Triples from DataProperties with Location as Domain
    g.add((location, NS.hasLocationLatitude,
           Literal(items['latitude'], datatype=XSD.float)))
    g.add((location, NS.hasLocationLongitude,
           Literal(items['longitude'], datatype=XSD.float)))
    g.add((location, NS.hasLocationAddress,
           Literal(items['adresse'], datatype=XSD.string)))
    g.add((location, NS.hasCountryISO,
           Literal(items['country_iso'], datatype=XSD.string)))

    # Triples from ObjectProperties between CulturalElement and Location
    g.add((cultural_element, NS.hasLocation, location))
    g.add((location, NS.isLocationOf, cultural_element))

    # Define Location URI, Class and Label of WikipediaPage
    wiki_page = URIRef(NAMESPACE+'Wikipedia_Of_'+items['place_id'])
    g.add((wiki_page, RDF.type, NS.WikipediaPage))
    g.add((wiki_page, RDFS.label, Literal(element_name+'_Wiki')))

    # Triples from DataProperties with WikipediaPage as Domain
    g.add((wiki_page, NS.hasWikipediaPageUrl,
           Literal(items['wiki_url'], datatype=XSD.anyURI)))
    g.add((wiki_page, NS.hasWikipediaPageTitle,
           Literal(items['wiki_title'], datatype=XSD.string)))

    # Triples from ObjectProperties between CulturalElement and WikipwdiaPage
    g.add((cultural_element, NS.hasWikipediaPage, wiki_page))
    g.add((wiki_page, NS.isWikipediaPageOf, cultural_element))

    # Check if the CulturalElement has a sentiment analysis
    if key in sentiment_data:
        for sentiment_review, items in sentiment_data[key].items():

            # Define Review URI, Class
            review = URIRef(NAMESPACE+element_name+'_'+sentiment_review)
            g.add((review, RDF.type, NS.Review))

            # Triples from DataProperties with Review as Domain
            g.add((review, NS.hasReviewIntensityIndexOrdinalClassification,
                   Literal(items['v_oc'], datatype=XSD.string)))
            g.add((review, NS.hasReviewIntensityIndexRegression,
                   Literal(items['v_reg'], datatype=XSD.float)))
            # g.add((review, NS.hasReviewRating, Literal(items['rating'], datatype=XSD.float)))

            # Dict of each sentiment and it's assossiated Class
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

            # Converts the list of dicts of the json file into one dict
            merged_oc = {k: v for d in items['ei_oc'] for k, v in d.items()}
            merged_reg = {k: v for d in items['ei_reg'] for k, v in d.items()}

            for sentiment_type in items['e_c']:

                # Define Sentiment URI, Class (done with sentiment_dict)
                sentiment = URIRef(NAMESPACE+element_name+'_'+sentiment_review+'_'+sentiment_type)
                g.add((sentiment, RDF.type, sentiment_dict[sentiment_type]))

                # Triples from ObjectProperties between Sentiment and Review
                g.add((review, NS.hasSentiment, sentiment))
                g.add((sentiment, NS.isSentimentOf, review))

                # Checks if it's a "main sentiment"
                if sentiment_type in ('joy', 'anger', 'fear', 'sadness'):

                    # Triples from DataProperties with Sentiment as Domain
                    g.add((sentiment,
                           NS.hasSentimentIntensityIndexOrdinalClassification,
                           Literal(merged_oc[sentiment_type],
                                   datatype=XSD.string)))
                    g.add((sentiment, NS.hasSentimentIntensityIndexRegression,
                           Literal(merged_reg[sentiment_type],
                                   datatype=XSD.float)))

            # Triples from ObjectProperties between CulturalElement and Review
            g.add((review, NS.isReviewOf, cultural_element))
            g.add((cultural_element, NS.hasReview, review))

# Saves the new populated ontology
g.serialize('Ontology/populated_ontology.rdf', format='xml', encoding='utf-8')
print(g.serialize(format='xml'))
