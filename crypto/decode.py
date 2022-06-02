import sys
from Crypto import *
from easygui import *

crypto = Crypto(sys.argv[1])

filename = fileopenbox('Avamine')

file = open(filename, encoding = 'UTF-8')
encoded_message = file.read()
message = crypto.decode(encoded_message)
msgbox(message, 'Dekrupteerimine')

file.close()
