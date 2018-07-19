q = 0 
w = 0
while w<=100:
	if w %2 ==0:
		q +=w
	w +=1
a = 0
b = 0
while b<=100:
	if b %2 !=0:
     #   print(b)
		a +=b
	b +=1
print('0~100之间奇数和是 = %d'%q)
print('0~100之间偶数求和结果是 = %d'%a)
l =(a-q)
print('1-2+3-4+5-6+7-8...+99的和是%d:'%l)
                                              
