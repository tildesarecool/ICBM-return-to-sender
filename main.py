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

    
    
    
    
    if pyg.get_init == False:    
        pyg.init()
    
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





##########################################################################################
        pyg.display.flip()        
        clock.tick(cmn.FPS)
        
        
if __name__ == '__main__':
    main()

