import re
count = 0
lst = []
inp = input("Enter a regex: ")
rx = str(inp)
fh = open("mbox-short.txt")
fr = fh.readlines()
for line in fr:
    line = line.rstrip()
    if len(line) > 0:
        word = line.split()
        lst.extend(word)
        r = re.findall(str(rx), str(lst))
        count = len(r)
print("mbox.txt had", count, "lines that matched", rx)
