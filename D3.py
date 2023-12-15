#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Dec  3 11:30:18 2023

@author: u0107886
"""

import pandas as pd
import re

file1 = open('inputD3.txt', 'r')
Lines = file1.read().splitlines()
engine_overview = [list(row) for row in Lines]

symbols = ["#", "@", "+", "-", "/", "=", "*", "%", "&", "$"]

#part 1
#I created a list within lists of all indexes, last number being the linenumber where these indexes can be found.
line_number = 0 #there is probably a cleaner way to do it without keeping track of a counter
all_indexes = []
for line in engine_overview:
    for symbol in symbols:
        if symbol in line: 
            indices = [i for i, x in enumerate(line) if x == symbol]
            indices.insert(0, line_number)
            all_indexes.append(indices)
    line_number += 1

#find the hits above, below, left, .... and add a ! to those numbers, Like this I won't count numbers twice
for indexlist in all_indexes:
    for x in indexlist[1:]:
            
        if engine_overview[indexlist[0]][x-1] != ".":
            engine_overview[indexlist[0]][x-1] += "!"
        if engine_overview[indexlist[0]][x+1] != ".":
            engine_overview[indexlist[0]][x+1] += "!"
        if engine_overview[indexlist[0]+1][x] != ".":
            engine_overview[indexlist[0]+1][x] += "!"
        if engine_overview[indexlist[0]-1][x] != ".":
            engine_overview[indexlist[0]-1][x] += "!"
        if engine_overview[indexlist[0]-1][x-1] != ".":
            engine_overview[indexlist[0]-1][x-1] += "!"
        if engine_overview[indexlist[0]-1][x+1] != ".":
            engine_overview[indexlist[0]-1][x+1] += "!"
        if engine_overview[indexlist[0]+1][x-1] != ".":
            engine_overview[indexlist[0]+1][x-1] += "!"
        if engine_overview[indexlist[0]+1][x+1] != ".":
            engine_overview[indexlist[0]+1][x+1] += "!"
        else:
            continue
        
result_list = []
current_concatenation = ''
for line in engine_overview:
    for part in line:
        if part != '.' and part not in symbols:
            current_concatenation += part
        else:
            if current_concatenation:  # If there's something to append
                result_list.append(current_concatenation)
                current_concatenation = ''  # Reset for the next concatenation



sum_numbers_with_exclamation = 0

for item in result_list:
    if "!" in item: # Find all digit sequences followed by '!'
        num_without_exclamation = item.replace('!', '')
        sum_numbers_with_exclamation += int(num_without_exclamation)

print(f"The sum of numbers containing an exclamation mark is: {sum_numbers_with_exclamation}")

#part2

file1 = open('inputD3.txt', 'r')
Lines = file1.read().splitlines()
engine_overview = [list(row) for row in Lines]

line_number = 0 #there is probably a cleaner way to do it without keeping track of a counter
all_indexesof = []
for line in engine_overview:
    if "*" in line: 
        indices = [i for i, x in enumerate(line) if x == "*"]
        indices.insert(0, line_number)
        all_indexesof.append(indices)
    line_number += 1

#find the hits above, below, left, .... and add a ! to those numbers, Like this I won't count numbers twice
for indexlist in all_indexesof:
    print(indexlist)
    for x in indexlist[1:]:
        print(x)
        counter = 0    
        if engine_overview[indexlist[0]][x-1] != "." and "!" not in engine_overview[indexlist[0]][x] and "!" not in engine_overview[indexlist[0]][x-2]:
            counter += 1
            engine_overview[indexlist[0]][x-1] += "!"
            print("to the left")
        if engine_overview[indexlist[0]][x+1] != "." and "!" not in engine_overview[indexlist[0]][x] and "!" not in engine_overview[indexlist[0]][x+2]:
            counter += 1
            engine_overview[indexlist[0]][x+1] += "!"
            print("to the right")
        if engine_overview[indexlist[0]+1][x] != "." and "!" not in engine_overview[indexlist[0]+1][x+1] and "!" not in engine_overview[indexlist[0]+1][x-1]:
            counter += 1
            engine_overview[indexlist[0]+1][x] += "!"
            print("directly below")
        if engine_overview[indexlist[0]-1][x] != "." and "!" not in engine_overview[indexlist[0]-1][x+1] and "!" not in engine_overview[indexlist[0]-1][x-1]:
            print("directly above")
            engine_overview[indexlist[0]-1][x] += "!"
            counter += 1
        if engine_overview[indexlist[0]-1][x-1] != "." and "!" not in engine_overview[indexlist[0]-1][x] and "!" not in engine_overview[indexlist[0]-1][x-2]:
            print("diagonal above left")
            engine_overview[indexlist[0]-1][x-1] += "!"
            counter += 1
        if engine_overview[indexlist[0]-1][x+1] != "." and "!" not in engine_overview[indexlist[0]-1][x] and "!" not in engine_overview[indexlist[0]][x+2]:
            counter += 1
            engine_overview[indexlist[0]-1][x+1] += "!"
            print("diagonal above right")
        if engine_overview[indexlist[0]+1][x-1] != "." and "!" not in engine_overview[indexlist[0]+1][x] and "!" not in engine_overview[indexlist[0]][x-2]:
            counter += 1
            engine_overview[indexlist[0]+1][x-1] += "!"
            print("diagonal down left")
        if engine_overview[indexlist[0]+1][x+1] != "." and "!" not in engine_overview[indexlist[0]+1][x] and "!" not in engine_overview[indexlist[0]][x+2]:
            counter += 1
            engine_overview[indexlist[0]+1][x+1] += "!"
            print("diagonal down right")
        if counter == 2:
                if engine_overview[indexlist[0]][x-1] != ".":
                    engine_overview[indexlist[0]][x-1] += "("
                if engine_overview[indexlist[0]][x+1] != ".":
                    engine_overview[indexlist[0]][x+1] += "("
                if engine_overview[indexlist[0]+1][x] != ".":
                    engine_overview[indexlist[0]+1][x] += "("
                if engine_overview[indexlist[0]-1][x] != ".":
                    engine_overview[indexlist[0]-1][x] += "("
                if engine_overview[indexlist[0]-1][x-1] != ".":
                    engine_overview[indexlist[0]-1][x-1] += "("
                if engine_overview[indexlist[0]-1][x+1] != ".":
                    engine_overview[indexlist[0]-1][x+1] += "("
                if engine_overview[indexlist[0]+1][x-1] != ".":
                    engine_overview[indexlist[0]+1][x-1] += "("
                if engine_overview[indexlist[0]+1][x+1] != ".":
                    engine_overview[indexlist[0]+1][x+1] += "("
                else:
                    continue
result_list2 = []
current_concatenation = ''
for line in engine_overview:
    for part in line:
        if part != '.' and part not in symbols:
            current_concatenation += part
        else:
            if current_concatenation:  # If there's something to append
                result_list2.append(current_concatenation)
                current_concatenation = ''  # Reset for the next concatenation

pow_numbers_with_exclamation = 0
true_list = []
for item in result_list2:
    if "(" in item: # Find all digit sequences followed by '!'
        num_without_exclamation = item.replace('(', '').replace('!', '')
        true_list.append(num_without_exclamation)
        

numbers = list(map(int, true_list))

# Check if the number of elements is even for correct pairing
if len(numbers) % 2 == 0:
    result = 0
    for i in range(0, len(numbers), 2):
        result += numbers[i] * numbers[i + 1]
    print(f"The result of multiplying pairs of numbers is: {result}")
else:
    print("The list contains an odd number of elements. Please ensure an even number of elements for pairing.")

        
            
    

        
