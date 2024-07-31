#strings are immutable means they can't be change in place
name=("ishan!!!!")
title=("SAWARN")
print(name)
print(name.upper())#change the string to upper case
print(title)
print(title.lower())#change the string to lower case
#  note that it can't the string it just make a another string lower or upper case
print(name.rstrip("!"))#cutsd the trailing character
print(name.replace("ishan","shubham"))
fullname=("ishan sawarn")
print(fullname.split(" "))#splits the string whenever it hits with space in string and make a list 
print(name.capitalize())#capitalize the first letter
print(name.center(50))#centre the whole string as given parameter
print(name.count("a"))#counts that how many times a character occur
print(name.endswith("!"))#tells that a string ending with specific char or not
print(name.startswith("i"))#tells that a string starting with specific char or not
print(name.find("a"))#returns the index of the first occurence of a char
print(title.isalnum())#returns true if the string contain only alpha and numeric charcter
print(name.isalnum())#returns  false because it conatain ! character
print(title.isalpha())#returns true if strings have only alpha charater
print(title.islower())#returns true if string is fully in lower case
print(title.isprintable())#returns true if string is printable
print(title.isspace())#returns true if string only contains white space
print(title.istitle())#returns true if all the words's first letter id captallized
print(title.swapcase())#changes the case of string
text=("vmtgmy gkjmthoykh tkg yg")
print(text.title())#makes the first letter of every word to uppercase