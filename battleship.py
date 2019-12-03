# -*- coding: utf-8 -*-
"""
Created on Mon Nov 11 15:27:57 2019

@author: erwan.begoc

"""

class Battleship:
    
    def __init__(self,x,pos,ort):
        self.x = x
        self.pos = pos
        self.ort = ort
        
    def shiplength(self,x):
        if x == "S":
            return 1
        elif x == "C":
            return 2
        elif x == "D":
            return 3
        elif x == "A":
            return 4
        else: print("invalid ship denomination")
       
    def refshorz(self,pos,length):
        a = []
        for i in range(length):
            a.append(str(chr(ord(pos[0])+i)+pos[1]))
        
        return a
            
    def refsvert(self,pos,length):
        a = []
        for i in range(length):
            a.append(pos[0]+str(int(pos[1])+i))
        
        return a
            