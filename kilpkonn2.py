from turtle import *

file = open('kasud.txt', encoding = 'UTF-8')

for row in file:
    command = row.strip().split(',')
    if command[0] == 'otse':
        forward(int(command[1]))
    elif command[0] == 'paremale':
        right(int(command[1]))
    elif command[0] == 'vasakule':
        left(int(command[1]))
    print(command)

done()

file.close()