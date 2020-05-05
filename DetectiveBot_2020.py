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
    input = input.replace("[", "").replace("]", "").replace("{", "").replace("}", "").replace("*", "* ").replace(":", ": ")
    return re.sub(reg_ref, '', input)

""" Fonction pour POS tagger du texte """
def preprocess(input):
    text = nltk.word_tokenize(input)
    return nltk.pos_tag(text)

"""Fonction pour trouver tous les tueurs"""
def getKiller(input):
    find = False
    letterM = False
    getInformation = False
    testKiller = []
    killerListWithM = []
    allInformation = []
    information = []
    
    for i in input:
        if (i[0] == ":"):
            find = False
            if (len(testKiller) != 0):
                letterM = False
                for killer in testKiller:
                    if (killer[0] == "M" and letterM == False):
                        killerListWithM.append(testKiller)
                        letterM = True
                        getInformation = True
                testKiller = []
        elif (i[0] == "*"):
            find = True 
        elif find == True and (i[1] == "NNP" or i[1] == "NNS"):            
            testKiller.append(i[0]) 
            
        """Pour trouver les informations"""
        if(i[1] != '.' and getInformation == True):
            information.append(i)
        elif (getInformation == True) :
            allInformation.append(information)
            getInformation = False
            information = []  
    show(killerListWithM, allInformation)

"""Fonction pour afficher les résultats"""
def show(killerListWithM, allInformation):
    name = ""
    k = -1
    details(allInformation[k])
    for listK in killerListWithM:
        for i in listK:
            name += i + " "
        print(name + ":")
        details(allInformation[k])
        name = ""
        k = k + 1

"""Fonction pour afficher les détails de la liste informations"""
def details(information):
    affichage = ""
    for i in information: 
        print
        affichage += i[0] + " "
    affichage += "\n\n"
    print(affichage)
    return affichage
        
""" Appel des fonctions """
file = filechooser()
text = readXML(file)
cleanText = clearText(text)
tagged_cleanText = preprocess(cleanText)
killer = getKiller(tagged_cleanText)

    

