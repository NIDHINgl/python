import datetime

def calcCenturyYear(name,age):
	if age > 100:
		print("Hi! "+name.capitalize()+" you already turned 100")
	else:
		year = datetime.datetime.now().year
		difference = 100 - age
		result = difference + int(year)
		output = "You will turn 100 in {}"
		print(output.format(result))

name = str(input("Hi! What's your name : "))
try:
	age = int(input("Hi! "+name.capitalize()+" How old are you : "))
except:
	age = int(input("Hi! "+name.capitalize()+" Please enter correct age : "))

calcCenturyYear(name,age)
