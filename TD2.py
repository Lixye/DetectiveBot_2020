# -*- coding: utf-8 -*-
"""
Created on Fri Feb  7 17:51:56 2020

@author: Lucille
"""
import nltk

text = "The decision by the independent MP Andrew Wilkie to withdraw his support for the minority Labor government sounded dramatic but it should not further threaten its stability. When, after the 2010 election, Wilkie, Rob Oakeshott, Tony Windsor and the Greens agreed to support Labor, they gave just two guarantees: confidence and supply."

def preprocess(input):
    text = nltk.word_tokenize(input)
    return nltk.pos_tag(text)

tokens = preprocess(text)

arbre = nltk.ne_chunk(tokens, binary=True)

subtrees = arbre.subtrees()

entities = []
for sub in subtrees:
    if sub.label() == 'NE':
        entities.append(sub)
        
for entity in entities:
    print(entity)
