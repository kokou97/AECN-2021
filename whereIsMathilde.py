# -*- coding: utf-8 -*-
"""
Created on Fri Oct 28 16:42:41 2022

@author: jdjad
"""

import checking as chckg

file = open("AECN-2021.txt", "r", encoding="UTF-8") 
readlines_file = file.readlines()
variantesName = ["Mathilde", "Mathild", "Matilde", "Matild",
                 "mathilde", "mathild", "matilde", "matild" ]
linesMathilde = chckg.searchByName(readlines_file, variantesName,
                                   "CHU de Saint-Etienne", 
                                   "médecine générale")
print(linesMathilde)
file.close()