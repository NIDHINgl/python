thislist = ["apple", "banana", "cherry"]
print("thislist[1] is : ",thislist[1])
thislist[1] = "mango"
print("value changed thislist[1] is : ",thislist[1])
#index() used to get index of first value index("value") give specific value index
print("index of mango : ",thislist.index("mango"))
#list(mylist) also used to copy the list
mylist = thislist.copy()
print("copy() to mylist : ",mylist)
print("loop the list is : ")
for x in thislist:
	print(x)
if "apple" in thislist:
	print("apple is here")
#count of is used to get the count of particular value in list
print('count("mango") : ',thislist.count("mango"))
print("length of list : ",len(thislist))
#append orange in end
thislist.append("orange")
print("append : ",thislist)
#extend() add iterations in end
values = ["pineapple","dragon fruit","blue berry"]
thislist.extend(values)
print("extend() : ",thislist)
#insert banana at specified position
thislist.insert(0,"banana")
print("insert : ",thislist)
#to reverse the list
thislist.reverse()
print("reversed list : ",thislist)
#sorts the list ascending by default
thislist.sort()
print("sorted list : ",thislist)
"""if give reverse=True in sort it sort in descending order
we can assign some function name in key.both are optional"""
def myFun(e):
	return len(e)
thislist.sort(reverse=True,key=myFun)
print("sort list in reverse of length: ",thislist)
#remove specific element
thislist.remove("cherry")
print("removed cherry : ",thislist)
#pop is used to delete last position or specified position
thislist.pop(1)
print("pop(1) : ",thislist)
thislist.pop()
print("pop() : ",thislist)
#clear() used to empty the list
thislist.clear()
print("clear() : ",thislist)
#del is used to delete list
del thislist
try:
	print(thislist)
	"""if list deleted not defined error occure
	so use NameError to define this in exception handling"""
except NameError:
	print("List was deleted")
except:
	print("Someting went wrong")
