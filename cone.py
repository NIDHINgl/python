def cone(number):
	space = 0
	for i in range(0,number):
		for k in range(0,space):
			print(end=" ")
		space = space + 1	
		for j in range(0,number):
			print("*",end=" ")
		number = number - 1
		print("\r")
    
number = int(input("Enter a number : "))
cone(number)
