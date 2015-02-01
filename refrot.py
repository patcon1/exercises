# in this file are the dictionaries for the rotors and reflectors

# In the rotor dictionary the key is the rotor number from the wikipedia page
# Each value is a list, the first element is the wiring from A to Z and
# the second element is the turnover points if any. The reflector dictionary 
# key is the name of the reflector and the value is a list of 


rotors = {
"I" : ["EKMFLGDQVZNTOWYHXUSPAIBRCJ", "r"],
"II" : ["AJDKSIRUXBLHWTMCQGZNPYFVOE", "f"],
"III" : ["BDFHJLCPRTXVZNYEIWGAKMUSQO", "w"],
"IV" : ["ESOVPZJAYQUIRHXLNFTGKDCMWB", "k"],
"V" : ["VZBRGITYUPSDNHLXAWMJQOFECK", "a"],
"VI" : ["JPGVOUMFYQBENHZRDKASXLICTW", "AN"],
"VII" : ["NZJHGRCXMYSWBOUFAIVLPEKQDT", "AN"],
"VIII" : ["FKQHTLXOCBJSPDZRAMEWNIUYGV", "an"],
"Beta" : ["LEYJVCNIXWPBQMDRTAKZGFUHOS"],
"Gamma" : ["FSOKANUERHMBTIYCWLQPZXVGJD"],
}


reflectors = {
"B" : ["AY", "BR", "CU", "DH", "EQ", "FS", "GL", "IP", "JX", "KN", "MO", "TZ", "VW"],
"C" : ["AF", "BV", "CP", "DJ", "EI", "GO", "HY", "KR", "LZ", "MX", "NW", "TQ", "SU"],
"BD" : [ "AE", "BN", "CK", "DQ", "FU", "GY", "HW", "IJ", "LO", "MP", "RX", "SZ", "TV"],
"CD" : ["AR", "BD", "CO", "EJ", "FN", "GT", "HK", "IV", "LM", "PW", "QZ", "SX", "UY"],
}

# print("the reflector rotor data file has been executed")
