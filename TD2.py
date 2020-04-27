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
regPattern = "<ref.*>.*\n*.*</ref.*>"
filetypes = [('Document XML','*.xml')] # Type de fichier pour le filechooser

""" Fonction pour ouvrir le fichier XML """
def filechooser():
    Tk().withdraw()
    filename = askopenfilename(filetypes=filetypes)
    print(filename)
    return filename

""" Fonction pour récupérer le contenu de la balise <text> du XML """
def readXML(filename) :
    file = minidom.parse(filename)
    text = file.getElementsByTagName('text')[0].childNodes[0].nodeValue
    return text

""" Fonction qui nettoie le texte"""
def clearText(text):
    clean_text = re.sub(regPattern, '', text)
    return clean_text
    

""" Fonction pour POS tagger du texte """
def preprocess(input):
    text = nltk.word_tokenize(input)
    return nltk.pos_tag(text)


""" Appel des fonctions """
file = filechooser()
text = readXML(file)
cleanText = clearText(text);
print(cleanText)

tokens = preprocess(cleanText)



"""
arbre = nltk.ne_chunk(tokens, binary=True)

subtrees = arbre.subtrees()

entities = []
for sub in subtrees:
    if sub.label() == 'NE':
        entities.append(sub)
        
for entity in entities:
    print(entity)

"""
