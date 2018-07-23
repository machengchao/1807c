def suiji():
	import random
	list = []
	for i in range(10):
		n=random.randint(1,100)
		if n not in list:
			list.append(n)
	print(list)
suiji()

