#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep 30 11:40:09 2020

@author: oscargalindo
"""


import re 

t = "`When I'm a Duchess,' she said to herself, (not in a very hopeful tone though), `I won't have any pepper in my kitchen at all. \n\n Soup does very well without--Maybe it's always pepper that makes people hot-tempered,' she went on …"
x = re.split(r'^[`]|-|[(]|[,]\s|\s[…]$|[,].\s|\s+|[,]\s[(]|[)][,]\s[`]|--|[.]\s|[?]$|\\n+',t)
print("############################################")
print(t)
print("############################################")
print(x)
print("############################################")
t = "After the glimpse I had had of the Martians emerging from the cylinder in which they had come to the earth from their planet, a kind of fascination paralyzed my actions. I remained standing knee-deep in the heather, staring at the mound that hid them. I was a battleground of fear and curiosity. I did not dare to go back towards the pit, but I felt a passionate longing to peer into it. I began walking, therefore, in a big curve, seeking some point of vantage and continually looking at the sand heaps that hid these new-comers to our earth. Once a leash of thin black whips, like the arms of an octopus, flashed across the sunset and was immediately withdrawn, and afterwards a thin rod rose up, joint by joint, bearing at its apex a circular disk that spun with a wobbling motion. What could be going on there?"
print(t)
print("############################################")
matches = re.findall(r'\b[b-dB-Df-hF-Hj-nJ-Np-tP-Tv-zV-Z]*[aeiouAEIOU]+[b-dB-Df-hF-Hj-nJ-Np-tP-Tv-zV-Z]*\b', t)    
print((matches))
print("############################################")