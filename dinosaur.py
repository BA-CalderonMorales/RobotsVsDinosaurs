from robot import Robot


class Dinosaur:
    def __init__(self, type, attack_power):
        self.type = type
        self.power_level = attack_power
        self.energy = 100
        self.health = 100

    def attack(self, Robot):
        """Decrease robot health"""
        robot = Robot
        robot.injury(10)

    def injury(self, damage):
        """Inflict damage to the Robot"""
        self.health = self.get_health() - damage

    def get_name(self):
        return self.type

    def get_power(self):
        return self.power_level

    def get_weapon(self):
        return self.energy

    def get_health(self):
        return self.health
