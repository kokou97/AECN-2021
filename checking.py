# -*- coding: utf-8 -*-
"""
Created on Thu Oct 27 17:10:47 2022

@author: jdjad
"""
import collections

def duplicatedElements(input0:list):
    return [item for item, 
            count in collections.Counter(input0).items() if count > 1]
# Check if duplicate in villes and specialites
def isNotDuplicated(villes:list, specialites:list):
    duplicate_villes = duplicatedElements(villes)
    duplicate_specialites = duplicatedElements(specialites)
    if (len(duplicate_villes)!=0):
        print("Duplication de villes."
              + " Le/les élément-s dupliqué-s dans villes est/sont : "
              + str(duplicate_villes))
        return False
    
    if (len(duplicate_specialites)!=0):
        print("Duplication de spécialités."
              + " Le/les élément-s dupliqué-s dans specialités est/sont : "
              + str(duplicate_villes))
        return False
    return True

def applyCaseFold(input1:list):
    output1=[]
    for i in range(0, len(input1)):
        output1.append(input1[i].casefold())
    return output1

def rankOfLine (phrase:str):
    resu = phrase.find("M")
    if resu != -1:
        resu2=phrase[0:resu-1]
        return int(resu2)
    
def resteListe (input2:list, input3:list):
    reste = input2.copy()
    for spe in  input3:
        reste.remove(spe)   
    return reste

def searchByName (input4:list, input5:list, input6:str, input7:str):
    output2=[]
    for line_input4 in input4:
        for line_input5 in input5:
            bool1 = line_input4.__contains__(line_input5)
            bool2 = line_input4.__contains__(input6)
            bool3 = line_input4.__contains__(input7)
            if bool1 and bool2 and bool3:
                if not output2.__contains__(line_input4):
                    output2.append(line_input4)
    return output2

def listSpeVille (input8:list, input9:str, input10:str):
    output3=[]
    for line_input8 in input8:
        bool1 = line_input8.__contains__(input9)
        bool2 = line_input8.__contains__(input10)
        if bool1 and bool2:
            if not output3.__contains__(line_input8):
                output3.append(line_input8)
    return output3