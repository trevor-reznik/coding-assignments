###
### Course: CSc 110
### Author: Christian Byrne
### Description: Avatar creation program.
###              Choose from three premade avatar avatars or make 
###              a custom avatar. Custom avatar creation allows for 
###              custom hat style, eyes, hair, arm style, torso length,
###              leg length, and shoe look. I only used concepts I learned in class.
###              I am good student. I tried my best. Thank you.
###


def post_cranium(height,arms,legs,shoes,neck):
    '''
    Void function that prints the avatar body below the neck in accordance w/ params
    height: any integer
    arms: a single character, determines what arms are made of
    legs: integer 1-4, determines rows in legs
    shoes: 5 character string, determines the characters in the shoes
    '''
    index1=index2=0;fill_mid=" ";fill_front="     "
    if neck==1:
        print("      |-X-|\n"+" 0{0}|---|{0}0".format(arms+arms+arms+arms));height=int(height)-1
    else:
        print(" 0{0}|---|{0}0".format(arms+arms+arms+arms))
    while index1<int(height):
        print("      |-X-|  ");index1+=1
    print("      HHHHH")
    while index2<int(legs):
        print("{}///{}\\\\\\ ".format(fill_front,fill_mid))
        fill_mid+="  ";index2+=1;fill_front=fill_front[:-1]
    print("{0}       {0}".format(shoes))


def make_face(eye,hair_style):
    '''
    Void function that prints avatar head based on eye and hair_style params
    eye: a single character that determines what the eyes are made of
    hair_style: arg must be either "True" or "False". Determines if hair is present
    '''
    hair=" ";forehead="'"
    if hair_style=="True":
        hair=forehead='"'
    print(('''   *|iiiiiii|*    
   *| x   x |*   
   *|   V   |*    
   *|  ~~~  |*    
   * \\_____/ *    ''').replace("*",hair).replace("x",eye).replace("i",forehead))


def make_hat(style):
    '''
    Void function that prints a hat with direction specified by param.
    style: arg must be either "left", "front", "right", or "both". Determines hat's direction
    '''
    fill1 = fill2 = "    "
    if style == "left" or style == "both":
        fill1 = " ___"
    if style == "right" or style == "both":
        fill2 = "___"
    print("\n       ~-~       \n     /-~-~-\     \n{}/_______\\{} ".format(fill1,fill2))


def construct(style,eye,hair_style,arms,height,legs,shoes,neck):
    '''
    Just encapsulation. Accepts all traits then calls all avatar creation functions.
    Params are specificed in the above function comments
    '''
    make_hat(style); make_face(eye,hair_style); post_cranium(height,arms,legs,shoes,neck)


def custom_avatar():
    '''
    Chained method that is called when "custom" option is selected in main().
    Assigns custom_traits array elements w/ 7 input() calls then uses as args in construct() call.
    The input() params are specificed in the above function comments
    '''
    print("Answer the following questions to create a custom avatar")
    custom_traits=[input("Hat style ?\n"),input("Character for eyes ?\n"),\
            input("Long hair (True/False) ?\n"),input("Arm style ?\n"),\
            input("Torso length ?\n"),input("Leg length (1-4) ?\n"),input("Shoe look ?\n"),0]
    construct(*custom_traits)


def main():
    traits=["Jeff","both","0","False","=",5,2,"#HHH#",1,"Jane","right","*",\
            "True","T",2,3,"<|||>",0,"Chris","front","U","False","W",3,4,"<>-<>",1,"end"]
    avatar=input("Select an Avatar or create your own:\n");index=0
    while avatar!=traits[index]:
        if traits[index]=="end":    # if user didn't choose premade avatar template
             return None if avatar=="exit" else custom_avatar() if avatar=="custom" else main()
        index+=1
    construct(*traits[index+1:index+9])


print("----- AVATAR -----")
main()