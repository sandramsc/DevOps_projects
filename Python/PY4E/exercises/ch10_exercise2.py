counts = dict()
lst = list()
fhand = open("mbox-short.txt")
for line in fhand:
    if line.startswith("From") and not line.startswith("From:"):
        words = line.split()
        hrs = words[5]
        hr = hrs.split(":")
        h = hr[0]
        counts[h] = counts.get(h, 0) + 1
        #print(counts)
for k,v in list(counts.items()):
   lst.append((k,v))
   lst.sort(reverse=True)
for k,v in lst:
   print(k,v)
