import spacy
from nltk import Tree

punctuation = [u',', u'.', u';', u'?']
nlp = spacy.load("en")
comma = nlp(u'Hello, World')[1]

text = "I like cake. The quick brown fox jumped over the lazy log. When I went to the store, to buy milk, the low fat one, I walked, albeit slowly, over a manhole, which had a strange pink cover. The horse raced past the barn fell. Anyone who feels that if so many more students whom we haven't actually admitted are sitting in on the course than ones we have that the room had to be changed, then probably auditors will have to be excluded, is likely to agree the curiculum needs revision."

def sentify(text):
	output = []
	doc = nlp(unicode(text, 'utf-8'))
	for token in doc:
		print token.text + " - " + token.dep_
	for sent in doc.sents:
		sentence = []
		for clause in clausify(sent):
			sentence.append(yodafy(clause))
		output.append(sentence)
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
	if len(new_array) > 0 and new_array[len(new_array)-1].dep_ != u'punct':
		new_array.append(comma)
	for token in clause:
	        new_array.append(token)
	        if token.dep_ == unicode("ROOT", "utf-8") or token.dep_ == unicode("aux", "utf-8"):
	                break
	return new_array

# TODO Handle punctuation of commas
# TODO Handle capitalization

string = ""
yodafied = sentify(text)
for sentence in yodafied:
	sentence_ = ""
	for clause in sentence:
		for token in clause:
			if token.dep_ == u'NNP' or token.dep_ == u'NNPS' or token.text == u'I':
				sentence_ += token.text + " "
			elif sentence_ == "":
				sentence_ += token.text[0].upper() + token.text[1:] + " "
			elif token.dep_ == u'punct':
				#print "Well gee golly, < " + token.text + " >"
				sentence_ = sentence_[:len(sentence_)-1] + token.text + " "
			else:
				sentence_+=token.text.lower() + " "
	print sentence_
print string

"""
for token in doc:
    print (token.text, token.dep_)
print "~~~~~~~"
print clausify(doc)
    #print(token.text, token.lemma_, token.pos_, token.tag_, token.dep_,token.shape_, token.is_alpha, token.is_stop)
"""
