def printNumDesc(num):
    print(num, end = ' ')
    if num > 1:
        printNumDesc(num - 1)

number = 10
printNumDesc(number)

"""
i = number

while i > 0:
    print(i, end = ' ')
    i -= 1
"""