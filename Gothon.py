# -*- coding: utf-8 -*-
"""
Created on Tue Nov 19 12:47:39 2019

@author: erwan.begoc
"""
from sys import exit
from random import randint

class Scene(object):
    
    def enter(self):
        print "This is is not yet configured"
            exit(1)

class engine(object):
    
    def __init__(self, scene_map):
        self.scene_map = scene_map
        
    def play(self):
        current_scene = self.scene_map.opening_scene()
        
        while True:
            print "\n----------"
            next_scene_name = surrent_scene.enter()
            current_scene = self.scene_map.next_scene(next_scene_name)

class Death(Scene):
    
    quips = [
            "You died, you suck",
            "Your mom would be proud",
            "Why don't you play PacMan instead",
            "Stick to what you know"
            ]
    
    def enter(self):
        print(Death.quips[randint(0,len(self.quips)-1)])
        exit(1)

class CentralCorridor(Scene):
    
    def enter(self):
        print("The Gothons have entered the ship and killed the entire crew")
        print("Your mission is to get the bomb from the Armory, put it in")
        print("The bridge, escape and blow the ship")
        print("\n")
        print("You're in the Corridor, a Gothon is blocking access to the")
        print("Armory and about to pull a weapon")

        action = raw_input("Do you Shoot, Dodge, or Joke =-> ")
        
        if action == "Shoot":
            print("You shoot, You miss, You Die!")
            return 'death'

        elif action == "Dodge":
            print("You Dodge, You slip, You Die!")
            return 'death'

        elif action == "Joke":
            print("The Joke is brilliant, you blast him and walk past")
            return 'laser_weapon_armory'
        else:
            print("Does not Compute")
            return 'central_corridor'               



























