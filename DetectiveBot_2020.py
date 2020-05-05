# -*- coding: utf-8 -*-
"""
Created on Fri Feb  7 17:51:56 2020

@author: Lucille
"""
import nltk
from tkinter import Tk
from tkinter.filedialog import askopenfilename
from xml.dom import minidom
import re

""" Variables """
reg_ref = "<ref.*>.*\n*.*</ref.*>"

filetypes = [('Document XML','*.xml')] # Type de fichier pour le filechooser

""" Fonction pour ouvrir le fichier XML """
def filechooser():
    Tk().withdraw()
    filename = askopenfilename(filetypes=filetypes)
    """print(filename)"""
    return filename

""" Fonction pour récupérer le contenu de la balise <text> du XML """
def readXML(filename) :
    file = minidom.parse(filename)
    text = file.getElementsByTagName('text')[0].childNodes[0].nodeValue
    return text

""" Fonction qui nettoie le texte des balises <ref></ref>"""
def clearText(input):
    input = input.replace("| name =", "|name=").replace("| country =", "|country=").replace("| victims =", "|victims=").replace("| beginyear =", "|beginyear=")
    return re.sub(reg_ref, '', input)

"""Fonction pour trouver tous les tueurs"""
def getKiller(input):
    find = False
    killer = ""
    killerList = []
    
    for i in input:
        if (i[0] == "|"):
            find = False
            if (len(killer) != 0):
                killerList.append(killer)
                killer = ""
        elif (i[0] == "|name="):
            find = True
        
        if find == True and (i[1] == "NNP" or i[1] == "NNS"):
            killer = killer + " " + i[0]   
            print(killer)
        
    return killerList

"""Fonction pour trouver tous les tueurs"""
def getNbVictims(input):
    find = False
    nbVictims = ""
    victimsList = []
    victimsList.append("non répertorié")
    
    for i in input:
        if (i[0] == "|"):
            find = False
        elif (i[0] == "|victims="):
            find = True
            if (len(nbVictims) != 0):
                victimsList.append(nbVictims)
                nbVictims = ""
        
        if find == True and (i[1] == "NNP" or i[1] == "NNS"):
            nbVictims = nbVictims + i[0]            
        
    return victimsList
     
"""Fonction pour trouver tous les tueurs"""
def getDate(input):
    find = False
    date = ""
    dateList = []
    dateList.append("non répertorié")
    
    for i in input:
        if (i[0] == "|"):
            find = False
        elif (i[0] == "|beginyear="):
            find = True
            if (len(date) != 0):
                dateList.append(date)
                date = ""
        
        if find == True and (i[1] == "NNP" or i[1] == "NNS"):
            date = date + i[0]            
        
    return dateList

""" Fonction pour POS tagger du texte """
def preprocess(input):
    text = nltk.word_tokenize(input)
    return nltk.pos_tag(text)


""" Appel des fonctions """
file = filechooser()
text = readXML(file)
cleanText = clearText(text)
tagged_cleanText = preprocess(cleanText)
print(cleanText)
killer = getKiller(tagged_cleanText)
date = getDate(tagged_cleanText)
victims = getNbVictims(tagged_cleanText)
print(killer, date, victims)
    

