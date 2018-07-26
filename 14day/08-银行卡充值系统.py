list = []
import time
#import time

def add():
	a = {}
	name = input("请输入办理人的姓名:")
	time.time()
	print("银行卡号,时间戳")	
	while True:
		pwd = input("请输入密码:")
		if len(pwd)==6:
			pwd=int(pwd)
			a["pwd"]=pwd
			print("创建完成")
			break

		else:
			print("请输入正确六位数字")
	info()			 
	a["name"]=name
	#a["pwd"]=pwd
	list.append(a)

def chongz():
	print("呵呵")	



def chaxun():
	pass
def xiugai():
	pass
def zhuxiao():
	pass
def daying():
	pass
def tuichu():
	pass











def zhuye():
	while True:
		print("欢迎来到***银行".center(50," "))
		print("1:办理银行卡")
		print("2:充值银行卡")
		print("3:查询银行卡金额")
		print("4:修改银行卡密码")
		print("5:注销银行卡号")
		print("6:业务办理完成")
		print("7:查看个人资产")
		info()

def info():
	name = int(input("请您选择序号:"))
	if name ==1:
		add()
	elif name ==2:
		chongz()
	elif name ==3:
		chaxun()
	elif name ==4:
		xiugai()
	elif name ==5:
		zhuxiao()
	elif name==6:
		daying()
	elif name==7:
		tuichu()
		
	


zhuye()






	





