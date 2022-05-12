number = input('Sisesta mingi taisarv: ')

# Variant 2
result = int(number) \
    if number.isdigit() \
    else None
print('Tulemus on ' + str(int(((result + (result + 1) + 9) / 2) - result)) \
          if result is not None \
          else 'Sa ei sisestanud numbrit')

# Variant 1
"""
if number.isdigit():
    result = int(number)
    result += result + 1
    result += 9
    result /= 2
    result -= int(number)
    print('Tulemus on', int(result))
else:
    print('Sa ei sisestanud numbrit')
"""