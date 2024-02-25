file = input("Enter a file name: ")
try:
    inp = open(file)
except:
    print("Enter another filename", inp)
for line in inp:
    line = line.rstrip().upper()
    print(line)