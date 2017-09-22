# -*- coding: utf-8 -*-
"""
Created on Thu Sep 21 22:12:04 2017

@author: Don Gass
"""
toss = []
scored_toss = []
user_max = 0
max_value = 0

while True:
    try:
        die = int(input('Enter die (1-6) or just hit Enter to quit: ')) 
        
        if die < 1 or die > 6:
            print('The dice we are using have 6 sides! Try again.')
        else:
            toss.append(die)
            
        continue
    except ValueError:
        break

while True:
    try:
        if toss != []:
            active = int(input('Choose active die: '))
        else:
            break
        #if toss.index(active) returns ValueError (meaning it doesn't find active
        #in the list), it will jump to except ValueError clause then back to try
        #clause
        
        toss.index(active)
        #calculate user score
        user_max = active * toss.count(active)
        #determine max possible score
        for x in toss:
            scored_toss.append(x * toss.count(x))
        
        max_value = max(scored_toss)
        
        break
    except ValueError:
        print('Try again! You must choose an active die from the rolled dice...', toss)

#display results
if max_value == 0:
    print("Didn't feel like rolling dice?")
else:        
    print('Your selection was %d with a score of %d.' % (active,user_max))

if max_value > user_max:
    print('You could have achieved a score of %d with a different selection!' % max_value)