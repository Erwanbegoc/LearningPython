from sys import exit
from random import randint

class Scene(object):
    
    def enter(self):
        print("Scene is not yet configured, subclass it and implement enter().")
        exit(1)
        
class Engine(object):

    def __init__(self, scene_map):
        self.scene_map = scene_map
    def play(self):
        current_scene = self.scene_map.opening_scene()
        
        while True:
            print("\n-----------")
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
        
        action = input("do you: a - Shoot, b - Dodge, c - tell a joke -> "  )
        
        if action == "a":
            print("You Miss!")
            return 'death'
        
        elif action == "b":
            print("you trip, and bang your head!")
            return 'death'
        
        elif action == "c":
            print("you make him laugh, to death!")
        else:
            print("Does not compute")
            return 'Central_corridor'

class LaserWeaponArmory(Scene):

    def enter(self):
            print("You dive roll into the Weapon Armory")
            print("The bomb is there, unlock the keypad, 10 tries, 3 digits, do it!")
            code = "%d%d%d" % (randint(1,9), randint(1,9), randint(1,9))
            guess = raw_input("[KEYPAD]> ")
            guesses = 0

            while guess != code and guesses < 10:
              print("BZZZEEEDDD!")
              guesses += 1
              guess = raw_input("[KEYPAD]> ")
            if guess == code:
                print("the container opens, you grab the bomb and run to the bridge")
                return 'the_bridge'
            else:
                print("the locks seals, you're dead")
                return 'death'
class TheBridge(Scene):

        def enter(self):
            print("you burst onto the bridge and see some gothons")

            action = raw_input("do you T - throw the bomb or P - Slowly place the bomb >")

            if action == "T":
                print("the bomb goes off, you all die")
                return 'death'

            elif action == "P":
                print("You place the bomb and escape to the pod")
                return 'finished'
class Map(object):

        scenes = {
            'central_corridor' : CentralCorridor(),
            'laser_weapon_armory' : LaserWeaponArmory(),
            'the_bridge' : TheBridge(),
            'death' : Death()}

        def __init__(self, start_scene):
            self.start_scene = start_scene

        def next_scene(self, scene_name):
            return Map.scenes.get(scene_name)

        def opening_scene(self):
            return self.next_scene(self.start_scene)

a_map = Map('central_corridor')
a_game = Engine(a_map)
a_game.play()