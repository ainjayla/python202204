

max_number = input('Sisesta number, milleni leitakse taisarvulised paaris numbrid: ')

if max_number.isdigit():
    max_number = int(max_number)
    for i in range(0, max_number + 1):
        if i >= 50:
            break
        if i % 2 == 1 or i == 0:
            continue
        print(i, end = ' ')
else:
    print('Sa ei sisestanud numbrit!')