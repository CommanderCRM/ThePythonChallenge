import bz2

un = 'BZh91AY&SYA\xaf\x82\r\x00\x00\x01\x01\x80\x02\xc0\x02\x00 \x00!\x9ah3M\x07<]\xc9\x14\xe1BA\x06\xbe\x084'
pw = 'BZh91AY&SY\x94$|\x0e\x00\x00\x00\x81\x00\x03$ \x00!\x9ah3M\x13<]\xc9\x14\xe1BBP\x91\xf08'

# converting to latin1 encoding, then decoding bz2 message
un_l = un.encode('latin1')
pw_l = pw.encode('latin1')

un_decomp = bz2.decompress(un_l)
pw_decomp = bz2.decompress(pw_l)

print(un_decomp, pw_decomp)