import random
suiji = random.randint(1,100)
for i in range(101):
	user = int(input("请输入数字:"))
	if user > suiji:
		print("猜大")
	elif user < suiji:
		print("猜小了")	
	else:
		print("猜对了")
		break









