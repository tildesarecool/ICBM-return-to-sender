# 27 feb 2024
# this is continues from display template to draw a shape on to the screen    
# I'm using 
# https://www.youtube.com/watch?v=ZeCeEUF2J2c
# as a basis for a very basic display setup and line/circle draw in in pygame

import pygame as pyg
#from pygame.sprite import Group
from pygame.sprite import Sprite
from common import Common 
cmn = Common()

# Import the abc module to define abstract classes and methods
# I got this from the cheat sheet I've been using
# https://www.pythoncheatsheet.org/cheatsheet/oop-basics

from abc import ABC, abstractmethod

# Define an abstract class called Shape that has an abstract method called area


pyg.init()

# dsp = pyg.display.set_mode((1000, 800)) # also known as the "surface"
# clock = pyg.time.Clock()
#FPS = 60
#
#ACCELLERATION = 0.5

class objShape(ABC, Sprite):
    '''A very generic shape class'''
    # as mentioned above apparently this is a thing.
    # I'd like to just write the one draw method and apply it to all shape classes so this syntax seemed perfect    
    
    def __init__(self) -> None:
        #Sprite.__init__()
        super().__init__(Sprite)

    
    @abstractmethod
    def _draw(self, color, xpos, ypos, width ):
        self.xpos = xpos 
        self.ypos = ypos
        self.color = color
        self.width = width


class objRightTriangle(objShape):
    
    def __init__(self  ) -> None:
        
        self.start_point = None
        self.base_length = None
        self.height = None
        
    def vertices(self, start_x, start_y, base_length):
        self.start_point = (start_x, start_y)
        self.base_length = base_length
        
    def _draw(self,  color, thickness, height):
        ''' 
        Use parameters from verticies to draw the three lines:
        startx/starty to startx + base lenghth (x2), y2 = starty
        x2, (y2 + vertical height) = (x3 = x2) and y3 = that height
        third line start point = x1/y1
        third line end point = x3/y3
        '''    

        # Calculate other vertices
        end_x = self.start_point[0] + self.base_length
        end_y = self.start_point[1]
        end_point = (end_x, end_y)
        
        x1 = self.start_point[0]
        y1 = self.start_point[1]
        
        x2 = self.start_point[0] + self.base_length
        y2 = y1
        
        x3 = x2
        y3 = height

        third_point = (end_x, height)
        
        hype_start_pos = (x1, y1)
        hype_end_pos = (x3, y3)
        
        # Draw lines
        pyg.draw.line(cmn.dsp, color, self.start_point, end_point, thickness) # Base/horizontal
        pyg.draw.line(cmn.dsp, color, end_point, third_point, thickness) # height/vertical
        pyg.draw.line(cmn.dsp, color, hype_start_pos, hype_end_pos, 2) # diagonal / hypotenuse 





class objTriangle(objShape):
    '''use polygon to draw a triangle: pos1 is upper most point, pos2 is bottom left'''    
    def __init__(self  ) -> None:
        pass
    
    def _draw(self, color, xpos1, ypos1, xpos2, ypos2, xpos3, ypos3,  width):
        '''use polygon to draw a triangle: pos1 is upper most point, pos2 is bottom left'''    
        
        self.color = color
        
        self.xpos1 = xpos1
        self.ypos1 = ypos1
        
        self.xpos2 = xpos2
        self.ypos2 = ypos2
        
        self.xpos3 = xpos3
        self.ypos3 = ypos3
        
        self.width = width


        return pyg.draw.polygon(cmn.dsp, self.color, 
                                [
                                 [self.xpos1, self.ypos1],
                                 [self.xpos2, self.ypos2],
                                 [self.xpos3, self.ypos3]
                                ],
                                self.width
                            )

class GameRect(objShape):
    '''A very generic shape Rectangle'''
    def __init__(self):#, xpos: int, ypos: int, width: int, height: int, color: list) -> None:
        pass

    def _draw(self, xpos: int, ypos: int, width: int, height: int, color: list) -> None:
        '''
        rectangle: color (three number tuple), x pos: single float, y pos: single float, width: float, height: float  
        '''
        #super()._draw()
        self.xpos = xpos
        self.ypos = ypos
        self.y = ypos
        self.color = color
        self.width = width
        self.height = height
        
        rect = pyg.Rect(self.xpos, self.ypos, self.width, self.height)
        pyg.draw.rect(cmn.dsp, self.color, rect)
        
   
class objCircle(objShape):
    '''Circle: color (three number tuple), centerpoint coords (two number tuple), radius int/float'''
    def __init__(self  ) -> None:
        pass


    
    def _draw(self, color,  centerPoint, radius) -> object:

        self.color = color
        self.centerPoint = centerPoint
        self.radius = radius

        return pyg.draw.circle(cmn.dsp, self.color, self.centerPoint, self.radius )

class objLine(objShape):
    def __init__(self):
        pass            
        #lineGroup = Group()




        
    def _draw(self, color, startPos, endPos, width ) -> object:
        '''
        Line: color (three number tuple), start pos (two number tuple), end pos (two number tuple), width: integer for line thickness 
        '''
        self.color = color
        self.startPos = startPos
        self.endPos = endPos
        self.width = width


        return pyg.draw.line( cmn.dsp, self.color, self.startPos, self.endPos, self.width)
        



#def game() -> None:
#    
##    firstRect = GameRect()
##    secRect = GameRect()
#    firstCircle = objCircle()
#    firstLine = objLine()
#    
#    
#    while True:
#        for event in pyg.event.get():
#            if event.type == pyg.QUIT:
#                return
#            if event.type == pyg.KEYDOWN and event.key == pyg.K_q:
#                return
#
#        dsp.fill((255,255,255))
###########################################################################            
#
#        # draw a horizontal line
#        #pyg.draw.line(dsp, (0, 0, 0), (0, 400), (1024, 400), 10 )
#
#        firstCircle._draw('green', (300,300), 150)
#        firstLine._draw('teal', (900,300), (100,600), 5)
#        
###########################################################################            
#
#        pyg.display.flip()
#        clock.tick(FPS)
#
#game()    
#pyg.quit()



#        secRect._draw(
#                250, 
#                10,
#                690,
#                15,
#                'blue'
#            )



#        firstRect._draw(
#            40,
#            100, 
#            100, 
#            300, 
#            'yellow', 
#        ) #._draw()