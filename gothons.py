from sys import exit
from random import randint

class Scene(object):
    
    def enter(self):
        print "Scene is not yet configured, subclass it and implement enter()."
        exit(1)
        
class Engine(object):

    def __init__(self, scene_map):
        self.scene_map = scene_map
    def play(self):
        current_scene = self.scene_map.opening_scene()
        
        while True:
            print "\n-----------"
            next_scene_name = current_scene.enter()
            current_scene = self.scene_map.next_scene(next_scene_name)
class Death(Scene): 
    
    quips = [
        "You died, too bad",
        "better luck next time",
        "You kinda suck, right?",
        "my 2 year old could do better"
    ]               
    def enter(self):
        print(Death.quips[randint(0,len(self.quips)-1)])
        exit(1)

class CentralCorridor(Scene):
    def enter(self):
        print("the Gothons has invaded you ship and destroyed")
        print("your entire crew. You are the last surviving member")
        print("Get to the Weapons Armory, blow the ship and Escape!")
        print("\n")
        print("you are on your way when a gothon pulls a weapon on you")
        
        action = input(">do you: a - Shoot, b - Dodge, c - tell a joke"  )  
        
        if action == "a"
            print("You Miss!")
            return 'death'
        
        elif action == "b"
            print("you trip, and bang your head!")
            return 'death'
        
        elif action == "c"
            print("you make him laugh")
                