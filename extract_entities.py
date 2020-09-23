import spacy

# load spacy model
nlp = spacy.load('en_core_web_sm')


# function to extract entities
def extract_entities(text):
    entities = []
    doc = nlp(text)
    for e in doc.ents:
        entities.append((e.text, e.label_))
    return entities
