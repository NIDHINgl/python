from termcolor import colored

def leaf(n):
	k = 2 * n - 2
	for i in range(0,n):
		for j in range(0,k):
			print(end=" ")
		k = k - 1
		for j in range(0,i+1):
			print(colored("* ","green"),end="")
		print("\r")
	stem(n)
def stem(n):
	x = 2 * n - 3
	for i in range(0,2):
		for j in range(0,x):
			print(end=" ")
		print(colored("| |","red"),end="")
		print("\r")

n = int(input("enter a number : "))
leaf(n)

