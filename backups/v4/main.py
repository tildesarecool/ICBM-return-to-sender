# 8 April 2024 
# My idea for this was to start working with lines
# having them draw from one point to another
# over some period of time rather than instantly
# And eventually make the mouse click location
# be the starting point
#  
# 18 April 2024
# Took a while, but i can now draw lines from an aribitrary start point
# to an arbitrary end point. The main task left is to make that end point 
# the captured mouse x/y coords. I've already done that once though so that 
# shouldn't take so long.


from common import Common 
cmn = Common()

import pygame as pyg
pyg.init()

from genericShapeTemplate import objCreateProjectile #,  GameRect

clock = pyg.time.Clock()

def main() -> None:
    disp = cmn.dsp # DO NOT MOVE OR COMMENT THIS

################################ see below #########################################    

#    firstLine = objLine()
#    xtrackLine = objLine()
#    ytrackLine = objLine()

    pressed = False


    mouse_release = False       

    RighttriangleOne = objCreateProjectile()
    
    RighttriangleOne.createVertices(
        cmn.screen_rect.left + 50, 
        cmn.screen_rect.bottom - 100, 
        cmn.CENTER_X + 100,   
        cmn.screen_rect.bottom - 250
    )

################################ see above #########################################    
    while True:
        
        for event in pyg.event.get():
            if event.type == pyg.QUIT:
                    pyg.quit()
                    return
            elif event.type == pyg.KEYDOWN and event.key == pyg.K_q:
                pyg.quit()
                return
            elif event.type ==  pyg.MOUSEBUTTONUP and event.button == 1:
                mouse_release = True

        disp.fill(cmn.windowFillColor)
################################ see below #########################################    

            
        if pyg.mouse.get_pressed()[0] == 1 and pressed == False:
            if mouse_release:
                pressed = True
                
                RighttriangleOne._draw( cmn.GREEN, 2, 2) #, 400)
                
                pressed = False
                
################################ see above #########################################    

        pyg.display.flip()        
        clock.tick(cmn.FPS)

        pyg.display.set_caption(f"fps: \
{ round( clock.get_fps(), 2 ) }\
 - ICBMs" )
        
        
if __name__ == '__main__':
    main()



                
                # these are imaginary line to right/up - just a tracker, not directly used in drawing line                
#                if xiterate <= cmn.SCREEN_WIDTH and  yiterate >= 0:
#                    
#                    xiterate = current_x
#                    current_x += 1
#                    xtrackLine._draw('red', start_coords, (xiterate, start_coords[1]), 5)
#                if yiterate >= 0:
#                    yiterate = current_y 
#                    current_y -= 1
#                    ytrackLine._draw('white', start_coords, (start_coords[0], yiterate ), 5)
#                
#                print(f"xiterate: {xiterate}")
#                print(f"yiterate: {yiterate}")
#                #print(f"ylonger is {ylonger}, xlonger is {xlonger}")
#                print(f"value of hypotenuse_final is {hypotenuse_final}")
#                # hypotenuse_length = math.hypot(final_coords[0] - start_coords[0], start_coords[1] - final_coords[1])
#                if (xlonger):
#                    if current_x <= final_coords[0]:
#                        #print(f"(value of xiterate / yiterate) ({xiterate / yiterate}) == target_ratio ({target_ratio}) is {(xiterate / yiterate) == target_ratio}")
#                        # target ratio = 9.5 e.g. x / y
#                        # x = target ratio * y
#                        # y = x / target ratio
#                        # x is longer to start iterating it first
#                        current_x = target_ratio * current_y
#                        # per the formula, given x, this should establish y
#                        current_y = current_x / target_ratio
#                        # now given the current x and y, draw the line?
#                        firstLine._draw('teal', start_coords, (current_x, current_y), 5)
#                        print(f"current_y is {current_y}, current_x is {current_x}")
#                        
#                        
#                        print(f"current_x is {current_x}, \
#current_y is {current_y} \
#target_ratio is {target_ratio} \
#current_x / target_ratio is {current_x / target_ratio}    \
#")
#                        
#
#
#
#
#
#                    
#            #mouse_release = False

#            firstLine = objLine()
#            print(f"mouse button pressed.")
#            firstLine._draw('teal', start_coords, (xiterate, yiterate), 5)












#                    print(f"(value of xiterate  + 5  / yiterate  + 5) is \
#                          ({(xiterate + 5 ) / (yiterate + 5 )})  \
#                           and (final_coords[0] - 5) / (final_coords[1]  \
#                               {(final_coords[0] ) / (final_coords[1])} ")
                    
#                    if (xiterate / yiterate) != target_ratio:
#                        yiterate += 1
#                        print(f"xiterate: {xiterate}")
#                        print(f"yiterate: {yiterate}")
##                            firstLine._draw('teal', start_coords, (xiterate, yiterate), 5)
#                        print(f"xiterate / yiterate is {xiterate / yiterate} while target ratio is {target_ratio}")
#                    elif (xiterate / yiterate) == target_ratio:
#                        print(f"(xiterate / yiterate) == target_ratio is equal ({xiterate / yiterate} and target radio {target_ratio})")
#                elif ylonger:
#                    yiterate += 1 # move imaginary line upwards  - just a tracker, not directly used in drawing line 
#                    print(f"yiterate: {yiterate}")
#                    if (yiterate / xiterate) == target_ratio:
#                        firstLine._draw('teal', start_coords, (xiterate, yiterate), 5)
#
#
#
#                if xiterate == 0:
#                    xiterate = 1
#                if yiterate == 0:
#                    yiterate = 1



#           This doesn't work because it sets is_drawing to false on mouseup the tests from is_drawing. so it's never true. stupid gpt
#            elif event.type == pyg.MOUSEBUTTONUP and event.button == 1:
#                is_drawing = True
#                endx, endy = pyg.mouse.get_pos()
#                print(f"value of endx is {endx} and endy is {endy}")
#                print(f"value of startx is {startx} and starty is {starty}")
#                print(f"value of 128 * 3 is  { 128 * 3}")
#                print(f"value of cmn.SCREEN_HEIGHT is {cmn.SCREEN_HEIGHT} so cmn.SCREEN_HEIGHT - 50 is {cmn.SCREEN_HEIGHT - 50}")
#            elif event.type ==  pyg.MOUSEBUTTONUP and event.button == 1:
#                is_drawing = False

#            if endx > startx:
#                endx = min(endx,startx + draw_speed)
#            elif endx < startx:
#                endx = max(endx, startx - draw_speed)
#            if endy > starty:
#                endy = min(endy, starty + draw_speed)
#            elif endy < starty:
#                endy = max(endy, starty - draw_speed)


        #while startx <= endx:
        
        #mouse_x, mouse_y = pyg.mouse.get_pos()
        #print(f"value of mouse_x is {mouse_x} and value of mouse_y is {mouse_y} ")
#        if pyg.mouse.get_pressed()[0] == 1 and pressed == False:
#            clickx = mouse_x
#            clicky = mouse_y
#            gotpressed = 1
#            #print(f"value of clickx is {clickx} and value of clicky is {clicky} ")
#            endx = clickx
#            endy = clicky
#            print(f"endx is {endx}")
#            print(f"endy is {endy}")
#            #endx = 278
#            #endy = 611
##            print(f"value of endx is {endx} and value of endy is {endy} ")
#            #xiterate = clickx
#            #yiterate = clicky
#            xiterate = startx
#            yiterate = starty
#        if pyg.mouse.get_pressed()[0] == gotpressed:
##            if xiterate > endx or yiterate > endy:
#
#            # x iter > end eg "mouse pos x" ==  "to the right"; y iter < end y eg mouse pos y== "above"
##            if xiterate >= endx or yiterate <= endy: # diagonal to right or vertical
#            if xiterate <= cmn.screen_rect.width \
#           and xiterate >= 0 \
#           and yiterate >= 0 \
#           and yiterate <= cmn.screen_rect.height:
#                
##                if xiterate != endx and yiterate != endy:
#                    
##                    if (cmn.screen_rect.height - endy) >= (cmn.screen_rect.width - endx) :
#                    #if xiterate <= endy:
#                print(f"endx is {endx} and endy is {endy}")                                    
#                print(f"(cmn.screen_rect.height - endy) >= (cmn.screen_rect.width - endx)  is {(cmn.screen_rect.height - endy) >= (cmn.screen_rect.width - endx) }")
#                yiterate -= 1
#                xiterate += 1
#                firstLine._draw('teal', (startx,starty), (xiterate,yiterate), 5)
##                    elif (cmn.screen_rect.height - endy) <= (cmn.screen_rect.width - endx):
##                        xiterate -= 1
#
#                    
#                    #print(f"endx is {endx} and endy is {endy}")                                    
#                    #firstLine._draw('teal', (startx,starty), (xiterate,yiterate), 5)
#            gotpressed = 0                    
                    #if xiterate >= endx:
                    #    xiterate -= 1                    
                    #if xiterate <= endx:
                    #    xiterate += 1
                    #if yiterate >= endy:
                    #    yiterate -= 1
                        
#                    if xiterate == endx and yiterate <= endy:
#                        yiterate -= 1
#                    if xiterate <= endx and yiterate == endy:
#                        xiterate += 1
#                    if xiterate >= endx and yiterate == endy:
#                        xiterate -= 1
#                    if xiterate == endx and yiterate >= endy:
#                        yiterate += 1
                    
            
                
                    
#                    if xiterate >= endx:
#                        xiterate -= 1
#                        yiterate -= 1
#                    elif xiterate <= endx:
#                        xiterate += 1
#                    elif yiterate >= endy:
#                        yiterate -= 1
#                    elif yiterate <= endy:
#                        #yiterate += 1
#                        pass
#                    #if xiterate == endx or yiterate == endy:
#                    #    print(f"xiterate == endx or yiterate == endy true reached")
#                    #    pass







#
#                    if (startx - endx) >= 1: # 
#                        if xiterate >= endx:
#                            xiterate -= 1
#                            yiterate -= 1
##                            print(f"value of xiterate is {xiterate}  (xiterate > endx) endx is {endx}")
#                            #firstLine._draw('teal', (startx,starty), (xiterate,yiterate), 5)

#                        elif (startx - endx) <= 0:
# 
#                            if endx >= xiterate:
#                                xiterate -= 1
#                                yiterate -= 1




                    
#                    if xiterate > endx:# or yiterate <= endy: # diagonal to right or vertical
#                        xiterate -= 1
#                        if yiterate < xiterate:
#                            yiterate -= 1
#                            firstLine._draw('teal', (startx,starty), (xiterate,yiterate), 5)
#                        elif xiterate > endx:
#                            xiterate += 1
#                        if xiterate == endx or yiterate == endy:
#                            print(f"value of endx is {endx}  value of xiterate is {xiterate}  (if xiterate == endx or yiterate == endy)")
#                            print(f"value of endy is {endy}  value of yiterate is {yiterate}  (xiterate > endx)")
#                    elif xiterate < endx:
#                        xiterate += 1
#                        yiterate -= 1
#                        firstLine._draw('teal', (startx,starty), (xiterate,yiterate), 5)
#                        if xiterate == endx or yiterate == endy:
#                            print(f"value of endx is {endx}  value of xiterate is {xiterate}  (if xiterate == endx or yiterate == endy) ")

            
            # x iter < end eg "mouse pos x" ==  "to the left";    
#            if xiterate < endx or yiterate <= endy: # diagonal to right or vert
#                xiterate += 1
#                yiterate -= 1
#                firstLine._draw('teal', (startx,starty), (xiterate,yiterate), 5)
                
                # to left of mouse x pos
                #if xiterate < endx: # and yiterate < endy:
                #  xiterate -= 1
                #  #yiterate += 1
                #  #firstLine._draw('teal', (startx,starty), (xiterate,yiterate), 5)
                #  
                ## above the mouse y pos
                #elif yiterate < endy:
                #  xiterate -= 1
                #  yiterate -= 1
                #elif xiterate > endx and yiterate < endy:
                #    xiterate += 1
                #    yiterate -= 1
            
            
                #print(f"value of xiterate is {xiterate} and value of yiterate is {yiterate} ")
                #print(f"Inside while loop: value of static y is {yiterate} and value of xiterate is {xiterate} ")
            #elif xiterate == endx or yiterate == endy:                
#            else:
#                gotpressed = 0
#        else:
#            #gotpressed = False
#            firstLine._draw('teal', (startx,starty), (xiterate,yiterate), 5)
            #gotpressed = 0


#        if pyg.mouse.get_pressed()[0] == 1:
#            pressed = True
#        elif pyg.mouse.get_pressed()[0] == 0:
#            pressed = False

##########################################################################################







