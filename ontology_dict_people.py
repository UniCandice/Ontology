# -*- coding: utf-8 -*-
"""
Created on Fri Oct 25 21:08:29 2024

@author: Liyuan.Liu
"""

from csv import DictReader
from rdflib import Graph, URIRef, Literal, Namespace, XSD
from iribaker import to_iri

# Define namespaces
data_ns = 'http://data.example.org/resource/'
vocab_ns = 'http://data.example.org/vocab/'
DATA = Namespace(data_ns)
VOCAB = Namespace(vocab_ns)

# Initialize RDF graph and bind namespaces
graph = Graph()
graph.bind('data', DATA)
graph.bind('vocab', VOCAB)

# Load CSV data
filename = "example.csv"
with open(filename, 'r', encoding='utf-8') as csvfile:
    csv_contents = [{k: v for k, v in row.items()}
                    for row in DictReader(csvfile, skipinitialspace=True, delimiter=';')]

# Add triples to the graph based on CSV data
for row in csv_contents:
    person = URIRef(to_iri(data_ns + row['Name']))
    graph.add((person, VOCAB['name'], Literal(row['Name'], datatype=XSD.string)))
    graph.add((person, VOCAB['age'], Literal(int(row['Age']), datatype=XSD.integer)))
    graph.add((person, VOCAB['country'], URIRef(to_iri(data_ns + row['Country']))))
    graph.add((person, VOCAB['favouriteColour'], URIRef(to_iri(data_ns + row['Favourite Colour']))))
    graph.add((person, VOCAB['place'], URIRef(to_iri(data_ns + row['Place']))))
    graph.add((person, VOCAB['address'], Literal(row['Address'], datatype=XSD.string)))
    graph.add((person, VOCAB['hobby'], URIRef(to_iri(data_ns + row['Hobby']))))

# Save graph to Turtle format
ttl_file = 'people_data_1000.owl'
with open(ttl_file, 'w', encoding='utf-8') as f:
    f.write(graph.serialize(format='turtle'))
print(f"RDF data saved as {ttl_file}")


from rdflib import Graph
from rdflib.namespace import Namespace
import pandas as pd

# Define namespaces
data_ns = 'http://data.example.org/resource/'
vocab_ns = 'http://data.example.org/vocab/'
DATA = Namespace(data_ns)
VOCAB = Namespace(vocab_ns)

# Initialize RDF graph and load data from .ttl file
graph = Graph()
graph.parse("people_data_1000.owl", format="turtle")

# SPARQL query to select people and their age
query = """
PREFIX vocab: <http://data.example.org/vocab/>
SELECT ?name ?age
WHERE {
    ?person vocab:name ?name .
    ?person vocab:age ?age .
}
"""

# Execute the query and convert results to DataFrame
results = []
for row in graph.query(query):
    results.append((str(row.name), int(row.age)))

df = pd.DataFrame(results, columns=['Name', 'Age'])

# Display the DataFrame
print(df)

