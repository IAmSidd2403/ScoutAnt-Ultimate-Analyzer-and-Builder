import spacy
nlp = spacy.load("en_core_web_sm")
text = "What is the best agent for TenZ on Bind?"
doc = nlp(text)
print("Entities:", [(ent.text, ent.label_) for ent in doc.ents])
print("Tokens:", [(t.text, t.pos_) for t in doc])
