import re
lst = []

fh = open("regex_sum_1713908.txt")
fr = fh.readlines()
for line in fr:
    line = line.rstrip()
    if len(line) > 0:
        x = re.findall("[0-9]+", line)
        lst.extend(x)
        count = len(lst)

nlst = list()
# convert the strings to integers
for i in lst:
    c = int(i)
    # create a list of integers
    nlst.append(c)
    total = sum(nlst)
print(total)
