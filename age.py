import datetime

def calcCenturyYear(name,age):
	if age > 100:
		print("Hi! "+name.capitalize()+" you already turned 100")
	else:
		year = datetime.datetime.now().year
		difference = 100 - age
		result = difference + int(year)
		print("You will turn 100 in "+str(result))

name = str(input("Hi! What's your name : "))
age = int(input("Hi! "+name.capitalize()+" How old are you : "))
calcCenturyYear(name,age)