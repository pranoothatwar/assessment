a=(1,2,3,4,5,6,7,8,9,10)
b=list()
for i in range(0,len(a)):
    if a[i]%2==0:
        b.append(a[i])

c=tuple(b)
print c