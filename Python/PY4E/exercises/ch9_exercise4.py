counts = dict()
lst = list()
max = None
total = 0
fhand = open("mbox-short.txt")
fh = fhand.readlines()
for line in fh:
  lines = line.rstrip()
  if line.startswith("From") and not line.startswith("From:"):
    words = line.split()
    email = words[1]
    #print(email)
    lst.append(email)
    print(lst)

    for e in lst:
        if e not in counts:
            counts[e] = 1
        else:
           counts[e] += 1
    #print(counts)
    #print('before:', max)
    for i in counts:
        if max is None or i > max:
            max = i
            total = 1
        elif i == max:
                total += 1
print(max, total)
