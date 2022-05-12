import sys

number = int(sys.argv[1]) \
    if len(sys.argv) >= 2 and sys.argv[1].isdigit() \
    else None

# number = int(input('Sisesta mingi taisarv: '))

print('paaris' if number % 2 == 0 else 'paaritu') \
    if number is not None \
    else print('puudub sisend')

"""
if number is not None:
    if number % 2 == 0:
        print('paaris')
    else:
        print('paaritu')
else:
    print('puudub sisend')
"""