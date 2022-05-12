from math import ceil

berries = int(input('Sisesta marjade kogus liitrites: '))

box_size = 0.5 * 0.3 * 0.15
box_quantity = ceil(berries / 7)
truck_size = round((box_size * box_quantity * 10 / 100), 3)

print('Marjade jaoks on vaja ' + str(box_quantity) + ' kasti')
print('Marjade jaoks on vaja kaubikut suurusega ' + str(truck_size) + ' kuupmeetrit')
