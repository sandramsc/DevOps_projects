count = 0
total = 0
avg = 0
#wrap entire function in while loop
while True:
    #prompt user for input
    line = input('Enter a number: ')
    try:
        if line == 'done':
            break
        print(line)
        #function formulars for total, count, avg
        total = total + int(line)
        count = int(count) + 1
        avg = total / count
    except:
        print('Invalid input')
        continue
#print function results
print(total, count, avg)





