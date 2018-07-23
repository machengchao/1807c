def print_sum(suizi):#形参
	sum = 0
	for i in range(1,suizi+1):
		sum+=i 
	print(sum)
suizi = int(input("请输入数字:"))
print_sum(suizi)#实参
