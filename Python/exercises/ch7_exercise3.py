file = input("Enter a file name: ")
count = 0
total = 0
avg = 0

if file == "na na boo boo":
    print("NA NA BOO BOO TO YOU - You have been punk'd!")
else:
try:
    inp = open(file)

    for line in inp:
        line = line.rstrip()

        if line.startswith("X-DSPAM-Confidence:"):
            p = float(line[20:27])
            count += 1
            total = total + float(p)
            avg = total / count
except:
    print("File cannot be opened:", file)
    exit()
print("There were %d subject lines in mbox.txt " % total)

