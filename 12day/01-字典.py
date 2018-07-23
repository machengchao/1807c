d={'name':'马成超','xb':'男','cs':'1999年','dz':'哈尔滨','ah':'美女'}
d['nl']=20
print(d)
print('')

d.pop('dz')
print(d)
print('')

d['xb']='女'
print(d)
print('')

print(d['ah'])
print('')

for i in d:
	print(i)
	print(d[i])
print('')

for j in d.keys():
	print(j)
	print(d[j])
print('')

for n in d.values():
	print(n)
print('')

for k,v in d.items():
	print(k)
	print(v) 
print('')

for l in d.items():
	print(l)
	print(l[0])
	print(l[1])





