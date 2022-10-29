# -*- coding: utf-8 -*-
"""
Created on Fri Oct 28 16:09:40 2022

@author: jdjad
"""

import checking as chckg

file = open("AECN-2021.txt", "r", encoding="UTF-8") 
readlines_file = file.readlines()
variantesName = ["Hélène", "Helene", "Hélene", "Helène","Heléne","Hèlène", 
                 "Hèléne", "hélène", "helene", "hélene","helène","heléne", 
                 "hèlène", "hèléne"]
linesHelene = chckg.searchByName(readlines_file, variantesName,"Assistance publique-hôpitaux de Paris", "médecine générale" )
print(linesHelene)
file.close()