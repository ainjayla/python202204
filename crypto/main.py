import sys
from Crypto import *

keyfile = sys.argv[1]
crypto = Crypto(keyfile)

# Bob koostab sonumi ja saadab krupteeritult Alicele
message = 'VOTI ON MATI ALL'
encoded = crypto.encode(message)
print('Bob:', encoded)

# Alice saab krupteeritud sonumi ja avab selle
decoded = crypto.decode(encoded)
print('Alice:', decoded)
