list = []

for i in range(3):
	add = {}
	name = input("请输入您的姓名:")
	sex = input("请输入您的性别:")
	age = input("请输入您的年龄:")
	add["name"] = name
	add["sex"]= sex
	add["age"]=age 

	list.append(add) 

for i in list:
	for j in i:
		print(i[j])




'''
添加3个人的身份证信息
定义一个空列表
请输入名字 name
请输入年龄 age
请输入性别 sex
构建一个字典 字典
把每个人的字典添加到列表当中

3个人添加都完成以后给遍历出来

[{"name":"老王"},{"name":"老宋"},{"name":"老李"}]
'''
