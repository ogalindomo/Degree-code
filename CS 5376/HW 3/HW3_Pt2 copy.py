#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Oct 17 23:37:05 2020

@author: oscargalindo
"""

'''
State Assignment:
    S0 = RU 8p
    S1 = TU 10p
    S2 = RU 10p
    S3 = RD 10p
    S4 = RU 8a
    S5 = RD 8a
    S6 = TU 10a
    S7 = RU 10a
    S8 = RD 10a
    S9 = TD 10a
    S10 = 11am class begins 
    

'''


if __name__=="__main__":
    states_names = ["RU 8p","TU 10p","RU 10p","RD 10p","RU 8a","RD 8a","TU 10a",
                    "RU 10a","RD 10a","TD 10a","11am class begins"]
    actions_states = [
        [["P",1],["R",2],["S",3]],#State 0  
        [["R",4],["P",7]],
        [["R",4],["P",4,7],["S",5]],
        [["R",5],["P",5,8]],
        [["P",6],["R",7],["S",8]],
        [["R",8],["P",9]],
        [["R",10],["P",10],["S",10]],
        [["R",10],["P",10],["S",10]],
        [["R",10],["P",10],["S",10]],
        [["R",10],["P",10],["S",10]],
        [],#State S10
        ]
    transition_rewards = [
        [[2],[0],[-1]],#State 0  
        [[0],[2]],
        [[0],[2,2],[-1]],
        [[0],[2,2]],
        [[2],[0],[-1]],
        [[0],[2]],
        [[-1],[-1],[-1]],
        [[0],[0],[0]],
        [[4],[4],[4]],
        [[3],[3],[3]],
        [],#State S10
        ]
    
    