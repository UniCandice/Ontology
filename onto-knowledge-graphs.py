# -*- coding: utf-8 -*-
"""
Created on Sat Feb 22 20:18:40 2025

@author: Liyuan.Liu
"""

from rdflib import Graph, Namespace, RDF, RDFS, OWL, Literal

# Create the RDF graph
g = Graph()

# Define a custom namespace for our battery ontology
BAT = Namespace("http://example.org/battery#")
g.bind("bat", BAT)

# Define main classes in our ontology
classes = ["Battery", "MaterialComponent", "Formulation", "Coating", "Testing"]
for cls in classes:
    g.add((BAT[cls], RDF.type, OWL.Class))
    g.add((BAT[cls], RDFS.label, Literal(cls)))

# Define subclasses for MaterialComponent
subcomponents = ["Anode", "Cathode", "Electrolyte", "Separator"]
for sub in subcomponents:
    g.add((BAT[sub], RDF.type, OWL.Class))
    g.add((BAT[sub], RDFS.subClassOf, BAT["MaterialComponent"]))
    g.add((BAT[sub], RDFS.label, Literal(sub)))

# Define object properties linking Battery to its related aspects
properties = {
    "hasComponent": (BAT.Battery, BAT.MaterialComponent),
    "hasFormulation": (BAT.Battery, BAT.Formulation),
    "hasCoating": (BAT.Battery, BAT.Coating),
    "hasTesting": (BAT.Battery, BAT.Testing)
}

for prop, (domain, range_) in properties.items():
    prop_uri = BAT[prop]
    g.add((prop_uri, RDF.type, OWL.ObjectProperty))
    g.add((prop_uri, RDFS.domain, domain))
    g.add((prop_uri, RDFS.range, range_))
    g.add((prop_uri, RDFS.label, Literal(prop)))

# ----------------------------
# Create Instances for Battery001: High Energy Battery
battery1 = BAT["Battery001"]
g.add((battery1, RDF.type, BAT.Battery))
g.add((battery1, RDFS.label, Literal("High Energy Battery")))

# Material Component: Lithium Anode (instance of Anode)
anode1 = BAT["Anode_Lithium"]
g.add((anode1, RDF.type, BAT.Anode))
g.add((anode1, RDFS.label, Literal("Lithium Anode")))
g.add((battery1, BAT.hasComponent, anode1))

# Formulation
formulation1 = BAT["Formulation001"]
g.add((formulation1, RDF.type, BAT.Formulation))
g.add((formulation1, RDFS.label, Literal("Standard Formulation")))
g.add((battery1, BAT.hasFormulation, formulation1))

# Coating
coating1 = BAT["Coating001"]
g.add((coating1, RDF.type, BAT.Coating))
g.add((coating1, RDFS.label, Literal("Protective Coating")))
g.add((battery1, BAT.hasCoating, coating1))

# Testing Protocol
testing1 = BAT["Testing001"]
g.add((testing1, RDF.type, BAT.Testing))
g.add((testing1, RDFS.label, Literal("Cycle Life Test")))
g.add((battery1, BAT.hasTesting, testing1))

# ----------------------------
# Create Instances for Battery002: Fast Charge Battery
battery2 = BAT["Battery002"]
g.add((battery2, RDF.type, BAT.Battery))
g.add((battery2, RDFS.label, Literal("Fast Charge Battery")))

# Material Components for Battery002:
# Graphite Anode
anode2 = BAT["Anode_Graphite"]
g.add((anode2, RDF.type, BAT.Anode))
g.add((anode2, RDFS.label, Literal("Graphite Anode")))
g.add((battery2, BAT.hasComponent, anode2))

# Lithium Cobalt Oxide Cathode
cathode2 = BAT["Cathode_LCO"]
g.add((cathode2, RDF.type, BAT.Cathode))
g.add((cathode2, RDFS.label, Literal("Lithium Cobalt Oxide Cathode")))
g.add((battery2, BAT.hasComponent, cathode2))

# Liquid Electrolyte
electrolyte2 = BAT["Electrolyte_Liquid"]
g.add((electrolyte2, RDF.type, BAT.Electrolyte))
g.add((electrolyte2, RDFS.label, Literal("Liquid Electrolyte")))
g.add((battery2, BAT.hasComponent, electrolyte2))

# Polymer Separator
separator2 = BAT["Separator_Polymer"]
g.add((separator2, RDF.type, BAT.Separator))
g.add((separator2, RDFS.label, Literal("Polymer Separator")))
g.add((battery2, BAT.hasComponent, separator2))

# Formulation
formulation2 = BAT["Formulation002"]
g.add((formulation2, RDF.type, BAT.Formulation))
g.add((formulation2, RDFS.label, Literal("Fast Charge Formulation")))
g.add((battery2, BAT.hasFormulation, formulation2))

# Coating
coating2 = BAT["Coating002"]
g.add((coating2, RDF.type, BAT.Coating))
g.add((coating2, RDFS.label, Literal("Conductive Coating")))
g.add((battery2, BAT.hasCoating, coating2))

# Testing Protocol
testing2 = BAT["Testing002"]
g.add((testing2, RDF.type, BAT.Testing))
g.add((testing2, RDFS.label, Literal("High Current Test")))
g.add((battery2, BAT.hasTesting, testing2))

# ----------------------------
# Create Instances for Battery003: Long-life Battery
battery3 = BAT["Battery003"]
g.add((battery3, RDF.type, BAT.Battery))
g.add((battery3, RDFS.label, Literal("Long-life Battery")))

# Material Components for Battery003:
# Silicon Anode
anode3 = BAT["Anode_Silicon"]
g.add((anode3, RDF.type, BAT.Anode))
g.add((anode3, RDFS.label, Literal("Silicon Anode")))
g.add((battery3, BAT.hasComponent, anode3))

# Nickel Manganese Cobalt Oxide Cathode
cathode3 = BAT["Cathode_NMC"]
g.add((cathode3, RDF.type, BAT.Cathode))
g.add((cathode3, RDFS.label, Literal("Nickel Manganese Cobalt Oxide Cathode")))
g.add((battery3, BAT.hasComponent, cathode3))

# Solid Electrolyte
electrolyte3 = BAT["Electrolyte_Solid"]
g.add((electrolyte3, RDF.type, BAT.Electrolyte))
g.add((electrolyte3, RDFS.label, Literal("Solid Electrolyte")))
g.add((battery3, BAT.hasComponent, electrolyte3))

# Ceramic Separator
separator3 = BAT["Separator_Ceramic"]
g.add((separator3, RDF.type, BAT.Separator))
g.add((separator3, RDFS.label, Literal("Ceramic Separator")))
g.add((battery3, BAT.hasComponent, separator3))

# Formulation
formulation3 = BAT["Formulation003"]
g.add((formulation3, RDF.type, BAT.Formulation))
g.add((formulation3, RDFS.label, Literal("Long-life Formulation")))
g.add((battery3, BAT.hasFormulation, formulation3))

# Coating
coating3 = BAT["Coating003"]
g.add((coating3, RDF.type, BAT.Coating))
g.add((coating3, RDFS.label, Literal("Durable Coating")))
g.add((battery3, BAT.hasCoating, coating3))

# Testing Protocol
testing3 = BAT["Testing003"]
g.add((testing3, RDF.type, BAT.Testing))
g.add((testing3, RDFS.label, Literal("Calendar Life Test")))
g.add((battery3, BAT.hasTesting, testing3))

# ----------------------------
# Serialize the graph to RDF/XML format (suitable for OWL ontologies)
owl_data = g.serialize(format="xml")

# Save the serialized data as an OWL file
with open("battery_ontology.owl", "w", encoding="utf-8") as f:
    f.write(owl_data)

# Optionally, print the serialized data
print(owl_data)

    
from rdflib import Graph, Namespace, RDF, RDFS, OWL, Literal

# Create the RDF graph
g = Graph()

# Define a custom namespace for our battery ontology
BAT = Namespace("http://example.org/battery#")
g.bind("bat", BAT)

# Define Battery as the root (father) class
g.add((BAT.Battery, RDF.type, OWL.Class))
g.add((BAT.Battery, RDFS.label, Literal("Battery")))

# Define other classes as subclasses of Battery
other_classes = ["MaterialComponent", "Formulation", "Coating", "Testing"]
for cls in other_classes:
    g.add((BAT[cls], RDF.type, OWL.Class))
    g.add((BAT[cls], RDFS.subClassOf, BAT.Battery))
    g.add((BAT[cls], RDFS.label, Literal(cls)))

# Define subclasses for MaterialComponent
subcomponents = ["Anode", "Cathode", "Electrolyte", "Separator"]
for sub in subcomponents:
    g.add((BAT[sub], RDF.type, OWL.Class))
    g.add((BAT[sub], RDFS.subClassOf, BAT.MaterialComponent))
    g.add((BAT[sub], RDFS.label, Literal(sub)))

# Define object properties linking Battery (as the root) to its aspects
properties = {
    "hasComponent": (BAT.Battery, BAT.MaterialComponent),
    "hasFormulation": (BAT.Battery, BAT.Formulation),
    "hasCoating": (BAT.Battery, BAT.Coating),
    "hasTesting": (BAT.Battery, BAT.Testing)
}

for prop, (domain, range_) in properties.items():
    prop_uri = BAT[prop]
    g.add((prop_uri, RDF.type, OWL.ObjectProperty))
    g.add((prop_uri, RDFS.domain, domain))
    g.add((prop_uri, RDFS.range, range_))
    g.add((prop_uri, RDFS.label, Literal(prop)))

# ----------------------------
# Create Instances for Battery001: High Energy Battery
battery1 = BAT["Battery001"]
g.add((battery1, RDF.type, BAT.Battery))
g.add((battery1, RDFS.label, Literal("High Energy Battery")))

# Material Component: Lithium Anode (instance of Anode)
anode1 = BAT["Anode_Lithium"]
g.add((anode1, RDF.type, BAT.Anode))
g.add((anode1, RDFS.label, Literal("Lithium Anode")))
g.add((battery1, BAT.hasComponent, anode1))

# Formulation
formulation1 = BAT["Formulation001"]
g.add((formulation1, RDF.type, BAT.Formulation))
g.add((formulation1, RDFS.label, Literal("Standard Formulation")))
g.add((battery1, BAT.hasFormulation, formulation1))

# Coating
coating1 = BAT["Coating001"]
g.add((coating1, RDF.type, BAT.Coating))
g.add((coating1, RDFS.label, Literal("Protective Coating")))
g.add((battery1, BAT.hasCoating, coating1))

# Testing Protocol
testing1 = BAT["Testing001"]
g.add((testing1, RDF.type, BAT.Testing))
g.add((testing1, RDFS.label, Literal("Cycle Life Test")))
g.add((battery1, BAT.hasTesting, testing1))

# ----------------------------
# You can add more battery instances similarly...

# Serialize the graph to RDF/XML (OWL-compatible format)
owl_data = g.serialize(format="xml")

# Save the ontology as an OWL file
with open("battery_ontology1.owl", "w", encoding="utf-8") as f:
    f.write(owl_data)

# Optionally, print the serialized data
print(owl_data)

from rdflib import Graph, Namespace, RDF, RDFS, OWL, Literal

# Create the RDF graph
g = Graph()

# Define a custom namespace for our battery ontology
BAT = Namespace("http://example.org/battery#")
g.bind("bat", BAT)

# ----------------------------
# Define the root class: Battery
g.add((BAT.Battery, RDF.type, OWL.Class))
g.add((BAT.Battery, RDFS.label, Literal("Battery")))

# Define other main classes as subclasses of Battery
main_classes = ["MaterialComponent", "Formulation", "Coating", "Testing"]
for cls in main_classes:
    g.add((BAT[cls], RDF.type, OWL.Class))
    g.add((BAT[cls], RDFS.subClassOf, BAT.Battery))
    g.add((BAT[cls], RDFS.label, Literal(cls)))

# Define a new class for formulation parameters
g.add((BAT.FormulationParameters, RDF.type, OWL.Class))
g.add((BAT.FormulationParameters, RDFS.label, Literal("FormulationParameters")))

# ----------------------------
# Define subclasses for MaterialComponent (e.g., Anode, Cathode, etc.)
subcomponents = ["Anode", "Cathode", "Electrolyte", "Separator"]
for sub in subcomponents:
    g.add((BAT[sub], RDF.type, OWL.Class))
    g.add((BAT[sub], RDFS.subClassOf, BAT.MaterialComponent))
    g.add((BAT[sub], RDFS.label, Literal(sub)))

# ----------------------------
# Define object properties linking Battery (root) to its aspects
properties = {
    "hasComponent": (BAT.Battery, BAT.MaterialComponent),
    "hasFormulation": (BAT.Battery, BAT.Formulation),
    "hasCoating": (BAT.Battery, BAT.Coating),
    "hasTesting": (BAT.Battery, BAT.Testing)
}
for prop, (domain, range_) in properties.items():
    prop_uri = BAT[prop]
    g.add((prop_uri, RDF.type, OWL.ObjectProperty))
    g.add((prop_uri, RDFS.domain, domain))
    g.add((prop_uri, RDFS.range, range_))
    g.add((prop_uri, RDFS.label, Literal(prop)))

# Define an object property to link a Formulation to its FormulationParameters
g.add((BAT.hasFormulationParameters, RDF.type, OWL.ObjectProperty))
g.add((BAT.hasFormulationParameters, RDFS.domain, BAT.Formulation))
g.add((BAT.hasFormulationParameters, RDFS.range, BAT.FormulationParameters))
g.add((BAT.hasFormulationParameters, RDFS.label, Literal("hasFormulationParameters")))

# ----------------------------
# Define data properties for each field in the formulation parameter set

# Solids content (%)
g.add((BAT.hasSolidsContent, RDF.type, OWL.DatatypeProperty))
g.add((BAT.hasSolidsContent, RDFS.domain, BAT.FormulationParameters))
g.add((BAT.hasSolidsContent, RDFS.label, Literal("hasSolidsContent")))

# Active Content (%)
g.add((BAT.hasActiveContent, RDF.type, OWL.DatatypeProperty))
g.add((BAT.hasActiveContent, RDFS.domain, BAT.FormulationParameters))
g.add((BAT.hasActiveContent, RDFS.label, Literal("hasActiveContent")))

# Conductive Content (%)
g.add((BAT.hasConductiveContent, RDF.type, OWL.DatatypeProperty))
g.add((BAT.hasConductiveContent, RDFS.domain, BAT.FormulationParameters))
g.add((BAT.hasConductiveContent, RDFS.label, Literal("hasConductiveContent")))

# Binder Content (%)
g.add((BAT.hasBinderContent, RDF.type, OWL.DatatypeProperty))
g.add((BAT.hasBinderContent, RDFS.domain, BAT.FormulationParameters))
g.add((BAT.hasBinderContent, RDFS.label, Literal("hasBinderContent")))

# Temperature
g.add((BAT.hasTemperature, RDF.type, OWL.DatatypeProperty))
g.add((BAT.hasTemperature, RDFS.domain, BAT.FormulationParameters))
g.add((BAT.hasTemperature, RDFS.label, Literal("hasTemperature")))

# Humidity
g.add((BAT.hasHumidity, RDF.type, OWL.DatatypeProperty))
g.add((BAT.hasHumidity, RDFS.domain, BAT.FormulationParameters))
g.add((BAT.hasHumidity, RDFS.label, Literal("hasHumidity")))

# ----------------------------
# Battery001: High Energy Battery
battery1 = BAT["Battery001"]
g.add((battery1, RDF.type, BAT.Battery))
g.add((battery1, RDFS.label, Literal("High Energy Battery")))

# Material Component: Lithium Anode (instance of Anode)
anode1 = BAT["Anode_Lithium"]
g.add((anode1, RDF.type, BAT.Anode))
g.add((anode1, RDFS.label, Literal("Lithium Anode")))
g.add((battery1, BAT.hasComponent, anode1))

# Formulation for Battery001
formulation1 = BAT["Formulation001"]
g.add((formulation1, RDF.type, BAT.Formulation))
g.add((formulation1, RDFS.label, Literal("Standard Formulation")))
g.add((battery1, BAT.hasFormulation, formulation1))

# Create formulation parameters instance for Battery001
formulationParams1 = BAT["FormulationParameters001"]
g.add((formulationParams1, RDF.type, BAT.FormulationParameters))
g.add((formulation1, BAT.hasFormulationParameters, formulationParams1))
g.add((formulationParams1, BAT.hasSolidsContent, Literal("50%")))
g.add((formulationParams1, BAT.hasActiveContent, Literal("80%")))
g.add((formulationParams1, BAT.hasConductiveContent, Literal("5%")))
g.add((formulationParams1, BAT.hasBinderContent, Literal("10%")))
g.add((formulationParams1, BAT.hasTemperature, Literal("27")))
g.add((formulationParams1, BAT.hasHumidity, Literal("20")))

# Coating for Battery001
coating1 = BAT["Coating001"]
g.add((coating1, RDF.type, BAT.Coating))
g.add((coating1, RDFS.label, Literal("Protective Coating")))
g.add((battery1, BAT.hasCoating, coating1))
g.add((coating1, BAT.hasCoatingParameter, Literal("thickness: 5 microns")))

# Testing Protocol for Battery001
testing1 = BAT["Testing001"]
g.add((testing1, RDF.type, BAT.Testing))
g.add((testing1, RDFS.label, Literal("Cycle Life Test")))
g.add((battery1, BAT.hasTesting, testing1))
g.add((testing1, BAT.hasTestingParameter, Literal("cycle life: 500 cycles")))

# ----------------------------
# Battery002: Fast Charge Battery
battery2 = BAT["Battery002"]
g.add((battery2, RDF.type, BAT.Battery))
g.add((battery2, RDFS.label, Literal("Fast Charge Battery")))

# Material Components for Battery002:
# Graphite Anode
anode2 = BAT["Anode_Graphite"]
g.add((anode2, RDF.type, BAT.Anode))
g.add((anode2, RDFS.label, Literal("Graphite Anode")))
g.add((battery2, BAT.hasComponent, anode2))

# Lithium Cobalt Oxide Cathode
cathode2 = BAT["Cathode_LCO"]
g.add((cathode2, RDF.type, BAT.Cathode))
g.add((cathode2, RDFS.label, Literal("Lithium Cobalt Oxide Cathode")))
g.add((battery2, BAT.hasComponent, cathode2))

# Liquid Electrolyte
electrolyte2 = BAT["Electrolyte_Liquid"]
g.add((electrolyte2, RDF.type, BAT.Electrolyte))
g.add((electrolyte2, RDFS.label, Literal("Liquid Electrolyte")))
g.add((battery2, BAT.hasComponent, electrolyte2))

# Polymer Separator
separator2 = BAT["Separator_Polymer"]
g.add((separator2, RDF.type, BAT.Separator))
g.add((separator2, RDFS.label, Literal("Polymer Separator")))
g.add((battery2, BAT.hasComponent, separator2))

# Formulation for Battery002
formulation2 = BAT["Formulation002"]
g.add((formulation2, RDF.type, BAT.Formulation))
g.add((formulation2, RDFS.label, Literal("Fast Charge Formulation")))
g.add((battery2, BAT.hasFormulation, formulation2))

# Create formulation parameters instance for Battery002
formulationParams2 = BAT["FormulationParameters002"]
g.add((formulationParams2, RDF.type, BAT.FormulationParameters))
g.add((formulation2, BAT.hasFormulationParameters, formulationParams2))
g.add((formulationParams2, BAT.hasSolidsContent, Literal("55%")))
g.add((formulationParams2, BAT.hasActiveContent, Literal("75%")))
g.add((formulationParams2, BAT.hasConductiveContent, Literal("7%")))
g.add((formulationParams2, BAT.hasBinderContent, Literal("8%")))
g.add((formulationParams2, BAT.hasTemperature, Literal("30")))
g.add((formulationParams2, BAT.hasHumidity, Literal("25")))

# Coating for Battery002
coating2 = BAT["Coating002"]
g.add((coating2, RDF.type, BAT.Coating))
g.add((coating2, RDFS.label, Literal("Conductive Coating")))
g.add((battery2, BAT.hasCoating, coating2))
g.add((coating2, BAT.hasCoatingParameter, Literal("thickness: 3 microns")))

# Testing Protocol for Battery002
testing2 = BAT["Testing002"]
g.add((testing2, RDF.type, BAT.Testing))
g.add((testing2, RDFS.label, Literal("High Current Test")))
g.add((battery2, BAT.hasTesting, testing2))
g.add((testing2, BAT.hasTestingParameter, Literal("current: 2C")))

# ----------------------------
# Battery003: Long-life Battery
battery3 = BAT["Battery003"]
g.add((battery3, RDF.type, BAT.Battery))
g.add((battery3, RDFS.label, Literal("Long-life Battery")))

# Material Components for Battery003:
# Silicon Anode
anode3 = BAT["Anode_Silicon"]
g.add((anode3, RDF.type, BAT.Anode))
g.add((anode3, RDFS.label, Literal("Silicon Anode")))
g.add((battery3, BAT.hasComponent, anode3))

# Nickel Manganese Cobalt Oxide Cathode
cathode3 = BAT["Cathode_NMC"]
g.add((cathode3, RDF.type, BAT.Cathode))
g.add((cathode3, RDFS.label, Literal("Nickel Manganese Cobalt Oxide Cathode")))
g.add((battery3, BAT.hasComponent, cathode3))

# Solid Electrolyte
electrolyte3 = BAT["Electrolyte_Solid"]
g.add((electrolyte3, RDF.type, BAT.Electrolyte))
g.add((electrolyte3, RDFS.label, Literal("Solid Electrolyte")))
g.add((battery3, BAT.hasComponent, electrolyte3))

# Ceramic Separator
separator3 = BAT["Separator_Ceramic"]
g.add((separator3, RDF.type, BAT.Separator))
g.add((separator3, RDFS.label, Literal("Ceramic Separator")))
g.add((battery3, BAT.hasComponent, separator3))

# Formulation for Battery003
formulation3 = BAT["Formulation003"]
g.add((formulation3, RDF.type, BAT.Formulation))
g.add((formulation3, RDFS.label, Literal("Long-life Formulation")))
g.add((battery3, BAT.hasFormulation, formulation3))

# Create formulation parameters instance for Battery003
formulationParams3 = BAT["FormulationParameters003"]
g.add((formulationParams3, RDF.type, BAT.FormulationParameters))
g.add((formulation3, BAT.hasFormulationParameters, formulationParams3))
g.add((formulationParams3, BAT.hasSolidsContent, Literal("60%")))
g.add((formulationParams3, BAT.hasActiveContent, Literal("85%")))
g.add((formulationParams3, BAT.hasConductiveContent, Literal("6%")))
g.add((formulationParams3, BAT.hasBinderContent, Literal("9%")))
g.add((formulationParams3, BAT.hasTemperature, Literal("25")))
g.add((formulationParams3, BAT.hasHumidity, Literal("18")))

# Coating for Battery003
coating3 = BAT["Coating003"]
g.add((coating3, RDF.type, BAT.Coating))
g.add((coating3, RDFS.label, Literal("Durable Coating")))
g.add((battery3, BAT.hasCoating, coating3))
g.add((coating3, BAT.hasCoatingParameter, Literal("thickness: 6 microns")))

# Testing Protocol for Battery003
testing3 = BAT["Testing003"]
g.add((testing3, RDF.type, BAT.Testing))
g.add((testing3, RDFS.label, Literal("Calendar Life Test")))
g.add((battery3, BAT.hasTesting, testing3))
g.add((testing3, BAT.hasTestingParameter, Literal("calendar life: 10 years")))

# ----------------------------
# Serialize the graph to RDF/XML (OWL-compatible format)
owl_data = g.serialize(format="xml")

# Save the ontology as an OWL file
with open("battery_ontology2.owl", "w", encoding="utf-8") as f:
    f.write(owl_data)

# Optionally, print the serialized OWL data
print(owl_data)


from rdflib import Graph, Namespace, RDF, RDFS, OWL, Literal

# Create the RDF graph
g = Graph()

# Define a custom namespace for our battery ontology
BAT = Namespace("http://example.org/battery#")
g.bind("bat", BAT)

# ----------------------------
# Define the root class: Battery
g.add((BAT.Battery, RDF.type, OWL.Class))
g.add((BAT.Battery, RDFS.label, Literal("Battery")))

# Define other main classes as subclasses of Battery
main_classes = ["MaterialComponent", "Formulation", "Coating", "Testing"]
for cls in main_classes:
    g.add((BAT[cls], RDF.type, OWL.Class))
    g.add((BAT[cls], RDFS.subClassOf, BAT.Battery))
    g.add((BAT[cls], RDFS.label, Literal(cls)))

# Define subclasses for MaterialComponent (e.g., Anode, Cathode, etc.)
subcomponents = ["Anode", "Cathode", "Electrolyte", "Separator"]
for sub in subcomponents:
    g.add((BAT[sub], RDF.type, OWL.Class))
    g.add((BAT[sub], RDFS.subClassOf, BAT.MaterialComponent))
    g.add((BAT[sub], RDFS.label, Literal(sub)))

# ----------------------------
# Define object properties linking Battery (root) to its aspects
object_props = {
    "hasComponent": (BAT.Battery, BAT.MaterialComponent),
    "hasFormulation": (BAT.Battery, BAT.Formulation),
    "hasCoating": (BAT.Battery, BAT.Coating),
    "hasTesting": (BAT.Battery, BAT.Testing)
}
for prop, (domain, range_) in object_props.items():
    prop_uri = BAT[prop]
    g.add((prop_uri, RDF.type, OWL.ObjectProperty))
    g.add((prop_uri, RDFS.domain, domain))
    g.add((prop_uri, RDFS.range, range_))
    g.add((prop_uri, RDFS.label, Literal(prop)))

# ----------------------------
# Define data properties for formulation parameters with domain: Formulation
g.add((BAT.hasSolidsContent, RDF.type, OWL.DatatypeProperty))
g.add((BAT.hasSolidsContent, RDFS.domain, BAT.Formulation))
g.add((BAT.hasSolidsContent, RDFS.label, Literal("hasSolidsContent")))

g.add((BAT.hasActiveContent, RDF.type, OWL.DatatypeProperty))
g.add((BAT.hasActiveContent, RDFS.domain, BAT.Formulation))
g.add((BAT.hasActiveContent, RDFS.label, Literal("hasActiveContent")))

g.add((BAT.hasConductiveContent, RDF.type, OWL.DatatypeProperty))
g.add((BAT.hasConductiveContent, RDFS.domain, BAT.Formulation))
g.add((BAT.hasConductiveContent, RDFS.label, Literal("hasConductiveContent")))

g.add((BAT.hasBinderContent, RDF.type, OWL.DatatypeProperty))
g.add((BAT.hasBinderContent, RDFS.domain, BAT.Formulation))
g.add((BAT.hasBinderContent, RDFS.label, Literal("hasBinderContent")))

g.add((BAT.hasTemperature, RDF.type, OWL.DatatypeProperty))
g.add((BAT.hasTemperature, RDFS.domain, BAT.Formulation))
g.add((BAT.hasTemperature, RDFS.label, Literal("hasTemperature")))

g.add((BAT.hasHumidity, RDF.type, OWL.DatatypeProperty))
g.add((BAT.hasHumidity, RDFS.domain, BAT.Formulation))
g.add((BAT.hasHumidity, RDFS.label, Literal("hasHumidity")))

# (Optional) Define data properties for coating and testing parameters with their respective domains
g.add((BAT.hasCoatingParameter, RDF.type, OWL.DatatypeProperty))
g.add((BAT.hasCoatingParameter, RDFS.domain, BAT.Coating))
g.add((BAT.hasCoatingParameter, RDFS.label, Literal("hasCoatingParameter")))

g.add((BAT.hasTestingParameter, RDF.type, OWL.DatatypeProperty))
g.add((BAT.hasTestingParameter, RDFS.domain, BAT.Testing))
g.add((BAT.hasTestingParameter, RDFS.label, Literal("hasTestingParameter")))

# ----------------------------
# Battery001: High Energy Battery
battery1 = BAT["Battery001"]
g.add((battery1, RDF.type, BAT.Battery))
g.add((battery1, RDFS.label, Literal("High Energy Battery")))

# Material Component: Lithium Anode (instance of Anode)
anode1 = BAT["Anode_Lithium"]
g.add((anode1, RDF.type, BAT.Anode))
g.add((anode1, RDFS.label, Literal("Lithium Anode")))
g.add((battery1, BAT.hasComponent, anode1))

# Formulation for Battery001 with formulation parameters directly
formulation1 = BAT["Formulation001"]
g.add((formulation1, RDF.type, BAT.Formulation))
g.add((formulation1, RDFS.label, Literal("Standard Formulation")))
g.add((battery1, BAT.hasFormulation, formulation1))
g.add((formulation1, BAT.hasSolidsContent, Literal("50%")))
g.add((formulation1, BAT.hasActiveContent, Literal("80%")))
g.add((formulation1, BAT.hasConductiveContent, Literal("5%")))
g.add((formulation1, BAT.hasBinderContent, Literal("10%")))
g.add((formulation1, BAT.hasTemperature, Literal("27")))
g.add((formulation1, BAT.hasHumidity, Literal("20")))

# Coating for Battery001
coating1 = BAT["Coating001"]
g.add((coating1, RDF.type, BAT.Coating))
g.add((coating1, RDFS.label, Literal("Protective Coating")))
g.add((battery1, BAT.hasCoating, coating1))
g.add((coating1, BAT.hasCoatingParameter, Literal("thickness: 5 microns")))

# Testing Protocol for Battery001
testing1 = BAT["Testing001"]
g.add((testing1, RDF.type, BAT.Testing))
g.add((testing1, RDFS.label, Literal("Cycle Life Test")))
g.add((battery1, BAT.hasTesting, testing1))
g.add((testing1, BAT.hasTestingParameter, Literal("cycle life: 500 cycles")))

# ----------------------------
# Battery002: Fast Charge Battery
battery2 = BAT["Battery002"]
g.add((battery2, RDF.type, BAT.Battery))
g.add((battery2, RDFS.label, Literal("Fast Charge Battery")))

# Material Components for Battery002
anode2 = BAT["Anode_Graphite"]
g.add((anode2, RDF.type, BAT.Anode))
g.add((anode2, RDFS.label, Literal("Graphite Anode")))
g.add((battery2, BAT.hasComponent, anode2))

cathode2 = BAT["Cathode_LCO"]
g.add((cathode2, RDF.type, BAT.Cathode))
g.add((cathode2, RDFS.label, Literal("Lithium Cobalt Oxide Cathode")))
g.add((battery2, BAT.hasComponent, cathode2))

electrolyte2 = BAT["Electrolyte_Liquid"]
g.add((electrolyte2, RDF.type, BAT.Electrolyte))
g.add((electrolyte2, RDFS.label, Literal("Liquid Electrolyte")))
g.add((battery2, BAT.hasComponent, electrolyte2))

separator2 = BAT["Separator_Polymer"]
g.add((separator2, RDF.type, BAT.Separator))
g.add((separator2, RDFS.label, Literal("Polymer Separator")))
g.add((battery2, BAT.hasComponent, separator2))

# Formulation for Battery002 with its own parameter values
formulation2 = BAT["Formulation002"]
g.add((formulation2, RDF.type, BAT.Formulation))
g.add((formulation2, RDFS.label, Literal("Fast Charge Formulation")))
g.add((battery2, BAT.hasFormulation, formulation2))
g.add((formulation2, BAT.hasSolidsContent, Literal("55%")))
g.add((formulation2, BAT.hasActiveContent, Literal("75%")))
g.add((formulation2, BAT.hasConductiveContent, Literal("7%")))
g.add((formulation2, BAT.hasBinderContent, Literal("8%")))
g.add((formulation2, BAT.hasTemperature, Literal("30")))
g.add((formulation2, BAT.hasHumidity, Literal("25")))

# Coating for Battery002
coating2 = BAT["Coating002"]
g.add((coating2, RDF.type, BAT.Coating))
g.add((coating2, RDFS.label, Literal("Conductive Coating")))
g.add((battery2, BAT.hasCoating, coating2))
g.add((coating2, BAT.hasCoatingParameter, Literal("thickness: 3 microns")))

# Testing Protocol for Battery002
testing2 = BAT["Testing002"]
g.add((testing2, RDF.type, BAT.Testing))
g.add((testing2, RDFS.label, Literal("High Current Test")))
g.add((battery2, BAT.hasTesting, testing2))
g.add((testing2, BAT.hasTestingParameter, Literal("current: 2C")))

# ----------------------------
# Battery003: Long-life Battery
battery3 = BAT["Battery003"]
g.add((battery3, RDF.type, BAT.Battery))
g.add((battery3, RDFS.label, Literal("Long-life Battery")))

# Material Components for Battery003
anode3 = BAT["Anode_Silicon"]
g.add((anode3, RDF.type, BAT.Anode))
g.add((anode3, RDFS.label, Literal("Silicon Anode")))
g.add((battery3, BAT.hasComponent, anode3))

cathode3 = BAT["Cathode_NMC"]
g.add((cathode3, RDF.type, BAT.Cathode))
g.add((cathode3, RDFS.label, Literal("Nickel Manganese Cobalt Oxide Cathode")))
g.add((battery3, BAT.hasComponent, cathode3))

electrolyte3 = BAT["Electrolyte_Solid"]
g.add((electrolyte3, RDF.type, BAT.Electrolyte))
g.add((electrolyte3, RDFS.label, Literal("Solid Electrolyte")))
g.add((battery3, BAT.hasComponent, electrolyte3))

separator3 = BAT["Separator_Ceramic"]
g.add((separator3, RDF.type, BAT.Separator))
g.add((separator3, RDFS.label, Literal("Ceramic Separator")))
g.add((battery3, BAT.hasComponent, separator3))

# Formulation for Battery003 with its own parameter values
formulation3 = BAT["Formulation003"]
g.add((formulation3, RDF.type, BAT.Formulation))
g.add((formulation3, RDFS.label, Literal("Long-life Formulation")))
g.add((battery3, BAT.hasFormulation, formulation3))
g.add((formulation3, BAT.hasSolidsContent, Literal("60%")))
g.add((formulation3, BAT.hasActiveContent, Literal("85%")))
g.add((formulation3, BAT.hasConductiveContent, Literal("6%")))
g.add((formulation3, BAT.hasBinderContent, Literal("9%")))
g.add((formulation3, BAT.hasTemperature, Literal("25")))
g.add((formulation3, BAT.hasHumidity, Literal("18")))

# Coating for Battery003
coating3 = BAT["Coating003"]
g.add((coating3, RDF.type, BAT.Coating))
g.add((coating3, RDFS.label, Literal("Durable Coating")))
g.add((battery3, BAT.hasCoating, coating3))
g.add((coating3, BAT.hasCoatingParameter, Literal("thickness: 6 microns")))

# Testing Protocol for Battery003
testing3 = BAT["Testing003"]
g.add((testing3, RDF.type, BAT.Testing))
g.add((testing3, RDFS.label, Literal("Calendar Life Test")))
g.add((battery3, BAT.hasTesting, testing3))
g.add((testing3, BAT.hasTestingParameter, Literal("calendar life: 10 years")))

# ----------------------------
# Serialize the graph to RDF/XML (OWL-compatible format)
owl_data = g.serialize(format="xml")

# Save the ontology as an OWL file
with open("battery_ontology3.owl", "w", encoding="utf-8") as f:
    f.write(owl_data)

# Optionally, print the serialized OWL data
print(owl_data)
