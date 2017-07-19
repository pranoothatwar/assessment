sent=raw_input("Enter the string")
b=''
flag=True
for i in sent:
    if i=="@":
        flag=False
    if i==".":
        break
    if flag==False and i!="@":
        b=b+i
print b