def up_low(string):
    upper = 0
    lower = 0
    for char in string:
        if char.islower():
            lower += 1
        elif char.isupper():
            upper += 1
        else:
            pass
    return('Total of Upper Case Letters', upper , 'Total of Lower Case Letters', lower)

print(up_low('Hi, MY Name iS VaneSsa. NICE to Meet yOu'))