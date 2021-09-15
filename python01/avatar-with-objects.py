###
### Course: CSc 110
### Author: Christian Byrne
### Description: Avatar creation program.
###              Choose from three premade avatar templates or make 
###              a custom avatar. Custom avatar creation allows for 
###              custom hat style, eyes, hair, arm style, torso length,
###              leg length, and shoe look. Inputs are validated.
###

class makeAvatar:
    # torso height, arm character, leg height, shoe string params. makes body. void
    def postCranium(height,arms,legs,shoes):
        if int(height)+int(legs)>6:
            print("      |-X-|\n"," 0{0}|---|{0}0".format((arms + arms + arms)))
            height = int(height) - 1
        else:
            print("  0{0}|---|{0}0".format((arms + arms + arms)))
        for _ in range(int(height)):
            print("      |-X-|  ")
        print("      HHHHH")
        fillMid = " "
        fillFront = "     "
        for _ in range(int(legs)):
            print("{}///{}\\\\\\ ".format(fillFront,fillMid))
            fillMid += "  "
            fillFront = fillFront[:-1]
            if _ == int(legs)-1:
                print("{0}       {0}".format(shoes))

    # eye character and hair-T/F params. makes face. returns parent obj
    def makeFace(eye,hairStyle):
        hair = " "
        forehead = "'"
        if hairStyle == "True":
            hair = forehead = '"'
        print(('''   *|iiiiiii|*    
   *| x   x |*   
   *|   V   |*    
   *|  ~~~  |*    
   * \\_____/ *    ''').replace("*",hair).replace("x",eye).replace("i",forehead))
        return makeAvatar
    
    # hat direction param. makes hat. returns parent obj
    def makeHat(style):
        fill1 = fill2 = "    "
        if style == "left" or style == "both":
            fill1 = " ___"
        if style == "right" or style == "both":
            fill2 = "___"
        print("""       ~-~       
     /-~-~-\     
{}/_______\\{} """.format(fill1,fill2))
        return makeAvatar

class userChoice:
    def exit():
        return
    def jeff():
        makeAvatar.makeHat("both").makeFace("0","False").postCranium(5,"=",2,"#HHH#")
    def jane():
        makeAvatar.makeHat("right").makeFace("*","True").postCranium(2,"T",3,"<|||>")
    def chris():
        makeAvatar.makeHat("front").makeFace("U","False").postCranium(3,"W",4,"<>-<>")
    def custom():
        print("Answer the following questions to create a custom avatar")
        traits = [input("Hat style ?\n"), input("Character for eyes ?\n"),\
                  input("Long hair (True/False) ?\n"),input("Arm style ?\n"),\
                  input("Torso length ?\n"), input("Leg length (1-4) ?\n"),input("Shoe look ?\n")]
        makeAvatar.makeHat(traits[0]).makeFace(traits[1],traits[2]).postCranium(traits[4],traits[3],traits[5],traits[6])


print("----- AVATAR -----")
characterSelect = input("Select an Avatar or create your own:\n")
while hasattr(userChoice, characterSelect) == False:
    characterSelect = input("Select an Avatar or create your own:\n")
getattr(userChoice, characterSelect)()

