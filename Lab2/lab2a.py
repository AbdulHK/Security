#Abdulellah Hakim
#D12122837
#Lab2 answers

#question 1
def caesar(s,k,decrypt=False):
	if decrypt: k=26 - k
	r=""
	for i in s:
			if(ord(i) >= 65 and ord(i) <= 90 ):
					r+=chr((ord(i) - 65 + k ) % 26 + 65 )
			elif(ord(i) >= 97 and ord(i) <= 122 ):
					r+=chr((ord(i) - 97 + k ) % 26 + 97 )
			else:
					r+=i
	return r
	
def encrypt(p,k):
		return caesar(p,k)

def decrypt(c,k):
		return caesar(c,k,True)

print("Caesar Cipher")
#msg  plain text
m="And I shall remain satisfied, and proud to have been the first who has ever enjoyed the fruit of his writings as fully as he could desire;for my desire has been no other than to deliver over to the detestation of mankind the false and foolish tales of the books of chivalry,which, thanks to that of my true Don Quixote, are even now tottering, and doubtless doomed to fall for ever. Farewell."
#plaintext being encrypted
c=encrypt(m,-3)
print("\n encrypted text")

print c

print("\n decrypted text")

d=decrypt(c,-3)
print d