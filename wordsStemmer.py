#importing snowballstrmmer for stemming words
from nltk.stem import SnowballStemmer

def wordsStemmer(words):
 	#choosing english to stem words
 	stemmer = SnowballStemmer('english')
 	filtered_list = []
 	for wrd in words:
 		#adding every stemmed word into filtered list
 		filtered_list.append(stemmer.stem(wrd))
 	#returning filtered list
 	return filtered_list
 	
 	
