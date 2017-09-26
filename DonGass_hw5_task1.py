# -*- coding: utf-8 -*-
"""
Created on Tue Sep 19 21:35:56 2017

@author: Don Gass
"""

amountMoney = int(input('How many dollars do you have to spend on chocolate bars? $'))
numBars = amountMoney
numCoupons = numBars

while numCoupons >= 10:
    (numBars, numCoupons) = (numBars + 1, numCoupons - 9)
    
print('You will have {0} bars of chocolate with {1} coupons left over!'.format(numBars, numCoupons))