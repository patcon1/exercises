

### 23RD OF JUNE 2015
# GOING TO SHELF THIS ONE FOR A WHILE
# ITS WORKING PRETTY WELL, THERE ARE 2 BUGS APPARENT:
# THE STEPPING OF THE SECOND ROTOR HAPPENS ONE CHARACTER LATE OPGNDXVQOCWJOXSFEZKSMISULUGOQWGHQXLMWVATTNMGW -->
# THISISSOMECYPHERTEXTLSLIGHTLYLONGERCYPHERTEXT THE FIRST L IS SUPPOSED TO READ 'A'
# ALSO THE CHECK TO STEP A ROTOR DOESNT JUST HAPPEN IF THE ONE TO THE RIGHT IS STEPPED,
# IT MIGHT GET STEPPED IF THE INITIAL SETTING IS THE STEP POSITION WHICH WOULD BE INCORRECT
# I ALSO WISH TO PUT IN TEXT INPUT (EASY) STECKERBRETT (DONT KNOW) AND THE RINGSTELLUNG (CONFUSING BUT PROBABLY NOT
# TOO HARD!)



# I should put these into a file I think.

alphabet_string = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

rotor_wiring = { "I" : "EKMFLGDQVZNTOWYHXUSPAIBRCJ",
"II" : "AJDKSIRUXBLHWTMCQGZNPYFVOE",
"III" : "BDFHJLCPRTXVZNYEIWGAKMUSQO",
"IV" : 'ESOVPZJAYQUIRHXLNFTGKDCMWB',
'V' : 'VZBRGITYUPSDNHLXAWMJQOFECK'}

rotor_stepping = { "I" : "Q",
"II" : "E",
"III" : "V",
"IV" : 'J',
'V' : 'Z'}

reflector_wiring = {
    'A' : "EJMZALYXVBWFCRQUONTSPIKHGD",
    "B" : "YRUHQSLDPXNGOKMIEBFZCWVJAT",
    'C' : 'FVPJIAOYEDRZXWGCTKUQSBNMHL'}





# make uppercase and assign a number to each letter 0-25
# if direction is 1 then go from letter to number if 0 number to letter
def letter_number_swapper(toswap, direction):

    if direction:

        toswap = toswap[0].upper()
        if toswap in alphabet_string:
            return alphabet_string.index(toswap)
        else:
            print("letter number swapping error, character not in alphabet")
    else:
        toswap = int(toswap)
        if toswap >=0 and toswap <=25:
            return alphabet_string[toswap]
        else:
            print('letter number swapping error, number out of range of alphabet')



# rotor and reflector functions are teh guts of the machine
def rotor (char_in, rotor_choice, position_in, direction):

    #turn the letter in into a number
    letter = letter_number_swapper(char_in, 1)

    #turn the position into a number
    position = letter_number_swapper(position_in, 1)

    if direction:
        #combine the position of the rotor and the input letter- this determines which input goes hot
        letter = (position + letter ) % 26

        # the letter that comes out of the rotor

        letter = letter_number_swapper(rotor_wiring[rotor_choice][letter], 1)

        # what is the final position of that letter where it comes out of the rotor
        letter = (letter - position) % 26


    else:

        # update the letter according to the position
        letter = (letter + position) % 26


        #which position/index in rotor wiring corresponds to that letter?
        #(equivalent of moving in teh reverse direction)
        letter = rotor_wiring[rotor_choice].index(alphabet_string[letter])

        #what is the output position of that letter?
        letter = (letter - position ) % 26


    return letter_number_swapper(letter,0)


def reflector(charin, reflector_choice):
    #change the character in to a number
    letter = letter_number_swapper(charin,1)

    #it's creepy to change the type like this i think
    letter = reflector_wiring[reflector_choice][letter]
    return letter



# take inputs from the user
def getinputs(testmode):
    global rotor_left, rotor_mid, rotor_right, reflect, rotorposition

    if testmode:
        rotor_left, rotor_mid, rotor_right, reflect, rotorposition = "I", "II","III",'B',['A','A','A']
    else:
        i = 0
        romnum = ['I','II', "III",'IV','V']

        #get the wiring pattern to use
        print("No.", 'Rotor'.ljust(5), 'Wiring Pattern'.rjust(15))
        print("---------------------------")
        for numeral in romnum:
            i += 1
            print(str(i)+ '. ', numeral.ljust(4), rotor_wiring[numeral].rjust(28))
        rotorsin = (input("Enter the 3 rotors (as arabic numerals) separated by commas, [enter] for default"))

        if rotorsin != "":
            rotorsin = rotorsin.split(',')
            rotor_left, rotor_mid, rotor_right = int(rotorsin[0])-1, int(rotorsin[1])-1, int(rotorsin[2])-1
            rotor_left = romnum[rotor_left]
            rotor_mid = romnum[rotor_mid]
            rotor_right = romnum[rotor_right]

            print('using:', rotor_left, rotor_mid, rotor_right)
        else:
            rotor_left = "I"
            rotor_mid = "II"
            rotor_right = "III"
            print("using default rotors of I, II, III")

        #get the reflector to use
        print("Reflector", 'Wiring Pattern'.rjust(15))
        print("---------------------------")
        for letter in ['A','B','C']:
            print(letter.ljust(10), reflector_wiring[letter])
        reflect = (input("enter the reflector to use. [enter] for default"))
        if reflect == "A" or reflect == "B" or reflect == "C":
            print('reflector is: ', reflect)
        else:
            reflect = 'B'
            print('using default', reflect)

        #get the start position
        rotorin = input("enter the start positions of the rotors, enter for default")
        rotorposition = ['A','A','A']
        if rotorin == "":
            print('using default AAA')
        else:
            rotorposition[0], rotorposition [1], rotorposition[2] = rotorin[0], rotorin[1], rotorin[2]

        print('rotor position is:', rotorposition)
    return "doneski"


def nextletter(letterin):
    if letterin == 'Z':
            return 'A'
    else:
        return alphabet_string[alphabet_string.index(letterin)+1]


def stepthrough():
    upto_letter = 0
    global rotorposition

    for currentcharacter in "OPGNDXVQOCWJOXSFEZKSMISULUGOQWGHQXLMWVATTNMGW":

        # Step the rightmost rotor
        #remember with the steppng- we dont want to
        #  step the rotor from initial settings only from a movement

        rotorposition[2] = nextletter(rotorposition[2])

        if rotorposition[2] == rotor_stepping[rotor_right]:
            rotorposition[1] = nextletter(rotorposition[1])

        #go through all the rotors

        currentcharacter= rotor(currentcharacter, rotor_right, rotorposition[2], 1)

        currentcharacter= rotor(currentcharacter, rotor_mid, rotorposition[1], 1)

        currentcharacter= rotor(currentcharacter, rotor_left, rotorposition[0], 1)

        currentcharacter= reflector(currentcharacter, reflect)

        currentcharacter = rotor(currentcharacter, rotor_left, rotorposition[0],0 )

        currentcharacter = rotor(currentcharacter, rotor_mid, rotorposition[1],0 )

        currentcharacter = rotor(currentcharacter, rotor_right, rotorposition[2], 0 )

        print ( currentcharacter, end="")


getinputs(1)
print('rotor_left, rotor_mid, rotor_right, reflect, rotorposition are',
      rotor_left, rotor_mid, rotor_right, reflect, rotorposition)

stepthrough()


