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
    input = input.replace("[", "").replace("]", "").replace("*", "").replace("| name =", "|name=")
    return re.sub(reg_ref, '', input)

"""Fonction pour trouver tous les tueurs avec la lettre M"""
def getKiller(input):
    find = False
    killer = ""
    
    for i in input:
        if (i[0] == "|"):
            find = False
        elif (i[0] == "|name="):
            find = True
            if (len(killer) != 0):
                killer = killer + "\n"
        
        if find == True and (i[1] == "NNP" or i[1] == "NNS"):
            killer = killer + " " + i[0]            
        
    return killer
     
"""Fonction qui trouve les victimes d'un tueur"""
def getVictims(input):
    find = False
    victims = ""
    for i in input:
        if (i[0] == "|"):
            find = False
        elif (i[0] == "|victims="):
            find = True
            if (len(victims) != 0):
                victims = victims + "\n"
        
        if find == True and (i[1] == "NUM" or i[1] == "NNS"):
            victims = victims + " " + i[0]
            
    return victims

""" Fonction pour POS tagger du texte """
def preprocess(input):
    text = nltk.word_tokenize(input)
    return nltk.pos_tag(text)


""" Appel des fonctions """
file = filechooser()
text = readXML(file)
cleanText = clearText(text)
tagged_cleanText = preprocess(cleanText)
killer = getKiller(tagged_cleanText)
victims = getVictims(tagged_cleanText)
print(killer + " " + victims)
    

