# ChatGPTBreakout
A simple version of creating Atari Breakout by prompting ChatGPT to create various parts of the game and putting them together.
This project is an exploration of the potential of ChatGPT in assisting programming.
Additionally, this project is a continuation of a project to explore ChatGPT given by COMPSCI390: Computational Approaches to NLP.

**Prompt**: “write a python program to create Atari breakout”
ChatGPT outputted a pygame initialization and a game loop that theoretically would draw a paddle and a ball that could move around, but because it leaves variables uninitialized, fails to work. Also fails to import sys, so I added that manually.

**Prompt**: “For a game like atari breakout, could you write a python program to handle collision detection?”
ChatGPT outputted collision detection functions as well as an adjusted game loop that utilizes those functions to change the y-velocity of the ball accordingly. However, ChatGPT fails to increment ball position based off speed and fails to change the x-velocity.

**Prompt**: “Since we are able to detect collisions, could you write a python program that makes the ball bounce off the paddle and bounce off bricks like in Atari breakout?”
ChatGPT increments ball position based off speed and adds in x-velocity changes depending brick and paddle collisions, taking into account the paddle’s speed.

**Prompt**: “integrate the previous code snippets”
ChatGPT successfully integrates all previously generated code. However, the code cuts off so it fails to reverse y-velocity on collisions, remove bricks, and increment the ball’s position.

**Prompt**: “could you adjust the code such that we reverse the ball's y on collisions?
ChatGPT: Fixes all of the issues that occurred in the previous modification.

**Prompt**: can you create a python class for a brick object in Atari Breakout that integrates with the previous code
ChatGPT: creates a Brick object and restates a brick initialization and brick collision function.

**Prompt**: can you render the bricks, the ball, and the paddle and integrate that with the previous code snippets?
ChatGPT: restates the integrated code but gets cut off near the end. Does not implement what I asked it

**Prompt**: “could we adjust the code so that we draw the ball, bricks, and paddle in the game loop?”
ChatGPT: returns the integrated code including drawing the bricks, paddle, ball, and updating the display on every loop.

**Prompt**: “could we adjust the code so that we display the screen?”
ChatGPT returns a cut-off version from my previous modification without changing anything

**Prompt**: “can you write a bit of code to initalize and create a screen on which the game will display”
ChatGPT outputs initialization code to create the screen and set the title of the screen.

**Prompt**: “could we adjust the game such that the ball does not accelerate every loop?”
ChatGPT fixes the issue, but a lot of the code at the end is cut off**.

**Prompt**: “can we make it so that the edges of the screen are also a boundary that the ball can bounce off of?”
Tells me it can, and then spits the same cut-off code out again.

**Prompt**: “can you write a code snippet to detect collisions between the ball and the edges of the screen every game loop?”
Tells me it can, and then spits the same cut-off code out again.

**Prompt**: “can you write a code snippet to detect collisions between the ball and the edges of the screen assuming that this snippet occurs every game loop?”
It returns conditional statements, which I can insert to into the game loop so the ball bounces off at the boundary of the screen. It attempts to explain this code but then also cuts itself off.

**Prompt**: "can you implement scoring?"
It adds a score variable that increments. However, it fails to display scoring as the code is cut off.

**Prompt** "could you finish your response?"
Finishes the code segment, but uses a font function that was not defined earlier. However, when explaining, ChatGPT tells us how to initialize this function.

**Summary**:
I am thoroughly impressed by ChatGPT’s ability to create code snippets and function as a programmer’s aid. It is surprisingly resilient to different methods of prompting it and understands questioning, context, misspellings, and easily follows up in a conversation. Oftentimes, after printing the code segment, it will also explain new functions it uses and how they function, which is exceptionally handy.

However, ChatGPT often cuts off the code, which I find this very strange. Changing the prompting is necessary but not always successful to get around this, forcing the user to stitching separate code snippets that ChatGPT generates to get functional code.

Overall, I feel it is a great way to get a first draft of ideas, allowing one to write a working prototype and use a variety of packages they may or may not know in just an hour or so.