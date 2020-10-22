#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Show a random message."""

from __future__ import print_function
import os
from random import choice

_, width = os.popen('stty size', 'r').read().split()
width = int(width)

messages = [
    "Welcome to Pandora, kiddos",
    "Butt Stallion says hello",
    "I told you guys, the hero always wins",
    "See, this is what I don't get about you bad guys. You know the hero's gonna win,\nbut you never just die quickly",
    "This guy rushes me with a spoon. A fricking spoon. And I'm just laughing.\nSo I scoop out his eyeballs with it, and his kids are all, 'aghhhhh!', and,\nah...you had to be there",
    "Anyway, the moral is: you're a bitch",
    "Welcome to the Wildlife Exploitation Preserve, kiddo",
    "Didja know your chances of being disemboweled increase by 800% \nupon leaving Opportunity? Scientific fact",
    "You’re a savage! You’re a maniac! You are a bandit AND I AM THE GODDAMN HERO!",
    "Science isn't about WHY. It's about WHY NOT",
    "But there's no sense crying over every mistake.\nYou just keep on trying 'til you run out of cake.",
    "All your base are belong to us",
    "Finish Him!",
    "Do a barrel roll!",
    "You are not a good person. You know that, right? Good people don't end up here",
    "I dont know the dead man. Probably doesn't deserve what he got.\nThat dont make him special though",
    "All kinds of people die out here.\nThe innocent and the not so innocent",
    "I HAVE THE SHINIEST MEAT BYCICLE!",
    "I'M THE CONDUCTOR OF THE POOP TRAIN!",
    "Tell her she is as gourgeous as a thousand sunsets. Tell her you need her help.\nTell her to rescue you and to care for you and whatever you do,\ndo not scream the word 'poop' from the top of your lungs!",
    "STRIP THE FLESH AND SALT THE WOUND!",
    "My stomach is clear and my mind is full of bacon!",
    "I LOOKED INTO THE HEART OF DARKNESS, AND I ATE IT ALL!!!"
]

for line in choice(messages).split("\n"):
    print("\x1B[0;100m{}\x1B[m".format(line.center(width, " ")))
