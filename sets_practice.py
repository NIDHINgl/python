thisset = {"apple", "banana", "cherry"}
print(thisset) 
for x in thisset:
  print(x) 
#Check if "banana" is present in the set if present print True else false
print("banana" in thisset)
thisset.add("orange")
print("added new value : ",thisset)
#update is used to enter multiple values
thisset.update(["pineapple","mango","lichy"])
print("updated multiple values : ",thisset)
print("length of set : ",len(thisset))
#remove and discard is used to remove values
#pop used to remove last value
thisset.remove("banana")
thisset.discard("apple")
print("removed values : ",thisset)
#find the difference b/w two sets
newset = {"mango","apple","blue berry"}
x = newset.difference(thisset)
print("difference is : ",x)
#intersection returns comomon values	
y = thisset.intersection(newset)
print("intersection : ",y)
#difference_update remove the common values
"""intersection_update remove the different values and update only common values
thisset.intersection_update(newset) """
thisset.difference_update(newset)
print('difference_update is : ',thisset)
#isdisjoint return true if none of the values are same in both sets otherwise return false
z= thisset.isdisjoint(newset)
print("isdisjoint : ",z)
#issubset return all True if all the items in specified set present in another one
z=thisset.issubset(newset)
print("issubset : ",z)
#issuperset just opposite of issubset check all the values in subset present in parent
z=thisset.issuperset(newset)
print("issuperset : ",z)
#union return unique values
z=thisset.union(newset)
print("union : ",z)