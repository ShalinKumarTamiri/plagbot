import random

#function for greetings
def greetings():
	#creating multiple greetings
	greeting_responses = ["Hi !!! I am plagbot \nI can help you to check the plagiarism \nMay I have your name ",
	                                       "Hello !!! I am plagbot \nI can do plagiarism checks for you \nCan I know your name ",
	                                       "Welcome aboard new buddy !!! I am plag bot \nYou can do plagiarism checks with me \nBefore we start can you say your name "]
	#returning response randomly
	return random.choice(greeting_responses)