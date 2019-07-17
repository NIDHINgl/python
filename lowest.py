def Sort(sub_li): 
    l = len(sub_li) 
    for i in range(0, l): 
        for j in range(0, l-i-1): 
            if (sub_li[j][1] > sub_li[j + 1][1]): 
                tempo = sub_li[j] 
                sub_li[j]= sub_li[j + 1] 
                sub_li[j + 1]= tempo 
    print(sub_li[1][0])
    print(sub_li[2][0])
n = input()
sub_li = list()
for i in range(n):
	ls = []
	name = raw_input()
	mark = input()
	ls.append(name)
	ls.append(mark)
	sub_li.append(ls)
Sort(sub_li)