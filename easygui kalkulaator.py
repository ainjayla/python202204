from easygui import *

first_num = integerbox('Sisesta esimene number (1-120):', title='Esimene number', lowerbound=1, upperbound=120)
second_num = integerbox('Sisesta teine number (1-120):', title='Teine number', lowerbound=1, upperbound=120)

operations = ['+', '-', '/', '*']
chose = buttonbox('Vali tehe', title='Tehted', choices=operations)

total = 0
if chose == '+':
    total = first_num + second_num
elif chose == '-':
    total = first_num - second_num
elif chose == '/':
    total = first_num / second_num
elif chose == '*':
    total = first_num * second_num

msgbox('Tehte tulemus on: ' + str(total))
