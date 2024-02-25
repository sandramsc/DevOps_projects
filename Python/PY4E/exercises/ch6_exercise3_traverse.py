inp = input('Enter word: ')
inp2 = input('Enter letter: ')
def counnt():
    count = 0
    t = str(inp)
    s = str(inp2)
    for letter in t:
        if letter == s:
            count = count + 1
    print(count)

counnt()
