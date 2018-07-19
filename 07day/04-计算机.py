
x = float(input("请输入值"))
y = float(input("请输入值"))
z = input("请选择\n+.\n-.\n*.\n/")
if z == "+":
	print("%.02f+%.02f=%.02f"%(x,y,x+y))
elif z == "-":
	print("%.02f-%.02f=%.02f"%(x,y,x-y))
elif z == "*":
	print("%.02f*%.02f=%.02f"%(x,y,x*y))
elif z == "/":
	print("%.02f/%.02f=%.02f"%(x,y,x/y))

'''
x = int(input("请输入x的值"))
y = int(input("请输入y的值"))
c = 0
z = input("请选择标点符号,+-*/")
if z == "+":
	c = c +x+y
	print("x和y的和是%d"%(c))
elif z == "-":
	c = c+c-y
	print("x和y的差是%d"%(c))
elif z == "*":
	c = c+c*y
	print("x和y的积是%d"%(c))
elif z == "/":
	c =c+x/y
	print("x和y的商是%d"(c))
else:
	print("输入错误")
'''
