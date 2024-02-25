hrs = input("Enter Hours:")
h = float(hrs)
rate = float(input("Enter Rate:"))
r = float(rate)
def computepay(h, r):

    if h > 40:
       return ((h-40)*(r*1.5)+(40*r))

p = computepay(h, r)
print("Pay", p)