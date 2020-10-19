#function to make choices 
def choice():
 	print("\nLets check for plagiarsm in \n")
 	print("1.Checking in files 2.Exit")
 	print("Enter your choice (1 or 2) : ")
 	try:
 		#returning user input
 		return int(input())
 	except:
 		
 		print("Invalid input!!! Please enter a number between 1 and 2 ")
 		