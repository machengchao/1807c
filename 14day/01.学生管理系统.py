list = []
while True:
	a = {}  
	print("欢迎来到学生管理系统")
	print("1:增加学生信息")
	print("2:查找学生信息")
	print("3:更改学生信息")
	print("4:删除学生信息")
	print("5:退出学生系统")
	num = int(input("请您选择序号:"))
	if num == 1:
		name = input("请您输入学生姓名:")
		age = input("请您输入学生年龄:")
		phone = int(input("请您输入学生手机号:"))
		a["name"]=name
		a["age"]=age
		a["phone"]=phone
		list.append(a)
	if num ==2:
		name = input("请输入您要查找的名字:")
		for stu in list:
			if stu["name"] ==name:
				print("学生姓名:%s\n学生年龄:%s\n学生手机号:%d\n"%(stu["name"],stu["age"],stu["phone"]))
				break
	elif num ==3:
		name = input("请输入您要修改的名字:")
		for stu in list:
			if stu["name"] ==name:
				print("学生姓名:%s\n学生年龄:%s\n学生手机号:%d\n"%(stu["name"],stu["age"],stu["phone"]))
			





