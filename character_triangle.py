def triangle(n,num):
    for i in range(0,n):
        for j in range(0,i+1):
            letter = chr(num)
            print(letter,end=" ")
        num = num + 1
        print('\r')
n = 5
num = 65
triangle(5,65)