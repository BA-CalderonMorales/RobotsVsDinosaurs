from dinosaur import Dinosaur
from robot import Robot
import random

# Used to populate a random dinosaur or robot type
random_number = random.randint(0, 2)

class BattleField:
    def __init__(self):
        self.fleet = list()
        self.herd = list()
        self.game_status = False

    def run_game(self):
        self.game_status = True
        if self.game_status:
            print(self.display_welcome())

            # Create the random dinosaur herd

            # Create the random robot fleet

            # Do something with this information.


    def display_welcome(self):
        return "Welcome to Robots vs Dinosaurs!"

    def battle(self):
        pass

    def dino_turn(self):
        pass

    def robo_turn(self):
        pass

    def show_dino_opponent_options(self):
        print("Choose your next action!")
        print("Will you attack?")
        userInput = input("Type in 'yes' or 'no': ")
        if userInput == "yes":
            print("The user chose to attack!")
        elif userInput == "no":
            print("The user chose not to attack!")

    def show_robo_opponent_options(self):
        print("Choose your next action!")
        print("Will you attack?")
        userInput = input("Type in 'yes' or 'no': ")
        if userInput == "yes":
            print("The user chose to attack!")
        elif userInput == "no":
            print("The user chose not to attack!")

    def display_winners(self):
        pass