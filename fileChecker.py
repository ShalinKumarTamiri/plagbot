import string 
from plagiarismChecker import plagiarismChecker
from wordsStemmer import wordsStemmer
from stopwords import stopwords

def fileChecker():
 	file1 = 0
 	file2 = 0
 	words = []
 	while(True):
 		file1 = input("Enter file1 name : ")
 		try:
 			file1 = open(file1,"r")
 			
 			for line in file1:
 				for w in line.split():
 					words.append(w)
 			words = list(set(words))
 			filtered_list1 = [wrd for wrd in words if not wrd in stopwords]
 			break
 		except:
 			print("Enter an exisiting file!!!")
 	while(True):
 		file2 = input("Enter file2 name : ")
 		try:
 			file2 = open(file2,"r")
 			for line in file2:
 				for w in line.split():
 					words.append(w)
 			words = list(set(words))
 			filtered_list2 = [wrd for wrd in words if not wrd in stopwords]
 			break
 		except:
 			print("Enter an existing file!!!")
 	word_file1=[]
 	word_file2=[]
 	for wrd in filtered_list1:
 		if wrd not in string.punctuation:
 			word_file1.append(wrd)
 	for wrd in filtered_list2:
 		if wrd not in string.punctuation:
 			word_file2.append(wrd)
 	words_f1 = wordsStemmer(word_file1)
 	words_f2 = wordsStemmer(word_file2)
 	plagiarismChecker(words_f1,words_f2)
 	
