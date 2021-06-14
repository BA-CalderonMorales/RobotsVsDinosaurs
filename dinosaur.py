# region Dinosaur class
class Dinosaur:
    # region Constructor
    def __init__(self, type, attack_power):
        self.type = type
        self.power_level = attack_power
        self.energy = 100
        self.health = 100
    # endregion

    # region Attack
    def attack(self, Robot):
        """Decrease robot health"""
        robot = Robot
        robot.injury(10)
    # endregion

    # region Injury
    def injury(self, damage):
        """Inflict damage to the Robot"""
        self.health = self.get_health() - damage
    # endregion

    # region Get_Name
    def get_name(self):
        return self.type
    # endregion

    # region Get_Power
    def get_power(self):
        return self.power_level
    # endregion

    # region Get_Weapon
    def get_weapon(self):
        return self.energy
    # endregion

    # region Get_Health
    def get_health(self):
        return self.health
    # endregion

# endregion