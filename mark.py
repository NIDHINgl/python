"""Given the names and grades for each student in a Physics class of students, store them in a nested list and print the name(s) of any student(s) having the second lowest grade.

**Note**: If there are multiple students with the same grade, order their names alphabetically and print each name on a new line.

**Input Format**
    The first line contains an integer,N , the number of students.
    The 2N subsequent lines describe each student over lines; the first line contains a student's name, and the second line contains their grade. 
**Output Format**
     Print the name(s) of any student(s) having the second lowest grade in Physics; if there are multiple students, order their names alphabetically and print each one on a new line."""

#hacker rank rested list question
index  = []
new = []
def Sort(mark_list):
    sorted_list = sorted(mark_list, key = lambda x:x[1])
    numbers = []
    for x in range(len(sorted_list)):
    	numbers.append(sorted_list[x][1])
    numbers = list(dict.fromkeys(numbers))
    temp = numbers[1]
    for j in range(len(mark_list)):
        if mark_list[j][1] == temp:
            index.append(j)
    for k in range(len(index)):
        new.append(mark_list[index[k]])
    ordered_list = sorted(new, key = lambda x:x[0])
    for i in range(len(ordered_list)):
        print(ordered_list[i][0])

mark_list = []
for i in range(int(input())):
    mark_list.append([])
    name = input()
    score = float(input())
    for j in range(0,1):
        mark_list[i].append(name)
        mark_list[i].append(score)
Sort(mark_list)
