#finding lowest mark scored student from list of students
#input format : first enter number of students then press enter -> student name then press enter -> student mark then press enter
#output format : lowest scored student name

index  = []
new = []
def Sort(mark_list):
	temp = mark_list[0][1]
	for i in range(len(mark_list)):
		val = mark_list[i][1]
		if val < temp:
			temp = val
	for j in range(len(mark_list)):
		if mark_list[j][1] == temp:
			index.append(j)
	for k in range(len(index)):
		new.append(mark_list[index[k]])
	final_list = sorted(new, key = lambda x:x[0])
	for x in range(len(final_list)):
		print(final_list[x][0])

mark_list = []
for i in range(int(input())):
	mark_list.append([])
	name = input()
	score = float(input())
	for j in range(0,1):
		mark_list[i].append(name)
		mark_list[i].append(score)
Sort(mark_list)
