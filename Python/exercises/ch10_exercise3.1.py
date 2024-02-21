import string

counts = dict()
lst = list()
fhand = open("lorem.txt")
for line in fhand:
     line = line.translate(str.maketrans("","",string.punctuation))
     line = line.lower()
     w = line.split()
     lst.extend(w)

letter_list = []
for word in lst:
    letter_list.extend(list(word))
    #print(letter_list)
for i in letter_list:
    if i not in counts:
        counts[i] = 1
    else:
        counts[i] += 1
# Create tuples and sort in decreasing order
final_list = []
for k,v in list(counts.items()):
    final_list.append((v,k))
    final_list.sort(reverse =True)
for k,v in final_list:
    print(k,v)
