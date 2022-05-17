colors = []
inp = ''

while True:
    inp = input('Sisesta mingi varv voi \'x\' lopetamiseks: ')
    if inp == 'x':
        break
    if inp in colors:
        continue
    colors.append(inp)

i = 0
while i < len(colors):
    print(colors[i])
    i += 1