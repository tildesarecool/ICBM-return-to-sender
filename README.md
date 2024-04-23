# ICBM: return to sender
Inspired by Atari's Missile Command, but simpler and with a twist.

---

I was trying to make the line draw from the starting position which is always the same to the x/y position of the mouse upon left-click. I actually had the working earlier in development. Then some work with calculating tangents was done, yada-yada-yada, it doesn't work any more.

I can at least have the line stop drawing when it reaches the mouse. I mean you have to still hold the mouse button instead of just clicking. But technically it works. Except once it reaches the mouse there's no way to start a new line unless your quit and re-run it.

The state it's currently in I was trying to make the line start over at the start point but instead it seems to have some kind of strobe effect already drawn to the mouse. So I still have more work to do.

---

I went through many more iterations of this. Over and over I did this. 

Eventually I realized I needed to maintain the ratio of the x and y. And that the end of the line as its being drawn makes a triangle. So I'm describing a *trigonometry*. The *tangent* more specifically. I'm not sure if it's good or bad it took me so long to arrive at elementary trigonometry.

So I've come to this conclusion but I haven't yet implemented it. At least I have a direction to go in now.

---

As of last night and some this morning I have the solution to this issue. I wish I could say I entirely understand how it works but truth is not really.

Below is my Right Triangle class, which may have some improper form to it. So don't use this as a model for "good code".

I'm glad I finally got the solution because I don't think I ever would have come up with this on my own. To my own credit I did have to "port" the code to my own class and mke sure it works. That wasn't very hard or time consuming.

I knew it was some kind of trigonometry related something-or-other.



```Python

class objRightTriangle(objShape):
    
    def __init__(self  ) -> None:
        
        self.start_point = None
        self.end_point = None
        self.drawn_length = 0  # Variable to track the length of the drawn line


    def vertices_from_hypotenuse(self, start_x, start_y, end_x, end_y):
        # this is copy/pasted from gpt and the name is from a prior request about calculation the width and height lines based on
        # the hypotenuse. seems i've lost the horizontal/verticle lines but kept the method name
        self.start_point = (start_x, start_y)
        self.end_point = (end_x, end_y)
        
        self.x1 = self.start_point[0]
        self.y1 = self.start_point[1]
        
        self.x2 = self.end_point[0]
        self.y2 = self.y1
        
        self.x3 = self.x2
        self.y3 = self.end_point[1]
        
    def _draw(self, color, thickness, iterator):
        
        # seems like a good thing to have in here
        if self.start_point is None or self.end_point is None:
            raise ValueError("Start and end points not specified")
        
        # Calculate the length of the hypotenuse using math.hypot()
        #                              start x "x2"         start x "x1"         end y "y2"         end y "y1" 
        hypotenuse_length = math.hypot(self.end_point[0] - self.start_point[0], self.end_point[1] - self.start_point[1])
        
        # Increase the drawn_length by iterator in each iteration actually wanted to do the iterating bit directly from 
        self.drawn_length += iterator
        
        # Calculate the end point of the drawn line based on the drawn_length
        drawn_end_x = self.start_point[0] + (self.end_point[0] - self.start_point[0]) * (self.drawn_length / hypotenuse_length)
        drawn_end_y = self.start_point[1] + (self.end_point[1] - self.start_point[1]) * (self.drawn_length / hypotenuse_length)
        drawn_end_point = (int(drawn_end_x), int(drawn_end_y))
        
        # draw the hypotenuse
        pyg.draw.line(cmn.dsp, color, self.start_point, drawn_end_point, thickness)
        
        
        # If the drawn length exceeds the length of the hypotenuse, stop the animation
        if self.drawn_length >= hypotenuse_length:
            self.drawn_length = hypotenuse_length

```

---

This might just be me failing basic trigonometry again, but I just solved a mystery of why something wasn't working. 

So I created a problem, found that there was a problem, then managed to resolve the problem I created. And now I'm making note of it like it was an accomplishment.

My idea was to use a class to combine three individual lines into a right triangle:
I need a starting (x1,y1) coordindate
a base width, will be the same y1 combined with x1 + base width
so y2 = y1
and
x2 = (x1 + base width)

Then a height, so
x3 = x2
y3 = (y2 + vertical height)

The last line, the hypotenuse, would just be from (x1,y1) to (x3,y3). This part worked. I have such a class.

Then, I thought, could just adjust that height variable - y3 in otherwards - and this would give me the drawing in over time diagonal line I've been looking for. By starting y3 at y2 and iterating y3 one pixel at a time.

The issue was that the height of the traingle would always start at apparently the max height of the triangle instance instead of where I wanted: y2. 

I tracked down the issue: I thought since the hypotenuse just needed to be drawn I didn't need any parameters. The draw method could just draw it. But that height is established with what is essentially (y2 - height). In other words if the y2 is 710 the end point of the hypotenuse is (710 - 710). Since the bigger the number the lower the point is on the y axis, that puts the height at the top of the screen or actually well off the screen.

The solution was to make y3 equal to that iterating variable. So that y3 started at y2 and slowly went upwards which by definition was drawing in the hypotenuse. 

The whole idea of the class with the three lines was to have the base and verticle lines there visible while i work on this but have the option of setting their "thickness" to 0 to make them no longer visible. Which works.



---

I'm still trying to figure out how to make the line draw from one place to another. I feel like I'm either really close or not any closer than I was. 

I thought I was on to something at one point but I think I must have missed something. I'll keep working on it but also probably work on some other things.

Actually I was able to click once to set off the loop that drew the string but that doesn't work any more. So in that sense I've gone backwards.

---

Today I worked for hours without success. I actually came painfully close a couple of times but still not acting the way I want it to.

I eventually move on to making the end point of the line a specific mouse x and y position. I mean I capture those points and set them as the end point. The line doesn't actually end at that set of mouse coordinates. 

I'm probably missing something really really obvious. It's be hard to make a line draw iteratively from one point to another. If the 2600 could it without any fancy radians, degrees or vector math than this little Python script should also be able to do that.

The code is a mess at the moment as I have this bad habit of commenting out a black of code at a time and starting somewhat fresh. If you can't read it it's okay as I can't either.

---

This is a generic learn-to-do-things project. Like an exercise by I set my own parameters.

My idea was to model *Missile Command*: lots of lines coming down from the top and player lines traveling upwards to the mouse click end point location.

The twist I'd like to implment is to have a role reversal after each round: after defending cities and silos from enemy ICBMs, the player is then in charge of sending ICBMs at enemy city targets and ICBMs.

I was also contemplating if that could work as a turn-based thing like the old game *Rampart*. 

This is just an exercise though. No idea if I'll ever implement anything.

Also, I need a better title.

---

So far I've created a *genericShapeTemplate* class that is supposed to make drawing various shapes easier. Or in this case almost entirely lines. There's also a class for rectangles and circles. They're there if I need them.

So I'm going to create a function or class that give the line a set of starting coordinates and one of the two end coordinates then the second coordinate I'll do the trust old += 3 to it and just see what happens. Something like that. I'm sure it'll work.


---