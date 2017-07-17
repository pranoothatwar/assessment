len_ = int(raw_input("tell lengeth of list : "))

a = []

for i in range(len_):
	c = (int(raw_input("input the number")))
	a.append(c)
	#print a


l = a[0]
m = a[len(a)-1]

count = 0
for i in a:
	#print i,count+1,
	if (i != count+1):
		print count+1,
		count = count +1
	count = count +1
	#print count