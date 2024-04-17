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