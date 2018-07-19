
list = []
list1 = [1,2,3,4]

list.append(list1)
#print(list)
list.extend(list1)
#print(list)
for i in list:
	print(i)

list = [2,3,55,44,100]

list.sort()
print(list)
list.sort(reverse=True)
print(list)
list.reverse()
print(list)




