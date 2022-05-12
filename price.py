pricelist = {'piim': 1.3, 'leib': 2, 'vorst': 3.6}

product = input('Sisesta toote nimi: ').lower()

# Variant 2
print('Toote', product, 'hind on', pricelist[product], 'eurot') \
    if product in pricelist \
    else print('Sellist toodet meil pole')

# Variant 1
#if product in pricelist:
#    print('Toote', product, 'hind on', pricelist[product], 'eurot')
#else:
#    print('Sellist toodet meil pole')

"""
if product == 'piim':
    print(pricelist['piim'])
elif product == 'leib':
    print(pricelist['leib'])
elif product == 'vorst':
    print(pricelist['vorst'])
else:
    print('Sellist toodet meil pole')
"""
