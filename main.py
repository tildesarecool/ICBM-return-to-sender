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
pyg.init()


from genericShapeTemplate import objLine #,  GameRect

clock = pyg.time.Clock()






def main() -> None:
    disp = cmn.dsp # DO NOT MOVE OR COMMENT THIS

##########################################################################################        

    firstLine = objLine()

#    staticy  = 200
#    startx   = 100
#    xiterate = 100
#    yiterate = 200
#    endx     = 600
#    endy     = 600
    
    startx  = 50    # cmn.screen_rect.centerx
    starty  = cmn.SCREEN_HEIGHT - 10
    
    xiterate: int = 1
    yiterate: int = 1
    
    
    endx = startx    #: int     #= 100
    endy = starty    #: int     #= 200
    
    is_drawing = False
    draw_speed = 1

##########################################################################################    
    
    while True:
        
        for event in pyg.event.get():
            if event.type == pyg.QUIT:
                    pyg.quit()
                    return
            elif event.type == pyg.KEYDOWN and event.key == pyg.K_q:
                pyg.quit()
                return
            elif event.type == pyg.MOUSEBUTTONUP and event.button == 1:
                is_drawing = True
                endx, endy = pyg.mouse.get_pos()
                print(f"value of endx is {endx} and endy is {endy}")
                print(f"value of startx is {startx} and starty is {starty}")
                print(f"value of 128 * 3 is  { 128 * 3}")
                print(f"value of cmn.SCREEN_HEIGHT is {cmn.SCREEN_HEIGHT} so cmn.SCREEN_HEIGHT - 50 is {cmn.SCREEN_HEIGHT - 50}")
#            elif event.type ==  pyg.MOUSEBUTTONUP and event.button == 1:
#                is_drawing = False

        disp.fill(cmn.windowFillColor)
##########################################################################################        
        if is_drawing:
#            firstLine = objLine()
            if endx > startx:
                endx = min(endx,startx + draw_speed)
            elif endx < startx:
                endx = max(endx, startx - draw_speed)
            if endy > starty:
                endy = min(endy, starty + draw_speed)
            elif endy < starty:
                endy = max(endy, starty - draw_speed)
            firstLine._draw('teal', (startx, starty), (endx, endy), 5)
            
        pyg.display.flip()        
        clock.tick(cmn.FPS)

        pyg.display.set_caption(
            f"fps: {round(clock.get_fps(), 2)} - ICBMs"
        )
        
        
if __name__ == '__main__':
    main()

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







