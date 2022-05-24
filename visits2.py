#def x(l):
#    return int(l[1])

file = open('visits.csv', encoding = 'UTF-8')

visits = []

for row in file:
    visit = row.strip('\ufeff').strip().split(',')
    visits.append(visit)

visits.sort(key = lambda l: int(l[1]), reverse = True)
print(visits)

print('Koige rohkem kylastajaid oli {}, siis kylastas loodusparki {} inimest'.format(visits[0][0], visits[0][1]))

file.close()