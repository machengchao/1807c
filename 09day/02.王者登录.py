
while True:
	acc = int(input("请输入账号:"))
	passwd = int(input("请输入密码:"))
	if acc == 123456 and passwd == 123456:
		print("登陆成功")
	else:
		print("登陆失败")	
	print("****0代表ADC,1代表肉,3代表法师")
	xuan = int(input("请选择英雄范围:"))
	if xuan == 0:
		print("鲁班大师")
	elif xuan == 1:
		print("程咬金")
	elif xuan == 2:
		print("王昭君")
	else:
		print("输入错误")
	




