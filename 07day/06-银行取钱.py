a = 1234
b = 1234
c = 20000
d = int(input("请输入账号"))
e = int(input("请输入密码"))
if d==a and e==a:
	print("就可以取钱了")
	f = int(input("请输入取钱金额:"))
	if f > c:
		print("没钱取毛钱")
	else:
		print("取了%d的钱,还剩%d的钱"%(f,c-f))
else:
	print("密码输入错误")	
	
