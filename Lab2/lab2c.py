plaintext   = raw_input("Input String: ").upper().replace(" ","")
key         = raw_input("Key: ").upper()

print(plaintext)
if len(key) == 0:
    print "Key must be of length 1 or more."; exit()
if not plaintext.isalpha() or not key.isalpha():
    print "Input and key must be composed of letters only."; exit()

crypt = ''
decrypt = ''
for n in range(0, len(plaintext)):
    new = ord(plaintext[n]) + ord(key[n%len(key)]) - 65
    if new > 90:
        new -= 26
    crypt += chr(new)
    new = ord(plaintext[n]) - ord(key[n%len(key)]) + 65
   
print "Crypted text: " + crypt
