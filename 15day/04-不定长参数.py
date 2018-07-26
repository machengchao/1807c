def test(a,*ma,b=12,**chao):
	sum = 0
	for i in ma:
		sum = sum+i
	sum1 = 0
	for j,v in chao.items():
		sum1 = sum1+v
	c = a+b+sum+sum1				
	print(c) 
'''
	print(a)
118	print(b)
	print(ma)
	print(chao)
'''

test(1,2,3,4,5,b=20,m=12,n=21)
