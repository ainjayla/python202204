pikkus = float(input('Sisesta inimese pikkus (cm): '))
kaal = float(input('Sisesta inimese kaal (kg): '))

print('Inimese kehamassiindeks on', round(kaal / (pikkus / 100) ** 2, 2))