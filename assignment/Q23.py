import math
def bin_search(a, element):
    bottom = 0
    top = len(a)-1
    index = -1
    while top>=bottom and index==-1:
        mid = int(math.floor((top+bottom)/2.0))
        if a[mid]==element:
            index = mid
        elif a[mid]>element:
            top = mid-1
        else:
            bottom = mid+1
    return index

a=[2,5,7,9,11,17,222]
print bin_search(a,11)