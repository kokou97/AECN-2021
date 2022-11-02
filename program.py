# -*- coding: utf-8 -*-
"""
Created on Thu Oct 27 15:52:09 2022

@author: jdjad
"""
import checking as chckg

file = open("AECN-2021.txt", "r", encoding="UTF-8") 
specialites = ["allergologie", "Anatomie et cytologie pathologique", 
               "Anesthésie-réanimation","Biologie médicale", 
               "Chirurgie maxillo-faciale", "Chirurgie orale",
               "Chirurgie orthopédique et traumatologique", 
               "Chirurgie pédiatrique", 
               "Chirurgie plastique, reconstructrice et esthétique",
               "Chirurgie thoracique et cardiovasculaire",
               "Chirurgie vasculaire", "Chirurgie viscérale et digestive",
               "Dermatologie et vénéréologie", 
               "Endocrinologie-diabétologie-nutrition", 
               "Génétique médicale","Gériatrie", "Gynécologie médicale", 
               "Gynécologie obstétrique","hématologie", 
               "Hépato-Gastro-Entérologie",
               "Maladies infectieuses et tropicales",
               "Médecine cardiovasculaire", "Médecine d'urgence", 
               "Médecine et santé au travail","Médecine générale", 
               "Médecine intensive-réanimation", 
               "Médecine interne et immunologie clinique",
               "Médecine légale et expertises médicales", 
               "Médecine nucléaire", "Médecine physique et de réadaptation",
               "Médecine vasculaire", "Néphrologie", "Neurochirurgie",
               "Neurologie", "Oncologie", "Ophtalmologie",
               "oto-rhino-laryngologie - chirurgie cervico-faciale", 
               "Pédiatrie", "Pneumologie","Psychiatrie", 
               "Radiologie et imagerie médicale", "Rhumatologie",
               "Santé publique", "Urologie"]
villes = ["Assistance publique-hôpitaux de Paris", 
          "Assistance publique des hôpitaux de Marseille",
          "hospices civils de Lyon","CHU de Bordeaux","CHU de Nice",
          "CHU de Nantes","CHU de Montpellier","CHU de Lille",
          "CHU de Caen","CHU de Toulouse","CHU de Tours","CHU de Limoges",
          "CHU de Rennes","CHU de Grenoble","CHU de Saint-Etienne",
          "CHU de Clermont-Ferrand","CHU de Nancy","CHU de Strasbourg",
          "CHU de Besançon","CHU de Dijon","CHU de Rouen","CHU de Poitiers",
          "CHU d'Amiens","CHU d'Anger","CHU de la Réunion","CHU de Brest",
          "CHU de la Martinique / Pointe-à-Pitre","CHU de Reims"]
specialites = chckg.applyCaseFold(specialites)
if (not chckg.isNotDuplicated(villes, specialites)):
    print("Retirez les éléments dupliqués"
          +" dans le liste villes ou dans la liste spécialités.")
else :
    print("Il y a en tout "+str(len(villes)) + " villes de spécialisation")
    print("Il y a en tout "+str(len(specialites)) 
          + " spécialités médicales et chirurgicales")
    #file.seek(0)
    readlines_file = file.readlines()
    file.close()
    irf=[]
    for i in range(0,len(readlines_file)) : irf.append(readlines_file[-1-i]) 
    res,spes_traitees,villes_traitees = [],[],[]
    for spe in specialites:
        for ville in villes:
            for line in irf:
                if line.__contains__(ville) and line.__contains__(spe):
                    res.append(chckg.rankOfLine(line))
                    if not spes_traitees.__contains__(spe) : 
                        spes_traitees.append(spe)
                    if not villes_traitees.__contains__(ville) : 
                        villes_traitees.append(ville)
                    break
    if len(spes_traitees)<len(specialites):
        print("Ces spécialités n'ont pas été traitees: \n")
        print(chckg.resteListe(specialites, spes_traitees))
    else: 
        if len(villes_traitees)<len(villes):
            print("Ces villes n'ont pas été traitees: \n")
            print(chckg.resteListe(villes, villes_traitees))   
        else :
            if len(res) > 0:             
                print("Le rang maximun pour que quelque soit son premier choix, "
                      +"celui-ci soit retenu est: "+str(min(res))) 