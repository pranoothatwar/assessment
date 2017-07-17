sent_ = raw_input("enter : ")
sent = sent_.split()
a = []
b ={}
for i in sent:
    if i not in a:
        b[i]=1
        a.append(i)
    else:
        b[i] = b[i]+1

print b
        
