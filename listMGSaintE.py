# -*- coding: utf-8 -*-
"""
Created on Fri Oct 28 16:55:05 2022

@author: jdjad
"""
import checking as chckg

file = open("AECN-2021.txt", "r", encoding="UTF-8") 
readlines_file = file.readlines()
linesMGSaintE = chckg.listSpeVille(readlines_file,"CHU de Saint-Etienne", 
                                   "médecine générale")
print(linesMGSaintE)
file.close()