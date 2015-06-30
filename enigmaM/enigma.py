 # this is my millionth attempt to implement enigma and i am going to get it working
 # today, the 15th of june
 
 
print('Enigma 15:')

alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

#get the wiring pattens
rotor_wiring = { "I" : "EKMFLGDQVZNTOWYHXUSPAIBRCJ",
"II" : "AJDKSIRUXBLHWTMCQGZNPYFVOE",
"III" : "BDFHJLCPRTXVZNYEIWGAKMUSQO" }


# rotor transforms according to the action of one rotor
# rotor needs 4 arguments: the character in, the rotor to use, the position and boolean 
# representing the direction, 1 is forward 0 is reverse

forward_offsets = {}
reverse_offsets = {}



for entry in rotor_wiring:
	forward_offsets
	for character in rotor_wiring[entry]:
		forward_offsets[entry].append("foo")
		
		
		
		
		
"""

def rotor(character, current_wiring, position, direction):
	global alphabet

	rotorposition = alphabet.index(position)
		
	if direction:
		letterposition = alphabet.index(character)
		letterposition = (letterposition + rotorposition) %26
		print(letterposition)
		return current_wiring[letterposition] 
	else:
		letterposition = current_wiring.index(character)
		letterposition = (letterposition + rotorposition) %26
		return alphabet[letterposition]
		

		


currentletter = "A"
print(currentletter)	
currentletter = rotor(currentletter,rotor_wiring['I'],"A",0)
print(currentletter)
"""