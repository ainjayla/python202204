from urllib.request import urlopen

kuu = input('Sisesta kuu (nt jaanuar): ')
paev = int(input('Sisesta paev (nt 1): '))

file = urlopen('https://robootika.digipurk.ee/wp-content/uploads/2021/06/' + kuu + '.txt')
content = file.read().decode()
names = content.splitlines()
file.close()

print('Kuupaeval', paev, kuu, 'on nimepaev jargmistel inimestel:', names[paev - 1])