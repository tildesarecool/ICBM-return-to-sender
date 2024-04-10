# 8 April 2024 
# My idea for this was to start working with lines
# having them draw from one point to another
# over some period of time rather than instantly
# And eventually make the mouse click location
# be the starting point
# 



from common import Common 
cmn = Common()

import pygame as pyg

from genericShapeTemplate import objLine, GameRect

clock = pyg.time.Clock()

pyg.display.set_caption(
    f"fps: {round(clock.get_fps(), 2)} - ICBMs"
)


def main() -> None:
    disp = cmn.dsp # DO NOT MOVE OR COMMENT THIS

##########################################################################################        

    firstLine = objLine()
    
    if pyg.get_init == False:    
        pyg.init()

#    staticy  = 200
#    startx   = 100
#    xiterate = 100
#    yiterate = 200
#    endx     = 600
#    endy     = 600
    
    starty  = 600
    startx   = 600
    xiterate = 600
    yiterate = 600
    endx     = 100
    endy     = 200

    pressed = False


##########################################################################################    
    while True:
        for event in pyg.event.get():
            if event.type == pyg.QUIT:
                    pyg.quit()
                    return
            elif event.type == pyg.KEYDOWN and event.key == pyg.K_q:
                pyg.quit()
                return

        disp.fill(cmn.windowFillColor)
##########################################################################################        

        #while startx <= endx:
        
        mouse_x, mouse_y = pyg.mouse.get_pos()
        #print(f"value of mouse_x is {mouse_x} and value of mouse_y is {mouse_y} ")
        if pyg.mouse.get_pressed()[0] == 1 and pressed == False:
            clickx = mouse_x
            clicky = mouse_y
            print(f"value of clickx is {clickx} and value of clicky is {clicky} ")
            

        if xiterate > endx or yiterate > endy:
            firstLine._draw('teal', (startx,starty), (xiterate,yiterate), 5)
            xiterate -= 1
            yiterate -= 1
                #print(f"Inside while loop: value of static y is {yiterate} and value of xiterate is {xiterate} ")
            #elif xiterate == endx or yiterate == endy:                
        firstLine._draw('teal', (startx,starty), (xiterate,yiterate), 5)


        if pyg.mouse.get_pressed()[0] == 1:
            pressed = True
        elif pyg.mouse.get_pressed()[0] == 0:
            pressed = False

##########################################################################################
        pyg.display.flip()        
        clock.tick(cmn.FPS)
        
        
if __name__ == '__main__':
    main()

