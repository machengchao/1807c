a = int(input("请输入年份:"))
if a % 4 == 0 and a % 100 != 0:
	print("闰年")
elif a % 400 == 0:
	print("润年")
else:
	print("平年")
