# -*- coding: utf-8 -*-
"""
Created on Wed Sep 20 21:43:06 2017

@author: Don Gass
"""
bit_list = []

while True:
    bit = input('Enter bit value (0 or 1) or "d" when done: ')
    if bit == "d":
        break
    elif bit.isdigit() == False:
        print('You must enter a digit or "d" when done!')
    else:
        bit_list.append(int(bit))

decimal_value = 0

for bit in bit_list:
    decimal_value = decimal_value * 2 + bit

print('The decimal value is', decimal_value)

