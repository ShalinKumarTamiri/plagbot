"""
   This is a program for a plagiarism chatbot. 
   * It will greet the end user and self info and request for the name of the end user
   * The bot will great the end user 
   * The bot will ask the end user what to do 
   * It will take input and returns the output
"""

#importing greetings , choice and filechecker functions
from greetings import greetings
from choice import choice
from fileChecker import fileChecker
from welcome import welcome

def bot():
 	#printing greetings
 	print(greetings())
 	#Taking name of the user
 	name = input()
 	welcome(name)
 	while(True):
 		#Taking choice from user
 		option = choice()
 		if option == 1:
 			#calling filechecker function to find plagiarism
 			fileChecker()
 			print()
 		elif option == 2:
 			#Exiting from the program
 			break
 	print("\nThank you {0} for utilizing me.".format(name ))
 
#calling bot function	    
bot()