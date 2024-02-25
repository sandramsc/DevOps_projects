str = "X-DSPAM-Confidence:0.8475"
pos = str.find(":")
ppos = str.find("5",pos)
slice = str[pos+1:ppos+1]
print(float(slice))