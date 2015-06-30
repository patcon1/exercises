__author__ = 'pconn'


# this is not the best but it is adequate for now
# create a list of lists containing the letters in wiring.txt
# I will create something to say what they are later
# but for now:
# line 1; alphabet, lines 2-4 are rotors I to III and line 5 is reflector thick B
wiringlist = []
positionlist = []

wiringfile = open('wiring.txt', "r")
for i in range(0, 5):
    positionlist.append(['A'])
    wiringlist.append([])
    thisline = wiringfile.readline()
    for letter in thisline:
        if letter == " ":
            break
        else:
            wiringlist[i].insert(0,letter)

wiringfile.close()

#make the reverse lists
#this contains magic numbers fix this later
#for each of the rotors
# goes through each letter of the alphabet
# finds the index of that letter in the current rotor
# adds to the end of the reverse rotor whatever letter of the alphabet is at that index


for i in range(5,8):
    wiringlist.append([])
    positionlist.append(['A'])
    for thisletter in wiringlist[0]:
        wiringlist[i].append((wiringlist[0][wiringlist[i-4].index(thisletter)]))



wordsin = input('put in the input')
wordsout = ""
orderlist = [3,2,1,4,5,6,7]

for thischar in wordsin:
    print ('character in is', thischar)
    # take the item off the end and put it on the front
    wiringlist[3].insert(0, wiringlist[3].pop())
    # look up the index of the current position and move it along in the alphabet by 1
    positionlist[3][0] = chr(65 + ((ord(positionlist[3][0])-64)%26))

    #do both of these operations again for the reverse rotor
    wiringlist[7].insert(0, wiringlist[7].pop())
    positionlist[7][0] = chr(65 + ((ord(positionlist[7][0])-64)%26))

    for rotor in orderlist:
        thischarindex = ord(thischar)-65
        rotoroffset = ord(positionlist[rotor][0])-65

        thischar = wiringlist[rotor][(thischarindex+rotoroffset)%26]
        print(thischar)
    wordsout += thischar

print ('words out are', wordsout)

# Print out the rotors and the reflector
print("rotors")

for j in range(0, len(wiringlist)):
    print("",j, end="")
print("")

for i in range(0,len(wiringlist[0])):
    print(i, end = "")
    for j in range(0, len(wiringlist)):
        print("",wiringlist[j][i], end="")
    print("")

print('Rotor Positions')
for i in range(0,len(wiringlist)):
    print("",positionlist[i][0], end="")
