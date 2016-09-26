#D12122837
#Abdulellah Hakim
# Encrypts ciphertext using Vignere cipher

from itertools import starmap, cycle
 
def encrypt(message, key):
 #converts to uppercase and remvoes all non alphabetic digits
    message = filter(str.isalpha, message.upper())
    # single letter encrpytion.
    def enc(c,k): return chr(((ord(k) + ord(c) - 2*ord('A')) % 26) + ord('A'))
 
    return "".join(starmap(enc, zip(message, cycle(key))))

#plain text:I shall (from now on) select and take the ingots individually in my own yard, 
#and I shall exercise against you my right of rejection because you have treated me with contempt.

msg = raw_input("Input String: ")
key = "PASSWORD"

emsg = encrypt(msg, key)

print msg
print emsg 