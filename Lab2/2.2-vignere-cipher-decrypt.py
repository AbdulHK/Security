# Date created: 2016-09-20
# Contents: Decrypt ciphertext using Vignere cipher

from itertools import starmap, cycle
 
def decrypt(message, key):
 
    # single letter decryption.
    def dec(c,k): return chr(((ord(c) - ord(k) - 2*ord('A')) % 26) + ord('A'))
 
    return "".join(starmap(dec, zip(message, cycle(key))))


#encrypted string is " Yhwvtroi, 28 Yudq 2016 ­ Pse bjatw pt foxgf zwjzql bgio qcwelwlar, blsg rmprochek ewrv nsoyr uvs ndcljebv rk pkium hy bef;
#sjr wutm vljg aybefl ds ydx mchf asx bojw lwfxx, aph fjsbntzaju kkwixit hvbduyzkik wme ylpzs gdrdv. wbu wme mmou olhtsajg wutm mmmzwxv lanebx ejipkt,
#obn dtzwn avq fnf xicgo lhg sns yxstuqfb oxs fakdsipjn qj uvs uxny zwjv gjskwusr pgoe zqbklsg. cre wt cdmw oafv lstgqqsfkie, lzam ydae eibgsn urge 
#pvvlw ipxfadogafua oj zfs kr uvssg pgoaf; rqi odiewsxi tg ldszu kavlff oxs mgldsi dsd vs uvs oadwjo, we rupqwjhwyc tg lds gdxt cptc wx ihw xqhluj, 
#ba wp oqdxny gj smhwy qgdogsdn, lzam nlql nmws poitwj wbu ptrg lbddsay"
msg = raw_input("Input String: ").replace(" ","")
#removing non alpha characters
msg = filter(str.isalpha, msg.upper())
key = "FACEBOOKPASSWORD"

dmsg = decrypt(msg, key)

print "Encrypted message: " + msg 
print "\nDecrypted message: " +dmsg