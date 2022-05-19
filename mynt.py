from random import randint

inp = input('Kas kull voi kiri? ').lower()

random_number = randint(1, 2)

coin = ''
if random_number == 1:
    coin = 'kull'
else:
    coin = 'kiri'

print('tuli {}'.format(coin))

if inp == coin:
    print('voitsid')
else:
    print('kaotasid')