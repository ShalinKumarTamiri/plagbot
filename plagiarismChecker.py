def plagiarismChecker(words_file1 , words_file2):
 	length1 = len(words_file1)
 	length2 = len(words_file2)
 	common_list = []
 	for word in words_file1:
 		if word in words_file2:
 			common_list.append(word)
 	common_length = len(common_list)
 	unique_words1_length = length1 - common_length
 	unique_words2_length = length2 - common_length
 	uniqueness = ((unique_words1_length + unique_words2_length)/(length1+length2))*100
 	print("The files are {0}% similar ".format(100-uniqueness))