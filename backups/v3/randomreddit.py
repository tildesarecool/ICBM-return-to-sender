# I found this on reddit
# https://www.reddit.com/r/pygame/comments/1c3jh6v/help_with_code/
# I decided to use it as exercise even though it current sits at 0 upvotes
# 
# 

import pygame as p, sys, time as t, random as r
p.init()
surface = p.display.set_mode((800, 800))
p.display.set_caption("Mining Game")
FPS = 60
grid = []
clock = p.time.Clock()

s = 0
color = None

def place_other():
    #grid = []
    for y in range(500, 1000, 50):
        for x in range(-50, 850, 50):
            five_below = r.randint(1, 20)
            if five_below == 1:
                grid.append((90, 37, 0))
            else:
                grid.append("gray")



def placc():
    #global s
    stop = False
    color = "white"
    for y in range(500, 1000, 50):
        for x in range(-50, 850, 50):
            if not stop:
                if s < len(grid):  
                    color = grid[s]
                    s += 1
                else:
                    stop = True
                    s = 0
            Stone_quadrat = p.Rect(x, y, 50, 50)
            p.draw.rect(surface, color, Stone_quadrat)



place_other()

def main():
######## declare main local vars between 'def main()' and  and this line ###########

    running = True

######## declare main local vars between 'def main()' and  and this line ###########
    while running:
        for event in p.event.get():
            if event.type == p.QUIT:
                    p.quit()
                    return
            elif event.type == p.KEYDOWN and event.key == p.K_q:
                p.quit()
                return
        surface.fill('black')

############################ actual while loop code below ##############################
# (call functions and make other loops here)


############################ actual while loop code above ##############################

        p.display.flip() # not sure difference between flip() and update(). I just use flip()
        clock.tick(FPS)

main()