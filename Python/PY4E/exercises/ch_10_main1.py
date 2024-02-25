counts = dict()
lst = list()
fhand = open("mbox-short.txt")
for line in fhand:
    if line.startswith("From") and not line.startswith("From:"):
        words = line.split()
        h = words[5]
        ht = h.split(":")
        hour = ht[0]
        lst.append(hour)
        
#for loop outside any other loop before it enables function to iterate and print only once       
for i in lst:
    counts[i] = counts.get(i, 0) + 1
    t = sorted(counts.items())
for k, v in sorted(counts.items()):
    print(k,v)
