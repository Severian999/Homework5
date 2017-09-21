# -*- coding: utf-8 -*-
"""
Compare a lump sum payment option vs an annuitized payment option
Created on Wed Sep 20 19:54:38 2017

@author: Don Gass
"""

#
import locale
locale.setlocale(locale.LC_ALL, '')

from prettytable import PrettyTable
restable = PrettyTable()
restable.field_names = ['Number of Payments', 'Calculated Value']
restable.align['Number of Payments'] = 'c'
restable.align['Calculated Value'] = 'r'

#get user input
print('Which is better - a lump sum payment or n annuitized payments?\n')

lumpsum = int(input('Enter amount of lump sum payment (as an integer): '))
annuityamount = int(input('Enter yearly payment amount (as an integer): '))
annuitytime = int(input('How many years will you recieve yearly payments?: '))
rate = int(input('Enter rate % (positive real number): '))

#setup additional variables to be used in calculations
annual_rate = rate / 100
compound = 1
time = annuitytime

#lump sum calculation
lumpfinalamount = lumpsum*((1 + annual_rate/compound)**(compound*time))



#annuitized payment calculation
numpayments = 1
currentamount = 0

while numpayments <= annuitytime:
    currentamount = currentamount + annuityamount
    currentamount = currentamount * 1.05
    
    restable.add_row([numpayments, locale.currency(currentamount, grouping=True)])
    numpayments += 1

#print results
print('\n\n\nAfter', time, 'years at', rate,'% interest:\n')

print('Lump sum of', lumpsum, 'will return: ', end='')
print(locale.currency(lumpfinalamount, grouping=True),'\n')

print(str(annuitytime), 'years of $' + str(annuityamount), 'payments results:\n')
print(restable)

if currentamount > lumpfinalamount:
    print('Annuity options is better.')
else:
    print('Lump sum option is better.')

