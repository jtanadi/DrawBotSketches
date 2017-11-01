"""
Temp. file, grabbed from https://github.com/thundernixon/drawbot/blob/master/experiments/type_alphabet_weight_test-110117.py
"""

Variable([
    dict(name="customString", ui="TextEditor"),
    dict(name="lockXHeight", ui="CheckBox"),
    dict(name="fontSize1", ui="Slider",
            args=dict(
                value=100,
                minValue=75,
                maxValue=125)),
    dict(name="fontSize2", ui="Slider",
            args=dict(
                value=100,
                minValue=75,
                maxValue=125)),
    dict(name="fontSize3", ui="Slider",
            args=dict(
                value=100,
                minValue=75,
                maxValue=125)),
    dict(name="fontColor1", ui="ColorWell"),
    dict(name="fontColor2", ui="ColorWell"),
    dict(name="fontColor3", ui="ColorWell"),
    ], globals())

defaultFontColor1 = [.75,0,.75]

print "font size 1 is " + str(fontSize1) + " pt"
print "font size 2 is " + str(fontSize2) + " pt"
print "font size 3 is " + str(fontSize3) + " pt"

size('A3')

fontSize(100)
fallbackFont("Arial")

counter = 1


################# 😺 TRIPLES LETTERS IN YOUR STRING, THEN SETS THEM AS TEXT 😺 #################
def testWeights(string):
    counter = 1
    lineCount = 1
    textWidth = 0
    starterPosX = 50
    starterPosY = 120
    positionX = starterPosX
    positionY = height()-150
    newString = ""
    for char in string:
        newString += char*3

    for char in newString:
        if counter % 3 == 0:
            fill(fontColor3)
            fontSize(fontSize3)
            font("Times New Roman") ################# ✅ REPLACE WITH YOUR HIGH CONTRAST FONT ✅ #################
            
            if lockXHeight:
                fontSize(fontSize3 * ratio3)

        elif (counter + 1) % 3 ==0:
            fill(fontColor2)
            fontSize(fontSize2)
            font("Courier") ################# ✅ REPLACE WITH YOUR REGULAR CONTRAST FONT ✅ #################

            if lockXHeight:
                fontSize(fontSize2 * ratio2)

        else:
            fill(fontColor1)
            fontSize(fontSize1)
            font("Helvetica") ################# ✅ REPLACE WITH YOUR LOW CONTRAST FONT ✅ #################

        text(char, (positionX, positionY))
        letterWidth, letterHeight = textSize(char)
        
        textWidth += letterWidth
        positionX += letterWidth
        
        if counter % 3 == 0:
            letterWidth, letterHeight = textSize(" ")
            positionX += letterWidth + 10
        
        if counter % 9 == 0:
            lineCount += 1
            positionX = starterPosX
            positionY -= starterPosY

        counter += 1
                
        # to do: if letter doesn't exist in the supplied font, replace with "n" or some other user-defined string

def calcXHeight():
    #font1
    fontSize(fontSize1)
    font("Helvetica")

    xHeight1 = fontXHeight()
    
    #font2
    fontSize(fontSize2)
    font("Courier")

    xHeight2 = fontXHeight()

    #font3
    fontSize(fontSize3)
    font("Times New Roman")
    xHeight3 = fontXHeight()

    global ratio2, ratio3
    ratio2 = xHeight1 / xHeight2
    ratio3 = xHeight1 / xHeight3


################# ✅ MAKE YOUR STRING HERE, THEN SET AS AN ARGUMENT IN FUNCTION CALL ✅ #################
import string
alpha = string.lowercase
heylook = "testyerfonts"
calcXHeight()
if customString != "":
    
    testWeights(customString) # use your string as an argument
else:
    testWeights(alpha)

################# 😺 SAVE AS A PDF IF YOU'D LIKE TO PRINT 😺 #################
# saveImage("give-it-a-title.pdf")