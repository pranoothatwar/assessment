class strn():

    def __init__(self):
        self.str1 = ''
    
    def add(self):
        self.str1=raw_input("Enter string: ")

    def print_(self):
        print(self.str1)


strg = strn()
strg.add()
strg.print_()
