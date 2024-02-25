min = None
max = None
# wrap entire function in while loop
while True:
    # prompt user for input
    line = input('Enter a number: ')
    try:

        if line == 'done':
            break
        print(line)
        #convert use input integer
        line = int(line)
        # min and max
        if min is None or line < min:
            min = line
            # print("min",min)
        if max is None or line > max:
            max = line
            # print("max",max)

    except ValueError:
        print('Invalid input')
        continue
# print function results
print("max is", max)
print("min is", min)
