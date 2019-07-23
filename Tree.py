from termcolor import colored
import math

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
	"""using this formula to
	get perfect shape"""
	x = math.ceil(n * (30/100))
	k = 2 * n - 3
	for i in range(0,x):
		for j in range(0,k):
			print(end=" ")
		print(colored("| |","red"),end="")
		print("\r")

try:
	n = int(input("Enter a number : "))
except:
	n = int(input("Please enter a valid number : "))
leaf(n)

