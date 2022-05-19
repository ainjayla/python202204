file = open('visits.csv', encoding = 'UTF-8')

visits = {}

for row in file:
    pair = row.strip('\ufeff').strip().split(',')
    visits[pair[0]] = int(pair[1])

maximum = 0
maximum_key = ''

for visit in visits:
    if visits[visit] > maximum:
        maximum = visits[visit]
        maximum_key = visit

print('Koige rohkem kylastajaid oli {}, siis kylastas loodusparki {} inimest'.format(maximum_key, maximum))

file.close()