# -*- coding: utf-8 -*-
"""
Created on Thu Nov  7 12:22:38 2019

@author: erwan.begoc
"""

def radiocode(code):
    mydict={'A':'Alpha',
            'B':'Bravo',
            'C':'Charly',
            'D':'Delta',
            'E':'Echo',
            'F':'Freddy',
            'G':'Golf',
            'H':'Hotel',
            'I':'India',
            'J':'Juliet',
            'K':'Kilo',
            'L':'Lima',
            'M':'Mike',
            'N':'November',
            'O':'Oscar',
            'P':'Papa',
            'Q':'Quebec',
            'R':'Romeo',
            'S':'Sierra',
            'T':'Tango',
            'U':'Uniform',
            'V':'Victor',
            'W':'Whisky',
            'X':'X-Ray',
            'Y':'Yankee',
            'Z':'Zulu'         
            }
    
    for i in code.upper():
        print(mydict.get(i,i))


myinput = input("What sentence do you want to encode :")
radiocode(myinput)