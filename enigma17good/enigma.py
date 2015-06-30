__author__ = 'pconn'


#this wiring is hard coded for now but i will make a file reader for this later

rotor_wiring = { "I" : "EKMFLGDQVZNTOWYHXUSPAIBRCJ",
"II" : "AJDKSIRUXBLHWTMCQGZNPYFVOE",
"III" : "BDFHJLCPRTXVZNYEIWGAKMUSQO" }
reflector_wiring = { "B" : "YRUHQSLDPXNGOKMIEBFZCWVJAT" }
alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

#make some dictionaries for the rotors and reflectors

rotor_forward = {}
reflector = {}
rotor_reverse = {}

#put the values into the forward rotors from the wiring dictionary


for i in rotor_wiring:
    rotor_forward[i] = []
    for j in rotor_wiring[i]:
        rotor_forward[i].append(alphabet.index(j))

for i in reflector_wiring:
    reflector[i] = []
    for j in reflector_wiring[i]:
        reflector[i].append(alphabet.index(j))

for i in rotor_wiring:
    rotor_reverse[i] = []
    for j in alphabet:
        revchar = alphabet[rotor_wiring[i].index(j)]
        rotor_reverse[i].append(alphabet.index(revchar))



for i in range(0, 26):
    print(alphabet[i],
          str(rotor_forward['III'][i]).rjust(3),
          str(rotor_forward['II'][i]).rjust(3),
          str(rotor_forward['I'][i]).rjust(3),
          str(reflector["B"][i]).rjust(3),
          str(rotor_reverse['I'][i]).rjust(3),
          str(rotor_reverse['II'][i]).rjust(3),
          str(rotor_reverse['III'][i]).rjust(3),
          alphabet[i],i)


rotor_forward["III"].append(rotor_forward["III"].pop(0))
rotor_reverse["III"].append(rotor_reverse["III"].pop(0))

print("")

for i in range(0, 26):
    print(alphabet[i],
          str(rotor_forward['III'][i]).rjust(3),
          str(rotor_forward['II'][i]).rjust(3),
          str(rotor_forward['I'][i]).rjust(3),
          str(reflector["B"][i]).rjust(3),
          str(rotor_reverse['I'][i]).rjust(3),
          str(rotor_reverse['II'][i]).rjust(3),
          str(rotor_reverse['III'][i]).rjust(3),
          alphabet[i],i)

#fix this
charin = "A"

letter_position = alphabet.index(charin)

print(letter_position, alphabet[letter_position], 'goes in')

letter_position = (letter_position + rotor_forward['III'][letter_position]) %26
print(letter_position, alphabet[letter_position])
letter_position = (rotor_forward['II'][letter_position]) %26
print(letter_position, alphabet[letter_position])
letter_position = (rotor_forward['I'][letter_position]) %26
print(letter_position, alphabet[letter_position])
letter_position = (reflector["B"][letter_position]) %26
print(letter_position, alphabet[letter_position])
letter_position = (rotor_reverse['I'][letter_position]) %26
print(letter_position, alphabet[letter_position])
letter_position = (rotor_reverse['II'][letter_position]) %26
print(letter_position, alphabet[letter_position])
letter_position = (rotor_reverse['III'][letter_position]) %26
print(letter_position, alphabet[letter_position], 'comes out')




rotor_forward["III"].append(rotor_forward["III"].pop(0))
rotor_reverse["III"].append(rotor_reverse["III"].pop(0))


charin = "A"

letter_position = alphabet.index(charin)

print(letter_position, alphabet[letter_position], 'goes in')

letter_position = (letter_position + rotor_forward['III'][letter_position]) %26
print(letter_position, alphabet[letter_position])
letter_position = (rotor_forward['II'][letter_position]) %26
print(letter_position, alphabet[letter_position])
letter_position = (rotor_forward['I'][letter_position]) %26
print(letter_position, alphabet[letter_position])
letter_position = (reflector["B"][letter_position]) %26
print(letter_position, alphabet[letter_position])
letter_position = (rotor_reverse['I'][letter_position]) %26
print(letter_position, alphabet[letter_position])
letter_position = (rotor_reverse['II'][letter_position]) %26
print(letter_position, alphabet[letter_position])
letter_position = (rotor_reverse['III'][letter_position]) %26
print(letter_position, alphabet[letter_position], 'comes out')