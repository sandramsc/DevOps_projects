#inp = input('Enter score: ')
def computegrade(s):
    try:
        #s = float(inp)
        if s >= float(0.9):
            return 'Grade: A'
        else:
            if s >= 0.8:
                return 'Grade: B'
            else:
                if s >= 0.7:
                    return 'Grade: C'
                else:
                    if s >= 0.5:
                        return 'Grade: D'
                    else:
                        if s >= 0.6:
                            return 'Grade: E'
                        else:
                            if s < 0.6:
                                return 'Grade: F'
    except:
        return 'Bad score'

x = computegrade(1)
print(x)