pikkus = float(input('Sisesta inimese pikkus (cm): '))
kaal = float(input('Sisesta inimese kaal (kg): '))

bmi = round(kaal / (pikkus / 100) ** 2, 2)

print('Inimese kehamassiindeks on', bmi)

if bmi < 16:
    print('Tervisele ohtlik alakaal')
elif 16 <= bmi < 19:
    print('Alakaal')
elif 19 <= bmi < 25:
    print('Normaalkaal')
elif 25 <= bmi < 30:
    print('Ylekaal')
elif 30 <= bmi < 35:
    print('Rasvumine')
elif 35 <= bmi < 40:
    print('Tugev rasvumine')
elif 40 <= bmi:
    print('Tervisele ohtlik rasvumine')
