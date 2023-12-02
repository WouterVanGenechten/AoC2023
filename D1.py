#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Dec  1 07:29:55 2023

@author: u0107886
"""


file1 = open('inputD1.txt', 'r')
calibration_document = file1.read().splitlines()


#part 1
calibration_values = []
for calibration_line in calibration_document:
    calibration_extraction = []
    for character in calibration_line:
        try:
            calibration_extraction.append(int(character))         
        except:
            continue
    if len(calibration_extraction) == 1:
        calibration_values.append(int(str(calibration_extraction[0])+str(calibration_extraction[0])))
    else:
        calibration_values.append(int(str(calibration_extraction[0])+str(calibration_extraction[-1])))        
total = sum(calibration_values)


#part 2
calibration_values = []
for calibration_line in calibration_document:
    if "oneight" in calibration_line: 
        calibration_line = calibration_line.replace("oneight", str(18))
    if "twone" in calibration_line:
        calibration_line = calibration_line.replace("twone", str(21))
    if "nineight" in calibration_line:
        calibration_line = calibration_line.replace("nineight", str(98))
    if "eightwo" in calibration_line:
        calibration_line = calibration_line.replace("eightwo", str(82))
        
    calibration_line = calibration_line.replace("one", str(1))    
    calibration_line = calibration_line.replace("two", str(2))
    calibration_line = calibration_line.replace("three", str(3))
    calibration_line = calibration_line.replace("four", str(4))
    calibration_line = calibration_line.replace("five", str(5))
    calibration_line = calibration_line.replace("six", str(6))
    calibration_line = calibration_line.replace("seven", str(7))
    calibration_line = calibration_line.replace("eight", str(8))
    calibration_line = calibration_line.replace("nine", str(9))
    print(calibration_line)
    calibration_extraction = []
    for character in calibration_line:
        try:
            calibration_extraction.append(int(character))         
        except:
            continue
    if len(calibration_extraction) == 1:
        calibration_values.append(int(str(calibration_extraction[0])+str(calibration_extraction[0])))
    else:
        calibration_values.append(int(str(calibration_extraction[0])+str(calibration_extraction[-1])))        
total = sum(calibration_values)