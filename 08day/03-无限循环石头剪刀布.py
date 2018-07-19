#1 ------石头
#2 ------剪刀
#3 ------布



while True:

	cp = int(input("我出拳"))

	import random
	pc = random.randint(1,3)#电脑出拳

	if cp <= 3 and cp > 0:
		if ( cp == 1 and pc == 2 ) or (cp == 2 and pc == 3) or(cp == 3 and pc ==1):
			print("玩家一赢")
		elif cp == pc: 
			print("平局")
		else:
			print("电脑赢")

	else:
		print("误")


