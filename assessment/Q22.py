text_ = raw_input("Enter something : ")
num_count =0
num_letter=0
for i in text_:
    if i.isdigit():
        num_count+=1
    else:
        num_letter+=1

print "LETTERS : ", num_letter, "\nDIGITS : ", num_count
