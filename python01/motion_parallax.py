###
### Course: CSc 110
### Author: Christian Byrne
### Description: Makes landscape with parallax motion relative to mouse on tkinter canvas
###              Day/night cycle changes luminosity of objects on periodic basis.
###              Mountains are made out of random colors
###              Stars and birds in the sky with simulated motion.
###              Sun and moon on fixed orbit trajectory
###              Objects change size and position to simulate perspective of mouse position.
###


import random
from graphics import graphics
import math


def gen_random_color(gui):
    '''
    Function that can be called whenever a random color is needed
    Gets three random integers and calls gui's get_color_string method, returns result
    gui: the canvas object
    '''
    return gui.get_color_string(random.randint(0,255),random.randint(0,255),\
                                random.randint(0,255))

 
def make_birds(gui,x_position,y_parallax):
    '''
    Chain function that writes the birds then calls the make_jet() and make_sign() functions
    gui: the canvas object to be written on
    x_position: the pixel position of the birds on the x-axis, periodic with respect to time
    y_parallax: the pixel position of the mouse relative to the y-axis of the tkinter window
    '''
    x_coord=30+x_position;y_coord=75;bird_count=0;
    while bird_count<5:
        gui.line(x_coord,y_coord-y_parallax*.4,x_coord+18,y_coord+8-y_parallax*.4);
        gui.line(x_coord+18,y_coord+8-y_parallax*.4,x_coord+36,y_coord-y_parallax*.4)
        x_coord+=80;y_coord+=14;bird_count+=1
    make_jet(gui,x_position*1.5);make_sign(gui,x_position*1.5)


def validate_rgb(gui,r,g,b,luminosity):
    '''
    Validates that the luminosity offset will create a valid r,g,b code
    If the luminosity offset will create a negative rgb number, the number will be set to zero;
    if the luminosity offset will create a rgb number>255, the number will be set to 255
    Returns validated gui.get_color_string call of conditionally adjusted r,g,b
    luminosity: float value representing luminosity of the canvas, periodic with respect to time
    in the domain [0,1330], simulates day/night cycle
    gui: the canvas object to be written on
    r,g,b: the base red, green, blue color codes of the object calling
    '''
    index=0;colors=[r,g,b]
    while index<3:
        while int(colors[index]-luminosity)>255 or int(colors[index]-luminosity)<0:
            if int(colors[index]-luminosity)>255:
                colors[index]-=.1
            else:
                colors[index]+=.1
        colors[index] = int(colors[index]-luminosity);index+=1
    return gui.get_color_string(colors[0],colors[1],colors[2])
    

def make_backdrop(gui,luminosity):
    '''
    Void function that writes the sky backdrop with lighting adjusted per simulated time of day
    Calls make_stars() when it is night time
    gui: the canvas object to be written on
    luminosity: float value representing luminosity of the canvas, periodic with respect to time
    in the domain [0,1330], simulates day/night cycle
    '''
    gui.rectangle(0,0,600,600,(validate_rgb(gui,181,218,255,luminosity*.2)))
    if luminosity>1100:
        make_stars(gui,luminosity)


def far_mountain(gui,mtn1_color,x_parallax,y_parallax):
    '''
    Void function that writes the far middle mountain filled w/ random color
    mtn1_color: a gui.get_color_string() result
    gui: the canvas object to be written on 
    x_parallax: the pixel position of the mouse relative to the x-axis of the tkinter window
    y_parallax: the pixel position of the mouse relative to the y-axis of the tkinter window
    '''
    gui.triangle(99-x_parallax*.2,500-y_parallax*.4,\
                 300-x_parallax*.2,149-y_parallax*.4,\
                 501-x_parallax*.2,500-y_parallax*.4);
    gui.triangle(100-x_parallax*.2,500-y_parallax*.4,\
                 300-x_parallax*.2,150-y_parallax*.4,\
                 500-x_parallax*.2,500-y_parallax*.4,mtn1_color)
    

def close_mountains(gui,mtn2_color,mtn3_color,x_parallax,y_parallax):
    '''
    Void function that writes the near left and right mountains filled w/ random colors
    mtn1_color, mtn2_color: distinct gui.get_color_string() results
    gui: the canvas object to be written on 
    x_parallax: the pixel position of the mouse relative to the x-axis of the tkinter window
    y_parallax: the pixel position of the mouse relative to the y-axis of the tkinter window
    '''
    gui.triangle(-123-x_parallax*.55,500-y_parallax*2,\
                 105-x_parallax*.55,197-y_parallax,\
                 332-x_parallax*.55,500-y_parallax*2);
    gui.triangle(-120-x_parallax*.55,500-y_parallax*2,\
                 105-x_parallax*.55,200-y_parallax,\
                 330-x_parallax*.55,500-y_parallax*2,mtn2_color);
    gui.triangle(247-x_parallax*.8,500-y_parallax*2,\
                 500-x_parallax*.8,197-y_parallax,\
                 723-x_parallax*.8,500-y_parallax*2);
    gui.triangle(250-x_parallax*.8,500-y_parallax*2,\
                 500-x_parallax*.8,200-y_parallax,\
                 720-x_parallax*.8,500-y_parallax*2,mtn3_color)
    

def make_foreground(gui,luminosity,x_parallax,y_parallax):
    '''
    Void function that writes the grass, grass blades, and tree w/ outlines
    gui: the canvas object to be written on
    luminosity: float value representing luminosity of the canvas, periodic with respect to time
    in the domain [0,1330], simulates day/night cycle
    x_parallax: the pixel position of the mouse relative to the x-axis of the tkinter window
    y_parallax: the pixel position of the mouse relative to the y-axis of the tkinter window
    '''
    gui.rectangle(-200,500-y_parallax*2,1000,600-y_parallax*2,\
                  (validate_rgb(gui,132,227,138,luminosity*.07)));
    gui.line(-200,500-y_parallax*2,1000,500-y_parallax*2,"black",2);x_index=-200;
    while x_index <= 800:
        gui.line(x_index-x_parallax,500-y_parallax*2,x_index-x_parallax,480-y_parallax*1.7,\
                 (validate_rgb(gui,132,227,138,luminosity*.07)),2)
        x_index+=5
    gui.rectangle(410-x_parallax*1.3,500-y_parallax*2,20,40,\
                  (validate_rgb(gui,61,1,9,luminosity*.01)));
    gui.ellipse(420-x_parallax*1.3,455-y_parallax*2,60,90,\
                (validate_rgb(gui,11,97,16,luminosity*.05)))


def make_moon(gui,orbit_angle,x_parallax,y_parallax):
    '''
    Void function that writes the moon at its current trajectory position
    Uses periodic parametric equation. (280,430) = orbit origin. 400 = orbit radius
    gui: the canvas object to be written on
    orbit_angle: float value should be periodic in domain [0°,180°] in radians w/ respect to time
    x_parallax: the pixel position of the mouse relative to the x-axis of the tkinter window
    y_parallax: the pixel position of the mouse relative to the y-axis of the tkinter window
    '''
    star_x=280+math.cos(orbit_angle)*400-x_parallax*.2;
    star_y=430+math.sin(orbit_angle)*400-y_parallax*.2;
    gui.ellipse(star_x,star_y,67,67,"white")
    

def make_sun(gui,orbit_angle,x_parallax,y_parallax):
    '''
    Void function that writes the sun at its current trajectory position
    gui: the canvas object to be written on
    orbit_angle: float value should be periodic in domain [0°,180°] in radians w/ respect to time
    x_parallax: the pixel position of the mouse relative to the x-axis of the tkinter window
    y_parallax: the pixel position of the mouse relative to the y-axis of the tkinter window
    '''
    star_x=280+math.cos(orbit_angle)*400-x_parallax*.2;
    star_y=430+math.sin(orbit_angle)*400-y_parallax*.2;
    gui.ellipse(star_x,star_y,70,70,"yellow")
    

def blinker_color(gui,luminosity):
    '''
    Returns red color half the time and blue the other half
    Accepts luminosity index value as an arbitrary ticker
    Slope of 2nd arg will determine frequency of blinker
    luminosity: any float or int value linearly changing with respect to time will work
    '''
    red,blue = gui.get_color_string(245,66,72),gui.get_color_string(66,126,245);
    return blue if int(luminosity/50)%2 == 0 else red
       
 
def make_tail(gui,x_position):
    '''
    Void function that writes the airplane tail, wings and blinking light
    gui: the canvas object to be written on
    x_position: the pixel position of the airplane on the x-axis, periodic with respect to time
    '''
    gui.triangle(490-x_position,120,500-x_position,120,492-x_position,165);
    gui.ellipse(492-x_position,165,10,10,'grey');
    gui.ellipse(492-x_position,165,7,7,blinker_color(gui,x_position));
    gui.line(600-x_position,100,595-x_position,67);
    gui.line(595-x_position,67,588-x_position,68);
    gui.line(588-x_position,68,578-x_position,99);
    gui.ellipse(590-x_position,87,7,7,'white');make_fumes(gui,x_position)
        
        
def make_fumes(gui,x_position):
    '''
    Periodically writes the fumes behind airplane as ellipses w/ semi-random sizes & positions
    gui: the canvas object to be written on
    x_position: the integer pixel position of the airplane on the x-axis,
    periodic with respect to time, also used as luminosity index value and random index
    '''
    color=validate_rgb(gui,206,210,217,x_position*.12);
    gui.ellipse(615-x_position-random.randint(-2,2),100-random.randint(-2,2),\
                15-random.randint(-8,-3),15-random.randint(-8,-3),color)
    if int(x_position/15)%2 == 0:
        gui.ellipse(625-x_position-random.randint(-2,5),100-random.randint(-2,5),\
                    15-random.randint(-2,5),15-random.randint(-2,5),color)
    if int(x_position/30)%2 == 0:
        gui.ellipse(635-x_position-random.randint(-2,5),100-random.randint(-2,5),\
                    15-random.randint(-2,5),15-random.randint(-2,5),color)


def make_sign(gui,x_pos):
    '''
    Writes banner behind airplane
    gui: the canvas object to be written on
    x_pos: the integer pixel position of the airplane on the x-axis, periodic with respect to time
    '''
    gui.rectangle(681-x_pos,89,178,30,gui.get_color_string(161,175,201))
    gui.rectangle(680-x_pos,90,177,30,'white');gui.line(685-x_pos,95,685-x_pos,115,'blue',1);
    gui.line(695-x_pos,95,695-x_pos,115,'red',1);gui.line(695-x_pos,115,702-x_pos,115,'red',1);
    gui.line(708-x_pos,95,708-x_pos,115,'red',1);gui.line(708-x_pos,115,716-x_pos,115,'red',1);
    gui.line(716-x_pos,115,716-x_pos,95,'red',1);gui.line(724-x_pos,95,730-x_pos,115,'red',1);
    gui.line(730-x_pos,115,736-x_pos,95,'red',1);gui.line(750-x_pos,95,750-x_pos,115,'blue',1);
    gui.line(750-x_pos,115,758-x_pos,115,'blue',1);gui.line(782-x_pos,95,782-x_pos,115,'red',1);
    gui.line(758-x_pos,115,758-x_pos,95,'blue',1);gui.line(775-x_pos,95,789-x_pos,95,'red',1);
    gui.line(782-x_pos,115,775-x_pos,115,'red',1);gui.line(797-x_pos,95,797-x_pos,115,'red',1);
    gui.line(797-x_pos,115,805-x_pos,115,'red',1);gui.line(805-x_pos,115,805-x_pos,95,'red',1);
    gui.line(812-x_pos,95,812-x_pos,115,'red',1);gui.line(841-x_pos,110,846-x_pos,110,'red',1);
    gui.line(812-x_pos,115,822-x_pos,115,'red',1);gui.line(830-x_pos,117,830-x_pos,94,'red',1);
    gui.line(838-x_pos,117,843-x_pos,95,'red',1);gui.line(843-x_pos,95,849-x_pos,117,'red',1);


def make_jet(gui,x_pos):
    '''
    Chained method that writes the airplane componenets then calls make_tail()
    gui: the canvas object to be written on
    x_pos: the integer pixel position of the airplane on the x-axis, periodic with respect to time
    '''
    gui.ellipse(512-x_pos,102,63,30);gui.ellipse(512-x_pos,103,60,30,'white');
    gui.line(460-x_pos,97,460-x_pos,135);gui.line(460-x_pos,97,453-x_pos,100);
    gui.line(460-x_pos,135,453-x_pos,128);gui.line(453-x_pos,100,453-x_pos,128);
    gui.ellipse(441-x_pos,114,3+.25*(x_pos%13),30);
    gui.ellipse(453-x_pos,114,25,13);
    gui.line(600-x_pos,100,460-x_pos,97);gui.line(600-x_pos,107,460-x_pos,135);
    gui.line(600-x_pos,100,600-x_pos,107);
    gui.triangle(600-x_pos,101,460-x_pos,98,460-x_pos,135,'grey');
    gui.triangle(460-x_pos,135,600-x_pos,99,600-x_pos,106,'grey');window_position=0
    while window_position<80:
        gui.ellipse(475+window_position-x_pos,107,6,6,'white');window_position+=10
    gui.line(600-x_pos,108,680-x_pos,106,'white',1);make_tail(gui,x_pos)

    
def make_stars(gui,luminosity):
    '''
    Makes stars when it is night time on the canvas
    Stars are randomly blinking dots with fluctuating brightness and semi-random yellowish color
    gui: the canvas object to be written on
    luminosity: float value representing luminosity of the canvas, periodic with respect to time
    in the domain [0,1330], simulates day/night cycle
    y_parallax: the pixel position of the mouse relative to the y-axis of the tkinter window
    '''
    x_coordinate=0
    while x_coordinate<600:
        if random.randint(0,142)%13==0:
            gui.ellipse(x_coordinate,random.randint(0,142),3,3,\
                        validate_rgb(gui,random.randint(0,255),255,\
                                     random.randint(0,255),luminosity*.1))
        x_coordinate+=random.randint(0,75)
                

def main():
    gui=graphics(600,600,'motion_parallax');wrap=luminosity=circadian=angle_moon=2.8;angle_sun=4;
    mtn1_color=gen_random_color(gui);mtn2_color=gen_random_color(gui);mtn3_color=gen_random_color(gui);
    while True:
        x=.2*(300-gui.mouse_x);y=.1*(300-gui.mouse_y); # parallax by mouse position
        gui.clear();make_backdrop(gui,luminosity);make_moon(gui,angle_moon,x,y);
        make_sun(gui,angle_sun,x,y);far_mountain(gui,mtn1_color,x,y);
        close_mountains(gui,mtn2_color,mtn3_color,x,y);make_foreground(gui,luminosity,x,y);
        make_birds(gui,wrap,y);gui.update_frame(120);
        # Define trajectory and angles of sun and moon in radians
        angle_moon+=0.00092;angle_sun+=0.00092;
        if angle_moon > 6:
            angle_moon = 3
        if angle_sun > 6:
            angle_sun = 3
            
        # Wrapping jet & birds
        wrap+=1;
        if wrap>650:
            wrap=-400
            
        # Day/night luminosity cycle
        circadian+=1;luminosity+=1;
        if circadian<500:
            luminosity-=1
        if circadian>1840 and circadian<2340:
            luminosity=1330
        if circadian>2340 and circadian<3680:
            luminosity-=2
        if circadian>3680:
            circadian=0


main()