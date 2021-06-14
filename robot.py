# region Imports
import random
from weapon import Weapon
# endregion

# region Robot class
class Robot:
    # region Constructor
    def __init__(self, name):
        self.name = name
        self.power_level = 100
        self.health = 25
        self.weapon = self.random_weapon()
    # endregion

    # region Set_Name
    def set_name(self, name):
        self.name = self.get_name()
    # endregion

    # region Attack
    def attack(self, Dinosaur):
        """Decrease Dinosaur health"""
        dino = Dinosaur
        random_damage = random.randint(0, 30)
        dino.injury(random_damage)
    # endregion

    # region Injury
    def injury(self, damage):
        """Inflict damage to the Dinosaur"""
        self.health = self.get_health() - damage
    # endregion

    # region Get_Name
    def get_name(self):
        return self.name
    # endregion

    # region Get_Power
    def get_power(self):
        return self.power_level
    # endregion

    # region Get_Health
    def get_health(self):
        return self.health
    # endregion

    # region Random_Weapon
    def random_weapon(self):
        all_weapons = ["Shot gun", "Machine Gun", "Lazer", "Baseball Bat"]
        weapon_levels = [10, 20, 30, 40]  # Bats are op in my game
        rand = random.randint(0, 3)
        choice = self.find_weapon(all_weapons[rand], weapon_levels[rand])
        return choice
    # endregion

    # region Find_Weapon
    def find_weapon(self, choice, level):
        random_weapon = Weapon(choice, level)
        """
        Returns a specific (but random) weapon, based off of 
        user creating a robot.
        """
        return random_weapon
    # endregion

# endregion