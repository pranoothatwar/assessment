def end(n):
    return n[-1]  
 
def sort(tuple_):
    return sorted(tuple_, key=end)
 
a=input("Enter a list of tuples:")
print "Sorted --> ","\n", sort(a)
