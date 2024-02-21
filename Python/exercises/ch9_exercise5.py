counts = dict()
lst = list()
fhand = open("mbox-short.txt")
fh = fhand.readlines()
for line in fh:
  lines = line.rstrip()
  if line.startswith("From") and not line.startswith("From:"):
    words = line.split()
    #print(words)
    email = words[1]
    #print(email)
    e_split = email.split('@')
    #print(e_split)
    domain = e_split[1]
    #print(domain)
    lst.append(domain)
    #print(lst)
    for i in lst:
        if i not in counts:
            counts[i] = 1
        else:
            counts[i] += 1
print(counts)
