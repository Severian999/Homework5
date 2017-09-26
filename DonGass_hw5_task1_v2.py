# -*- coding: utf-8 -*-
"""
Created on Tue Sep 19 21:35:56 2017

@author: Don Gass
Decided to try out a homebrew function :-)
"""

def howmanybars(money):
    """
    Given an amount of money (as int), return the number of chocolate bars you
    can get, where each bar costs $1 and contains a coupon. 10 coupons can be
    redeemed for 1 chocolate bar.
    
    Parameters
    ----------
    money : number
    
    Returns
    -------
    numbars : number
        The total number of chocolate bars that can be purchased/redeemed
    
    Example
    -------
    >>> howmanybars(100)
    111
    
    """
    numbars = money
    numcoupons = numbars
    
    while numcoupons >= 10:
        (numbars, numcoupons) = (numbars + 1, numcoupons - 9)
    return numbars        

# main program start
USRMONEY = int(input('How much money do you have to spend on chocolate bars? '))
print('You will have ' + str(howmanybars(USRMONEY)) + ' bars of chocolate!')
