
inputtext = input("put in some text")

outputtext = inputtext[0]


outputtext = chr(65 + ((ord(outputtext)-64)%26))

print(outputtext)



"""
__author__ = 'pconn'


rawinputtext = input("please put in the text to be enciphered")
inputtext = rawinputtext.upper()
inputtext = inputtext.replace(" ", '')

print("the input text to be enciphered is", inputtext)



for letter in inputtext:
    print(rotor1[alphabet.index(letter)])
    rotor1.insert(0,rotor1.pop())
    input ('continue')


##dont think this is right



# take input from the user and set the current letter to the first one (iterate
# through the whole message later)

inputtext = input("enter text")
inputtext = inputtext.upper()
inputtext = inputtext.replace(" ", "")

currentletter = inputtext[0]

#the first rotor:
# find the position of currentletter in the alphabet with wiringlist[0].index()
#then set currentletter to that index in wiringlist[1], the first rotor



# Advance the rotor
#wiringlist[3].append(wiringlist[3].pop(0))
#wiringlist[3].insert(0,wiringlist[3].pop())

print (currentletter, end="")


currentletter = wiringlist[3][wiringlist[0].index(currentletter)]
print (currentletter, end="")


currentletter = wiringlist[2][wiringlist[0].index(currentletter)]
print (currentletter, end="")


currentletter = wiringlist[1][wiringlist[0].index(currentletter)]
print (currentletter, end="")

# Reflector here

currentletter = wiringlist[4][wiringlist[0].index(currentletter)]
print (currentletter, end="")

#logic changes on the reverse: it finds what is the index of the current letter in the rotor and then
#appends the letter of the alphabet with that index

currentletter = wiringlist[0][wiringlist[1].index(currentletter)]
print (currentletter, end="")

currentletter = wiringlist[0][wiringlist[2].index(currentletter)]
print (currentletter, end="")


currentletter = wiringlist[0][wiringlist[3].index(currentletter)]
print (currentletter)


outputtext = "the first character enciphered is: " + currentletter
print(outputtext)

"""


#

# print("Input".rjust(2), 'Rotor 1 '.rjust(7))

# for i in range(0,25):
#     print(alphabet[i].rjust(2), rotor1[i].rjust(7))

