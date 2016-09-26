def Vcipher(msg, key):
	crypt = ''
	crypt2 = ' '
	decrypt = ''
	for n in range(0, len(msg)):
		new = ord(msg[n]) + ord(key[n%len(key)]) - 65
		if new > 90:
			new -= 26
		crypt = crypt +  chr(new)
		new = ord(msg[n]) - ord(key[n%len(key)]) + 65
		
		if new < 65:
			new+= 26
		decrypt = decrypt +  chr(new)
		
	for n in range(0, len(crypt)):
		new = ord(crypt[n]) + ord(key[n%len(key)]) - 65
		if new > 90:
			new -= 26
		else:
			new += 1
			
		crypt2 = crypt2 +  chr(new)
		new = ord(crypt[n]) - ord(key[n%len(key)]) + 65
		
		if new < 65:
			new+= 26
		decrypt = decrypt +  chr(new)
		
	return crypt, decrypt

str3 = "Yhwvtroi, 28 Yudq 2016Pse bjatw pt foxgf zwjzql bgio qcwelwlar, blsg rmprochek ewrv nsoyr uvs ndcljebv rk pkium hy bef; sjr wutm vljg aybefl ds ydx mchf asx bojw lwfxx, aph fjsbntzaju kkwixit hvbduyzkik wme ylpzs gdrdv. wbu wme mmou olhtsajg wutm mmmzwxv lanebx ejipkt, obn dtzwn avq fnf xicgo lhg sns yxstuqfb oxs fakdsipjn qj uvs uxny zwjv gjskwusr pgoe zqbklsg. cre wt cdmw oafv lstgqqsfkie, lzam ydae eibgsn urge pvvlw ipxfadogafua oj zfs kr uvssg pgoaf; rqi odiewsxi tg ldszu kavlff oxs mgldsi dsd vs uvs oadwjo, we rupqwjhwyc tg lds gdxt cptc wx ihw xqhluj, ba wp oqdxny gj smhwy qgdogsdn, lzam nlql nmws poitwj wbu ptrg lbddsay"

k = " "

while k < 90 and k > 10 :
	k = k + 1
	Vcipher(str3, k)
	if "a" or "Thursday" in str3:
		print str3
		
print k