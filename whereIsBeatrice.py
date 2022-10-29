# -*- coding: utf-8 -*-
"""
Created on Fri Oct 28 16:38:41 2022

@author: jdjad
"""

import checking as chckg

file = open("AECN-2021.txt", "r", encoding="UTF-8") 
readlines_file = file.readlines()
variantesName = ["Béatrice", "Beatrice", "beatrice", "béatrice"]
linesBeatrice = chckg.searchByName(readlines_file, variantesName,"CHU de Lille", "médecine générale" )
print(linesBeatrice)
file.close()