#1------石头
#2------剪刀
#3------布


for i in range(100):
	import random
	pc = random.randint(1,3)
	cp = int(input("请您输入序号:1.石头,2.剪刀,3.布"))
	if cp > 4 and cp < 0:
		print("您输入有误,请重新输入")
	if (cp == 1 and pc == 2) or(cp ==2 and pc == 3)or (cp == 3 and pc ==1):
		print("玩家赢")
	elif cp == pc:
		print("平局")
	else:
		print("系统赢")
	




