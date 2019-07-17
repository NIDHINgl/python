import re
#findall
str = "The rain in Spain falls mainly in the plain!"

#Check if the string contains "ai" followed by 1 or more "x" characters:

x = re.findall("aix+", str)

print("aix+ : ",x)
x = re.findall("aix*", str)

print("aix* : ",x)
x= re.findall("[a-m]",str)
print("[a-m] : ",x)
str = "That will be 59 dollars"	
x=re.findall("\d",str)
print("\d : ",x)
str = "hello world"
#return a string from beginning to last word
x=re.findall("he... w",str)
print("he... w : ",x)
x=re.findall("^he",str)
print("^he : ",x)
x=re.findall("world$",str)
print("world$ : ",x)
str = "The rain in Spain falls mainly in the plain!"
#check if the string contain "a" followed by exactly 2 "l"
x=re.findall("al{2}",str)
print("al{2} : ",x)
x=re.findall("falls|stays",str)
print("falls|stays : ",x)

#Special Sequences
str="The rain in spain"
#check if sentence start with specific value
x=re.findall("\AThe",str)
print(x)