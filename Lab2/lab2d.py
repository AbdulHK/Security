#D12122837
#Abdulellah Hakim
# Decrypt ciphertext using Vignere cipher

from itertools import starmap, cycle
 
def decrypt(message, key):
 
    # single letter decryption.
    def dec(c,k): return chr(((ord(c) - ord(k) - 2*ord('A')) % 26) + ord('A'))
 
    return "".join(starmap(dec, zip(message, cycle(key))))
#filter will filter the inputed string and make it into one concatinated string
#.upper() will change it to uppercase 
encrypted_msg = raw_input()
encrypted_msg = filter(str.isalpha, encrypted_msg.upper())
key = "FACEBOOKPASSWORD"
#when using "FACEBOOK" as a key it shows the word Thrusday.
#when trying to brute force the next few letters using "PASS" you get July
#once I got pass I decided to try passcode, which came with no luck
#so I tried "password" and it decrypted the msg.
decrypted_msg = decrypt(encrypted_msg, key)

print "\nDecrypted message: " +decrypted_msg