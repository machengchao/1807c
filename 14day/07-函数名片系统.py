list = []

def add():
	a = {}	
	name = input("请输入您的名字:")
	ming = input("请输入您的民族:")
	a["name"]=name
	a["ming"]=ming
	
	list.append(a)
def cha():
	name = input("请您输入您要查找的名字:")
	for i in list:
	
		if i["name"] == name:
			print("学生名字:%s\n学生民族:%s\n"%(i["name"],i["ming"]))
		else:
			print("查无此人")	
			break
def gai():

	name = input("请您输入您要修改的名字:")
	for i in list:
		if i["name"] == name:
			print("1:修改名字")
			print("2:修改民族")
			stu = int(input("请您选择序号:"))
			if stu ==1:
				name = input("请您输入新的名字:")
				i["name"] = name
			elif stu==2:
				ming = input("请您输入新的民族:")
				i["ming"] = ming
				print("打印成功")
				break

def shan():
	name = input("请输入你要删除的名字")
	flag = False
	for position,i in enumerate(list):#把索引遍历出来
		if i["name"] == name:
			flag = True#找到了
			print("1:确认删除")
			print("2:取消删除")
			num_2 = int(input("请选择序号"))
			if num_2 == 1:
				list.pop(position)#直接删除
				print("删除成功")
				


def yin():
	print("名字\t民族")
	for i in list:
		print(" "+i["name"]+"\t "+i["ming"])








def tui():
	print("1:退出系统")
	print("2:继续使用")	
	num = int(input("请您输入序号"))
	if num == 1:
		exit()
		print("欢迎下次使用")
	elif num ==2:
		print("继续使用")






def menu():
	print("欢迎来到学生管理系统".center(50," "))
	while True:
		print("1:增加学生信息")
		print("2:查找学生信息")
		print("3:更改学生信息")
		print("4:删除学生信息")
		print("5:打印学生信息")
		print("6:退出学生系统")
		info()
def info():
	num = int(input("请您输入序号:"))
	if num == 1:
		add()
	elif num == 2:
		cha()
	elif num ==3:
		gai()
	elif num == 4:
		shan()
	elif num ==5:
		yin()
	elif num ==6:
		tui()

menu()





