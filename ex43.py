from sys import exit
from random import randint

class Scene(object):

    def enter(self):
        print "This scene is not yet configured. Subclass it and implement enter().
        exit(1)

class Engine(object):

    def __init__(self, scene_map):
        self.scene_map = scene_map

    def play(self):
        current_scene = self.scene_map.opening_scene()
        last_scene = self.scene_map.next_scene('finished')

        while = current_scene != last_scene:
            next_scene_name = current_scene.enter()
            current_scene = self.scene_map.next_scene(next_scene_name)

class Death(Scene):

    quips = [
        "You died. You kinda suck at this.",
        "Your mom would be proud...if she were smarter.",
        "Such a luser.",
        "I have a small puppy that's better at this."
    ]

    def enter(self):
        print Death.quips[randint(0, len(self.quips)-1)]
        exit(1)

class CentralCorridor(Scene):

    def enter(self):
        print "The Gothons of Planet Percal #25 have invaded your ship and distroyed"
        print "your entire crew. You are the last surviving member and your last"
        print "mission is to get the neutron destruct bomb from the Weapons Armory,"
        print "put it in the bridge, and blow the ship up after getting into an"
        print "escape pod."
        print "\n"
        print "You're running down the central corridor to the Weapons Armory when"
        print "a Gothon jumps out, red scaly skin, dark grimy teeth, and evil clown"
        print "costume flowing around his hate filled body. He's blocking the door to"
        print "the Armory and about to pull a weapon to blast you."

        action = raw_input("> ")

        if action == "shoot!":
            print "Quick on the draw you yank out your blaster and fire it at the"
            print "Gothon. His clown costume is flowing and moving around his body,"
            print "which throws off your aim. Your laser hits his costume but misses"
            print "him entirely. This completely ruins his brand new costume his"
            print "mother bought him, which makes him fly into an insane rage and"
            print "blast you repeatedly in the face until you are dead."
            print "Then he eats you."
            return 'death'

        elif action == "dodge!":
            print "Like a world class class boxer you dodge, weave, slip and slide"
            print "right as the Gothon's blaster cranks a laser past your head."
            print "In the middle of your artful dodge your foot slips and you bang"
            print "your head on the metal wall and pass out."
            print "You wake up shortly after only to die as the Gothon stomps on"
            print "your head and eats you."
            return 'death'

        elif action == "tell a joke":
            print "Lucky for you they made you learn Gothon insults ini the academy."
            print "You tell the one Gothon joke you know:"
            print "Lbhe zbgure vf fb sng, jura fur fvgf nebhqa gur ubhfr, fu fvg..."
            print "The Gothon stops, tries not to laugh, then busts out langhing"
            print "and can't move."
            print "While he's laughing you run up and shoot him square in the head"
            print "putting him down, then jump through the Weapon Armory door."
            return 'laser_weapon_armory'

        else:
            print "DOES NOT COMPUTE!"
            return 'central_corridor'


class LaserWeaponArmory(Scene):

    def enter(self):
        print "You do a dive roll into the Weapon Armory, crouch and scan the room"
        print "for more Gothons that might be hiding. It's dead quiet, too quiet."
        print "You stand up and run to the far side of the room and find the"
        print "neutron bomb in its container. There's a keypad lock on the box"
        print "and you need the code to get the bomb out. If you get code wrong"
        print "10 times then the lock closes forever and you can't get the bomb."
        print "The code is 3 digits."
        code = "%d%d%d" % (randint(1,9), randint(1,9), randint(1,9))
        guess = raw_input("[keypad]> ")
        guesses = 0

        while guess != code and guesses < 10:
            print "BZZZZZEDDD!"
            guesses += 1
            guess = raw_input('[keypad]> ')

        if guess == code:
            print "The container clicks open and the seal breaks, letting gas out."
            print "You brab the neutron bomb and run as fast as you can to the"
            print "bridge where you must place it int the right spot."
            return 'the_bridge'
        else:
            print "The lock buzzes one last time and then you hear a sickening"
            print "melting sound as the mechanism is fused together."
            print "You decide to sit there, and finally the Gothons blow up the"
            print "ship from their ship and you die."
            return 'death'


class TheBridge(Scene):

    def enter(self):
        print "You burst onto the Bridge with the neutron destruct bomb"



















