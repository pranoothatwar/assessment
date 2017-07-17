class func():
    """

    parameters
    ----------
    b : list
    a : int or char, element to be added or deleted
    
    """
    def __init__(self,b,a):
        self.a = a
        self.b = b

    def append(self,b,a):
        return (self.b).append(self.a)

    def delete(self,b,a):
        return (self.b).append(self.a)


if __name__ == ' __main__':
    a = [1,2,3,4,5]
    print "hello"

    k = func()
    k.append(a,4)
    print a
        
