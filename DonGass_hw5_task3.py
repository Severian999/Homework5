# -*- coding: utf-8 -*-
"""
Created on Wed Sep 20 21:43:06 2017

@author: Don Gass
"""
bit_list = []
decimal_value = 0

while True:
    bit = input('Enter bit value (0 or 1) or anything else when done: ')
    if not bit.isnumeric():
        break
    elif int(bit) < 0 or int(bit) > 1:
        print('You must enter only a 1 or 0!')
    else:
        bit_list.append(int(bit))

for bit in bit_list:
    decimal_value = decimal_value * 2 + bit

print('The decimal value is', decimal_value)

