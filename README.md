# ICBM: return to sender
Inspired by Atari's Missile Command, but simpler and with a twist.

---

I went through many more iterations of this. Over and over I did this. 

Eventually I realized I needed to maintain the ratio of the x and y. And that the end of the line as its being drawn makes a triangle. So I'm describing a *trigonometry*. The *tangent* more specifically. I'm not sure if it's good or bad it took me so long to arrive at elementary trigonometry.

So I've come to this conclusion but I haven't yet implemented it. At least I have a direction to go in now.

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