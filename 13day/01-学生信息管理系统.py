list = []
print("欢迎进入学生管理系统")
while True:
	a = {}
	print("1:增加学生信息")
	print("2:查找学生信息")
	print("3:修改学生信息")
	print("4:删除学生信息")
	print("5:退出学生信息")
	print("6:打印全部学生信息")
	num = int(input("请选择功能:"))
	if num == 1:
		name = input("请输入您要添加的名字:")
		age = int(input("请输入您要添加的年龄:"))
		a["name"]=name
		a["age"]=age
		list.append(a)
	elif num ==2:
		name = input("请输入您的要查找的名字:")
		for stu in list:
			if stu["name"] == name:
				print("学生姓名:%s\n学生年龄:%d\n"%(stu["name"],stu["age"]))
				break			
	elif num ==3:			
		name = input("请输入您的要修改的名字:")
		for stu in list:
			if stu["name"] == name:
				print("学生姓名:%s\n学生年龄:%d\n"%(stu["name"],stu["age"]))
				print("1:修改姓名")
				print("2:修改年龄")
				num=int(input("请选择修改序号:"))			
				if num == 1:
					name = input("请输入新的名字:")
					stu["name"]=name
				elif num ==2:
					age = int(input("请输入新的年龄:"))
					stu["age"]=age
				print("修改成功")
				break
#	elif num ==4:
'''
		print("1:删除名字")
		print("2:删除年龄")
		num == int(input("请您选择序号:"))
		if num ==1:
			list.pop(position)
'''












	

'''
	elif num == 5:
		print("确定要退出吗?")
		print("1:确认退出")
		print("2:继续使用")
		num = int(input("请选择序号:"))
		if num ==1:
			break
			
	elif num ==6:
		pass



'''








