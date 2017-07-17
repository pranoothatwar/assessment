f_name = raw_input("Enter an exisitng file name along with valid extenstion: ")
num = 0
with open(f_name , 'rb') as f:
    for line in f:
        num = num + 1
print("No. of lines: ")
print(num)
