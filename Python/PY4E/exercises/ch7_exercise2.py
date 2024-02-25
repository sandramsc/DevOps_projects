file = input("Enter a file name: ")
count = 0
total = 0
avg = 0

try:
    inp = open(file)
    for line in inp:
        line = line.rstrip()
        if line.startswith("X-DSPAM-Confidence:"):
            #get the integr from the string
            p = float(line[20:27])
            count += 1
            total = total + float(p)
            avg = total / count
except:
    print("Enter another filename:", file)
    exit()
print("Average spam confidence: ", avg)

