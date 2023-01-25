# ChatGPTBreakout
A simple version of creating Atari Breakout by prompting ChatGPT to create various parts of the game and putting them together.

Prompt: “write a python program to create Atari breakout”
ChatGPT: outputted a pygame initialization and a game loop that theoretically would draw a paddle and a ball that could move around, but missing variable initializations.

Here I was not confident in my was more interested in writing out more complete code and establishing my vision for what ChatGPT would do than getting the screen to pop up. 

Modification: “For a game like atari breakout, could you write a python program to handle collision detection?”
ChatGPT: outputted collision detection functions as well as an adjusted game loop that checks for collision detection between the ball and paddle and ball and bricks and changes the y-velocity accordingly. However, fails to increment ball position based off of speed and fails to change the x-velocity.

Modification: “Since we are able to detect collisions, could you write a python program that makes the ball bounce off the paddle and bounce off bricks like in Atari breakout?”
ChatGPT: Increments ball position based off of speed and adds in x-velocity changes depending brick and paddle collisions, taking into account the paddle’s speed.

Modification: “integrate the previous code snippets”
Integrates all of the above code and adds in variable declarations. However, the code cuts off near the end of the game loop and fails to reverse y-velocity on collisions, remove bricks, and increment the ball’s position.

Modification: “could you adjust the code such that we reverse the ball's y on collisions?
ChatGPT: Fixes all of the issues that occurred in the previous modification.

However, here I noticed that the code doesn’t run because we lack a Brick class that the integrated code misses.

Modification: can you create a python class for a brick object in Atari Breakout that integrates with the previous code
ChatGPT: creates a Brick object and restates a brick initialization and brick collision function.

Modification: can you render the bricks, the ball, and the paddle and integrate that with the previous code snippets?
ChatGPT: restates the integrated code but gets cut off near the end. Does not implement what I asked it

Here I’m concerned because the pygame window still does not display when the code is run. I looked around online and then asked ChatGPT to draw everything:

Modification: “could we adjust the code so that we draw the ball, bricks, and paddle in the game loop?”
ChatGPT: returns the integrated code including drawing the bricks, paddle, ball, and updating the display on every loop.

Still concerned because I can’t see the screen.

Modification: “could we adjust the code so that we display the screen?”
Returns a cut-off version from my previous modification without changing anything

Modification: can you write a bit of code to initalize and create a screen on which the game will display
Misspell initialize and it still works
Output initialization code to create the screen and set the title of the screen to Atari Breakout

Modification: could we adjust the game such that the ball does not accelerate every loop?
Outputs the cut-off integrated code with a modification at the top to initialize with a set ball speed. This fixes the issue

Modification: can we make it so that the edges of the screen are also a boundary that the ball can bounce off of?
Tells me it can, and then spits the same integrated code out again.

Modification: can you write a code snippet to detect collisions between the ball and the edges of the screen every game loop?
Spits the same integrated cod eout again.

I’m annoyed, so I reduce the amount of code that has to output 

Modification: can you write a code snippet to detect collisions between the ball and the edges of the screen assuming that this snippet occurs every game loop?
It returns if and elif conditions which I can use to put into the game loop so the ball bounces off at the boundary of the screen. I inserted this into the game loop and it works fine.
It attempts to explain this code but then also cuts itself off.
