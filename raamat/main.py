import sys
from Raamat import *
from math import *

raamat = Raamat(sys.argv[1])

print('Raamatus on', raamat.getWordsCount(), 'sona')
print('Selle raamatu valjatrukiks kulub', ceil(raamat.getRowsCount() / 58 / 2), 'paberilehte')

file = open('raamat_tagurpidi.txt', 'w', encoding = 'UTF-8')
file.write(raamat.keeraYmber())
file.close()