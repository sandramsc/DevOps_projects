hrs = float(input("Enter Hours:"))
rate = float(input("Enter Rate:"))
if hrs > 40:
    print((hrs - 40) * (rate * 1.5) + (40 * rate))