#
# Cameron Hawtin
# 101047338
# 
# Gaddis, T. (2015). "Starting Out With Python"
#
# This program loads a string from an external file and uses
# it's contents to form a homoglyph translation dictionary. 
#
# The external file contains: ";R:12;I:1;E:3;D:cl;I:!;B:!3;G:(_+;J :(/;:"
#

# Function to insert a new translation
def myInsert(mydict, key, value):
	if key in mydict: 
		print("This key already exists. Nothing was added.")
		return False
	else:
		mydict[key] = value
		return True
# Function to delete a translation		
def myDelete(mydict, key):
	if key in mydict:
		mydict[key] = key
		return True
	else:
		print("This key does not exist. Nothing was deleted.")
		return False

def main():		
	mydict = {}
	# Open and clean up the information into a list format
	file = open("example glyphs.dat", "r")
	list = file.read()
	list = "".join(list.split())
	list = list.strip(":")  
	list = list.strip(";")
	list = list.split(";")
	for i in range(8):
		list[i] = list[i].split(":")
	# Moves the list into a useable dictionary	
	for i in range (0, len(list)):
		a = list[0][0]
		b = list[0][1]
		mydict[a] = b
		del list[0]
	# Loop through the menu to build up the dictionary and translate strings
	while True:
		print("\nYour current dictionary is: ")
		print(mydict)
		ans = input("\nWould you like to '(q)uit', '(t)ranslate', '(i)nsert', or '(d)elete'?: ")
		# Quit program
		if ans == "quit" or ans == "q":
			break
		# Translate input string
		## Since my generator did not specify how it wanted me to translate 
		## given strings, I had to make the assumption that this is how 
		## it was supposed to be done. Only delete and insert functions were 
		## given instructions for my generated assignment.
		elif ans == "translate" or ans == "t":
			string = input("\nEnter the string you would like to translate: ")
			print("\nTranslation: ")
			for i in range(0, len(string)):
				if string[i] in mydict:
					print(mydict[string[i]], end="")
				else:
					print(string[i], end="")
			print()
		# Insert new translations
		elif ans == "insert" or ans == "i":
			newkey = input("\nEnter the key you would like to insert:  ")
			newvalue = input("Enter the value you would like associate with the key :")
			myInsert(mydict, newkey, newvalue)		
		# Delete a translation
		elif ans == "delete" or ans == "d":
			newkey = input("\nEnter the key you would like to delete:  ")
			myDelete(mydict, newkey)
		else:
			print("Incorrect input. Please choose specified answer")
		
main()
