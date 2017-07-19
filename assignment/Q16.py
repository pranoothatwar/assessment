A=[1,2,3]
B=[]
for i in A:
    t=A.index(i)
    A.remove(i)
    B.append([i,A[0],A[1]])
    B.append([i,A[1],A[0]])
    A.insert(t,i)
for i in B:
    print i,
    