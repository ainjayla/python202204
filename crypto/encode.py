import sys
from Crypto import *
from easygui import *

crypto = Crypto(sys.argv[1])

#file = open(sys.argv[2], encoding = 'UTF-8')
#message = file.read()

message = textbox('Sisesta tekst mida soovid krupteerida', 'Krupteerimine')

decoded_message = crypto.encode(message)

filename = filesavebox('Salvestamine')

file2 = open(filename, 'w', encoding = 'UTF-8')
file2.write(decoded_message)
file2.close()
#file.close()