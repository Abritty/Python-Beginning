# -*- coding: utf-8 -*-
"""
Created on Fri May  1 00:55:52 2020

@author: User
"""

sentence = input("Enter Sentence :")

vowels=['a','e','i','o','u']

vowel_count={}

for i in list(sentence):
    for j in vowels:
        if vowel_count.get(i) == None:
            vowel_count[i]=1
        else:
            vowel_count[i]
        