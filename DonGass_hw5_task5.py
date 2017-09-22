# -*- coding: utf-8 -*-
"""
Created on Thu Sep 21 23:38:58 2017

@author: Don Gass
"""

medals = [("ITA","JPN","AUS"), ("KOR","TPE","UKR"), ("KOR","KOR","GBR"),("KOR","CHN","TPE")]
medal_counts = {}

for gold, silver, bronze in medals:
    #process gold list
    medal_counts.setdefault(gold, [0,0,0])
    medal_counts.setdefault(silver, [0,0,0])
    medal_counts.setdefault(bronze,[0,0,0])
    
    medal_counts[gold][0] += 1
    medal_counts[silver][1] += 1
    medal_counts[bronze][2] += 1

print(medal_counts)