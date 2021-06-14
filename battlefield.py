# region Imports
import random

from dinosaur import Dinosaur
from fleet import Fleet
from herd import Herd

# endregion

# region BattleField class
from robot import Robot


class BattleField:
    chosen_side = ""

    # region Constructor
    def __init__(self):
        self.robot_fleet = Fleet().create_fleet()  # The fleet of robots
        self.dino_herd = Herd().create_herd()  # The herd of dinosaurs
        self.game_status = False  # The current status of the game, false if not running
        self.winner = ""  # The winner of the rumble : Dinosaur or Robot
        self.chosen_side = ""  # Indicates the side the user is on.
        self.user_dinosaur = Dinosaur("", 0)  # An empty dino object
        self.user_robot = Robot("")  # An empty robot object
        self.current_dino_opponent = Dinosaur("", 0)  # The dino opponent
        self.current_robot_opponent = Robot("")  # The robot opponent
        self.user_current_position = 0  # The position of the user dino or robot in fleet or herd
        self.opponent_current_position = 0  # The robot or dino opponent position
        self.scare_count = 0  # The total amount of times intimidation attack was used

    # endregion

    # region Run_Game
    def run_game(self):
        #  While the game_status is true, the game will run. When false, it's over.
        self.game_status = True
        while self.game_status:
            print(self.display_welcome())
            print("Choose your species!")
            #  The player decides what side they want to be on.
            userInput = input("Enter 'Dino' or 'Robot':\n")
            self.set_chosen_side(userInput)  # What side is the user on?

            #  Depending on the choice, the user will step into that experience.
            if userInput.lower() == "dino":
                print("You picked the dino species!\n")
            elif userInput.lower() == "robot":
                print("You picked the robot side!\n")
            else:
                #  Must be a valid side, or else you will be in an endless loop!
                print("That's not a dino or a robot. Try again, bud!")
                #  Start the game based on the side the user chose in userInput.

            #  The game_status is determined by the outcome of the battle.
            self.game_status = self.battle(self.chosen_side)

    # endregion

    # region Set_Chosen_Side (Dino or Robot)
    def set_chosen_side(self, dino_or_robot):  # Takes in a string "dino" or "robot"
        self.chosen_side = dino_or_robot  # Indicates which side the user is on
        #  They are either on the Dinosaur side or the Robot side.

    # endregion

    # region Display_Welcome
    def display_welcome(self):
        """
        Simply returns the welcome string.
        :return: Welcome message
        """
        return "Welcome to Robots vs Dinosaurs!"

    # endregion

    # region Battle
    def battle(self, chosen_side):
        """
        The outcome of the battle in run_game() decides the winner.
        Once they choose their side, then the user will be able to battle against
        either the robot fleet or the dinosaur herd.
        :param chosen_side: Is the chosen side that the user wants to be on.
        :return: The outcome/status of the game. False when winner is declared.
        """
        outcome = True  # Current status of the game
        rand = random.randint(0, 3)  # Assists with choosing a random opponent

        if chosen_side.lower() == "dino":
            print("This is your randomly chosen dinosaur champion:\n")
            for index in range(0, len(self.dino_herd)):
                if index == rand:
                    print(f"{self.dino_herd[index].type}\n\n")
                    self.user_dinosaur = self.dino_herd[index]
                    break

            print("Now that you have your champion, let's fight against the\n"
                  "fleet of robots!\n")

            print("You'll find your attack options below. Right now, you're \n"
                  "up against the first robot in the fleet: ")

            new_robot_fleet = Fleet().create_fleet()
            for robot_pos in range(0, len(new_robot_fleet)):
                if robot_pos == self.opponent_current_position:
                    print("\n" + new_robot_fleet[robot_pos].name + "\n")
                    #  Set the initial robot opponent against the dino contender
                    self.current_robot_opponent = new_robot_fleet[robot_pos]
                    break

            print("Here are your attack choices:")
            self.scare_count = 0

            # Pass in the current number of "stunt" attacks. If greater than 0, stunt can't be used.
            # Once the robot opponent has been defeated, then the next robot resets scare_count to 0.

            self.show_dino_opponent_options(self.current_robot_opponent, self.scare_count)

            outcome = False  # New status of the game, False once winner decided

        # Enter elif choice.lower() == "robot" only if user chooses to go the robot route.
        elif chosen_side.lower() == "robot":  # outcome will be false, always.
            print("This is your randomly chosen robot champion:\n")
            for index in range(0, len(self.robot_fleet)):
                if index == rand:
                    print(f"Your champion is: {self.robot_fleet[index].name}")
                    self.store_robot_position = index
                    break
            print("Now that you have your champion, let's fight against the\n"
                  "herd of dinosaurs!")

            outcome = False  # New status of the game, False once winner decided
        return outcome

    # endregion

    # region Dino_Turn
    def dino_turn(self, robot_or_dino_opponent, number):
        if number == 1 or self.current_robot_opponent.health <= 0:

            print("The dino attacked with headbutt!\n")

            random_damage = random.randint(0, 30)

            robot_or_dino_opponent.injury(random_damage)  # Injure the robot
            #  Set the incoming robot_or_dino opponent object = to the current robot fighting
            self.current_robot_opponent = robot_or_dino_opponent

            print(f"Now, {robot_or_dino_opponent.name} has only "
                  f"{robot_or_dino_opponent.health} health!")  # Robot health

            print(f"It's now {robot_or_dino_opponent.name}'s turn to"
                  f" attack!")  # Robot turn to attack

            robot_or_dino_opponent.attack(self.user_dinosaur)

            print(f"Your dinosaur's current health is: {self.user_dinosaur.health}")

            self.show_dino_opponent_options(self.current_robot_opponent, number)

        elif number == 2:
            print("The dino attacked with scratch!")

        elif number == 1 and self.current_robot_opponent.health == 0:
            print("The robot has been destroyed! On to the next, boi!")

        elif number == 1 and self.user_dinosaur >= 0:
            print("Looks like you lost, bud! Try again next time.")
            print("End Game")



    # endregion

    # region Robo_Turn
    def robo_turn(self):
        pass

    # endregion

    # region Show_Dino_Opponent_Options
    def show_dino_opponent_options(self, robot_or_dino_opponent, count):
        #  The robot_or_dino_opponent can be either a Robot() or a Dinosaur()
        #  The count simply keeps track of the amount of type "3" attacks allowed
        print("\n1. Use headbutt\n")
        print("2. Use scratch\n")
        print("3. Use intimidate\n")
        type_of_attack = input(f"\nEnter one of the options above "
                               f"to attack {robot_or_dino_opponent.name}:\n")
        if type_of_attack == "1":
            print("The user chose headbutt!")
            count = 0
            self.dino_turn(robot_or_dino_opponent, 1)
        elif type_of_attack == "2":
            count = 0
            print("The user chose scratch!")
            self.dino_turn(robot_or_dino_opponent, 2)
        elif type_of_attack == "3" and count < 1:
            print("The user made the robot spill some "
                  "oil. No damage caused, but the "
                  "robot is too scared to play their turn.")
            print("You get to go again!")
            count = count + 1
            self.show_dino_opponent_options(robot_or_dino_opponent, count)
        elif type_of_attack == "3" and count == 1:
            print("You can no longer use that attack. "
                  "You will have to choose another form "
                  "of attacking.")
            self.show_dino_opponent_options(robot_or_dino_opponent, count)
        else:
            print("That's not a type of attack. Enter a valid choice!!")

    # endregion

    # region Show_Robo_Opponent_Options
    def show_robo_opponent_options(self):
        print("Choose your next action!")
        print("Will you attack?")
        userInput = input("Type in 'yes' or 'no': ")
        if userInput == "yes":
            print("The user chose to attack!")
        elif userInput == "no":
            print("The user chose not to attack!")

    # endregion

    # region Display_Winners
    def display_winners(self):
        the_winner = "The person who won the battle. Need to keep coding!"
        return the_winner
    # endregion

# endregion
