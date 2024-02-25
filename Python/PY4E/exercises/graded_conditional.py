inp = input('Enter score: ')

try:
    s = float(inp)
    if s >= 0.9:
        print('Grade: A')
    else:
        if s >= 0.8:
            print('Grade: B')
        else:
            if s >= 0.7:
                print('Grade: C')
            else:
                 if s >= 0.6:
                     print('Grade: D')
                 else:
                     if s < 0.6:
                        print('Grade: F')
except:
    print('Bad score')


