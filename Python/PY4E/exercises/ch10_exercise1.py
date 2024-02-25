counts = dict()
lst = list()
fhand = open("mbox-short.txt")
for line in fhand:
    if line.startswith("From") and not line.startswith("From:"):
        words = line.split()
    #print(words)
        e = words[1]
        counts[e] = counts.get(e, 0) + 1
# Person with the most commits
for email, counts in list(counts.items()):
    lst.append((counts, email))
#Sort the list
    lst.sort(reverse=True)
for email, counts in lst[:1]:
    print(counts, email)




        
