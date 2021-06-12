import random

from weapon import Weapon


class Robot:
    health = 0
    def __init__(self, name):
        self.name = name
        self.power_level = 100
        self.health = 100
        self.weapon = self.random_weapon()

    def set_name(self, name):
        self.name = self.get_name()

    def attack(self, Dinosaur):
        """Decrease Dinosaur health"""
        dino = Dinosaur
        dino.injury(10)

    def injury(self, damage):
        """Inflict damage to the Dinosaur"""
        self.health = self.get_health() - damage

    def get_name(self):
        return self.name

    def get_power(self):
        return self.power_level

    def get_health(self):
        return self.health

    def random_weapon(self):
        all_weapons = ["Shot gun", "Machine Gun", "Lazer", "Baseball Bat"]
        weapon_levels = [10, 20, 30, 40] # Bats are op in my game
        rand = random.randint(0, 3)
        choice = self.find_weapon(all_weapons[rand], weapon_levels[rand])
        return choice

    def find_weapon(self, choice, level):
        random_weapon = Weapon(choice, level)
        """
        Returns a specific (but random) weapon, based off of 
        user creating a robot.
        """
        return random_weapon