list = []
for i in range(3):
	dict = {}	
	name = input("请输入您的姓名:")
	age =int(input("请输入您的年龄:"))
	sex = input("请输入您的性别:")
	QQ = int(input("请输入您的qq号:"))
	wei = float(input("请输入您的体重:"))
	dict["name"]=name
	dict["age"]=age
	dict["sex"]=sex
	dict["QQ"]=QQ
	dict["wei"]=wei
	list.append(dict)
for i in list:
	print(i)

'''
	if name == name:
		i=i + 1
		print("名字重复,请重新输入:")
'''



