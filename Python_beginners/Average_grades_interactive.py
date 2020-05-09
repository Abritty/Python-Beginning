# -*- coding: utf-8 -*-
"""
Created on Fri May  1 00:28:09 2020

@author: Shafia
"""

import math

grades = []
index =0

while True :
    print("Enter your choice :")
    print("Enter grade --> 1")
    print("List grades --> 2")
    print("delete grades --> 3")
    print("Exit --> 6")
    
    choice =input("-->")
    
    if not(len(choice) == 1 and choice.isnumeric()):
        print("Enter a valid choice.")
        continue
    
    if int(choice)==6:
        break
        
    
    if int(choice)==1:
        print("Enter 'e' to exit .")
        while True:
            grade = input("-->")
            
            if grade == 'e' :
                break
            else:
                grade=float(grade)
                grades.append(grade)
                
    if int(choice)==2:
        for grade in grades:
            print(grade)
            
    if int(choice)==3:
        for grade in grades:
            print(grade)
            
        
        index=int(input("Enter Index-->"))
     
        if index<=len(choice)-1 and index>=0:

            grades.pop(index)
        else:
            print("Enter valid index.")
        
    
    

