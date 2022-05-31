from Koer import *
from TeenistusKoer import *

print('Koigi koerte nina on', Koer.nina)

rex = Koer('Rex')
#rex.nina = 'kuiv'
pontu = Koer('Pontu')

rex.haugu()
pontu.haugu()

rex.muuda_nime('Muri')
rex.haugu()

print('Aga', rex.tagasta_nimi(), 'nina on', rex.nina)

print('Mis Su nimi on?', pontu.tagasta_nimi())


print(rex)
print(pontu)

print(rex == pontu)

liitkoer = rex + pontu
print(liitkoer)

pitsu = TeenistusKoer('Pitsu')
pitsu.jahi()
pitsu.haugu()
print(pitsu)
