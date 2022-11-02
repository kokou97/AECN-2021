# -*- coding: utf-8 -*-
"""
Created on Fri Oct 28 15:13:46 2022

@author: jdjad
"""
import checking as chckg

def missingRanks(path_string:str):
    file = open(path_string, "r", encoding="UTF-8") 
    readlines_file = file.readlines()
    file.close()
    allRanks = []
    for line in readlines_file:
        tmpRank = chckg.rankOfLine(line)
        if type(tmpRank) == int:
            allRanks.append(tmpRank)
    consecutiveRanks = list(range(1,max(allRanks)+1))
    missingRanks = chckg.resteListe(consecutiveRanks, allRanks)
    return missingRanks
    
def searchByRanks(ranksInput:list[int]):
    file = open("Rang-ECN-2021.txt", "r", encoding="UTF-8") 
    readlines_file = file.readlines()
    file.close()
    result = []
    fileToWrite = open("CESP-2021.txt", "w", encoding="UTF-8")
    fileToWrite.write("Voici le classement des CESP qui ont passé l'ECN en 2021: \n \n \n")
    for line in readlines_file :
        for jj in ranksInput :
            if line.__contains__(str(jj)):
                result.append(line)
                fileToWrite.writelines(line)
            break
    fileToWrite.close()
    return result
    
rangs_cesp_2021 = missingRanks("AECN-2021.txt")

result_cesp_2021 = searchByRanks(rangs_cesp_2021)