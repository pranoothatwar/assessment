import collections
sent = raw_input("Enter text:")
a = []
for i in sent:
    a.append(i)
for i in set(a):
    print i+",",
    print a.count(i)