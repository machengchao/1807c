weight = float(input("请输入身高:"))
height = float(input("请输入身价:"))
yan = float(input("请输入颜值分:"))
if weight > 180 and height > 1000000 and yan > 99:
	print("高富帅")

elif height > 1000000 and yan > 99:
	print("富帅")
elif yan > 99:
	print("帅")
elif weight < 160 and height < 100 and yan < 60:
	print("矮穷矬")





