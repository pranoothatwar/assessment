filename = raw_input("Enter the valid file name: ")
for line in reversed(list(open(filename))):
    print(line.rstrip())
