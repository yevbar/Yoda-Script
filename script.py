import spacy
from nltk import Tree

en_nlp = spacy.load("en")

doc = en_nlp(u'The quick brown fox jumps over the lazy dog and the magical unicorn flew over the rainbow.')

def clausify(doc):
    output = []
    cur = []
    for token in doc:
        if token.dep_ == 'cc':
            output.append(cur)
            output.append([token])
            cur = []
        else
            cur.append(token)
    output.append(cur)
    return output


for token in doc:
    print (token.text, token.dep_)
    print "~~~~~~~"
    print clausify(doc)
    #print(token.text, token.lemma_, token.pos_, token.tag_, token.dep_,token.shape_, token.is_alpha, token.is_stop)
