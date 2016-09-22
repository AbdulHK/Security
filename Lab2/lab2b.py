#Abdulellah Hakim
#D12122837
#Lab2 answers
#question 2
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

def decrypt(c,k):
		return caesar(c,k,True)

run=True
key=0
i=0
text="Vg jbhyq frrz gung, nf ur rknzvarq gur frireny cbffvovyvgvrf, n fhfcvpvba pebffrq uvf zvaq: gur zrzbel bs ubj ur uvzfrys unq orunirq va rneyvre qnlf znqr uvz nfx jurgure fbzrbar zvtug or uvqvat ure sebz gur jbeyq"
#brute force and try it with diffrent keys.

while run:
	#loop will keep going until the user presses Y or Y. displaying the text to the user.
	print decrypt(text,i)
	ans=raw_input("is this the key? y/n")
	if (ans == "Y" or ans == "y" ):
	 	key=i
	 	run=False
	else:
	 	i+=1 
print("the key is : ", key)

