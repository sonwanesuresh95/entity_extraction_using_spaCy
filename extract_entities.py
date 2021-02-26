# previous method
import spacy

# load spacy model
nlp = spacy.load('en_core_web_sm')

#new method
'''
import spacy
import en_core_web_sm
nlp = en_core_web_sm.load()'''

# function to extract entities
def extract_entities(text):
    entities = []
    doc = nlp(text)
    for e in doc.ents:
        entities.append((e.text, e.label_))
    return entities
