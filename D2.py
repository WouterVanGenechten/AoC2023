#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Dec  2 09:36:04 2023

@author: u0107886
"""


file1 = open('inputD2.txt', 'r')
Lines = file1.read().splitlines()
splitted = []
for line in Lines:
    splitfurther = line.split(":")
    splitted.append(splitfurther)


#part 1
games = {}
for k,v in splitted:
    splitfurther = v.split(";")
    single_game = []
    for v in splitfurther:
        splitevenfurther = v.split(",")
        single_game.append(splitevenfurther)
    games[k] = single_game
impossible_games = []
for gamenumber in games:
    for color in games[gamenumber]:
        for subdraw in color:
            subdraw = subdraw.strip() 
            if "blue" in subdraw:
                if int(subdraw[0:2]) > 14:
                    impossible_games.append(gamenumber)
                    break
            if "red" in subdraw:
                if int(subdraw[0:2]) > 12:
                    impossible_games.append(gamenumber)
                    break
            if "green" in subdraw:
                if int(subdraw[0:2]) > 13:
                    impossible_games.append(gamenumber)
                    break
for wrong_game in impossible_games:
    try:
        del games[wrong_game]
    except: 
        continue
sum = 0
for gamenumber in games:
    split = gamenumber.split(" ")
    game_number = int(split[1])
    sum += game_number
print("answer to part one", sum)


#part 2
games = {}
for k,v in splitted:
    splitfurther = v.split(";")
    single_game = []
    for v in splitfurther:
        splitevenfurther = v.split(",")
        single_game.append(splitevenfurther)
    games[k] = single_game
sumpower = 0    
for gamenumber in games:
    blue = 0
    red = 0
    green = 0
    for color in games[gamenumber]:
        for subdraw in color:
            subdraw = subdraw.strip() 
            if "blue" in subdraw:
                if blue == 0:
                    blue = int(subdraw[0:2])
                else:
                    if blue < int(subdraw[0:2]):
                        blue = int(subdraw[0:2]) 
            if "red" in subdraw:
                if red == 0:
                    red = int(subdraw[0:2])
                else:
                    if red < int(subdraw[0:2]):
                        red = int(subdraw[0:2]) 
            if "green" in subdraw:
                if green == 0:
                    green = int(subdraw[0:2])
                else:
                    if green < int(subdraw[0:2]):
                        green = int(subdraw[0:2]) 
    power = blue*green*red
    sumpower += power
print("answer to part two", sumpower)



    
