text = input('Sisesta mingi lobus tervitus: ')
count = input('Sisesta mitu korda seda kuvatakse: ')

if count.isdigit():
    count = int(count)
    i = 0
    while i < count:

        print(str(i + 1) + '. kord:', text.upper())
        i += 1
else:
    print('Sa ei sisestanud numbrit!')