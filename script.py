import spacy
from nltk import Tree

punctuation = [u',', u'.', u';', u'?']

nlp = spacy.load("en")

text = "I like cake. The quick brown fox jumped over the lazy log. When I went to the store, to buy milk, the low fat one, I walked, albeit slowly, over a manhole, which had a strange pink cover. The horse raced past the barn fell. Anyone who feels that if so many more students whom we haven't actually admitted are sitting in on the course than ones we have that the room had to be changed, then probably auditors will have to be excluded, is likely to agree the curiculum needs revision."

def sentify(text):
	output = []
	doc = nlp(unicode(text, 'utf-8'))
	for sent in doc.sents:
		for clause in clausify(sent):
			output.append(yodafy(clause))
	return output

def clausify(sent):
	output = []
	cur = []
	for token in sent:
		if token.dep_ == u'cc' or (token.dep_ == u'punct' and token.text in punctuation):
	        	output.append(cur)
        		output.append([token])
	        	cur = []
		else:
			cur.append(token)
	if cur != []:
		output.append(cur)
	return output

def yodafy(clause):
	new_array = []
	state = False
	for token in clause:
	        if state:
        	        new_array.append(token)
	        if not state and (token.dep_ == unicode("ROOT", "utf-8") or token.dep_ == unicode("aux", "utf-8")):
	                state = True
	new_array.append(",")
	for token in clause:
	        new_array.append(token)
	        if token.dep_ == unicode("ROOT", "utf-8") or token.dep_ == unicode("aux", "utf-8"):
	                break
	return new_array

print sentify(text)

"""
for token in doc:
    print (token.text, token.dep_)
print "~~~~~~~"
print clausify(doc)
    #print(token.text, token.lemma_, token.pos_, token.tag_, token.dep_,token.shape_, token.is_alpha, token.is_stop)
"""
