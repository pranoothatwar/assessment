file_name = raw_input("Enter name of file : ")
file_ = open(file_name+".txt","a")
c = raw_input("Enter the sentence: ");
file_.write(c)
file_.close()
file_1=open(file_name+".txt",'rb')
line_=file_1.readline()
while(line_!=""):
    print(line_)
    line_ = file_1.readline()    
file_1.close()
