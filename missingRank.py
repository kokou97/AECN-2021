# -*- coding: utf-8 -*-
"""
Created on Fri Oct 28 15:13:46 2022

@author: jdjad
"""
import checking as chckg

file = open("AECN-2021.txt", "r", encoding="UTF-8") 
#file.seek(0)
readlines_file = file.readlines()
allRanks = []
for line in readlines_file:
    tmpRank = chckg.rankOfLine(line)
    if type(tmpRank) == int:
        allRanks.append(tmpRank)
consecutiveRanks = list(range(1,max(allRanks)+1))
missingRanks = chckg.resteListe(consecutiveRanks, allRanks)
print(missingRanks)
file.close()