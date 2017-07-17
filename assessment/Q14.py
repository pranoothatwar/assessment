a = raw_input("enter a number: ")
b = bin(int(a))[2::]
if int(b) == 10**(len(b)-1):
	print "power of 2"
else:
	print "not a power of 2"
	