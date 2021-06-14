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
        self.taunt = False  # The total amount of times intimidation attack was used

    # endregion

    # region Run_Game
    def run_game(self):
        #  While the game_status is true, the game will run. When false, it's over.
        self.game_status = True
        while self.game_status:
            print(self.display_welcome())
            print("Choose your species!")
            #  The player decides what side they want to be on.
            userInput = input("Enter 'Dino' or 'Robot':\n\n")
            self.set_chosen_side(userInput)  # What side is the user on?

            #  Depending on the choice, the user will step into that experience.
            if userInput.lower() == "dino":
                print("\nYou picked the dino species!\n")
            elif userInput.lower() == "robot":
                print("\nYou picked the robot side!\n")
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
        return "Welcome to Robots vs Dinosaurs!\n" \
               "\n*******************************************************\n" \
               "The goal is to defeat all the enemies in the \n" \
               "fleet of robots or the herd of dinosaurs, depending \n" \
               "on the side you choose below. Good luck trying to \n" \
               "defeat all of your opponents. You'll need it!\n" \
               "\n*******************************************************\n"

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

        #  The user decides that they wish to be an ally of the dinosaurs
        if chosen_side.lower() == "dino":
            print("This is your dinosaur herd:\n")
            for index in range(0, len(self.dino_herd) - 1):
                print(f"{self.dino_herd[index].type}")
                if index == self.user_current_position:
                    self.user_dinosaur = self.dino_herd[index]
            print(f"\n*******************************************************\n\n"
                  f"Your first champion up to bat is {self.user_dinosaur.type}.\n"
                  f"Let's fight against the fleet of evil robots!\n")
            print("You'll find your attack options below. Right now, you're \n"
                  "up against the first robot in the fleet: ")
            #  Create a new robot fleet, get the robot that is up first in the fleet
            new_robot_fleet = Fleet().create_fleet()
            for robot_pos in range(0, len(new_robot_fleet)):
                #  The self.opponent_current_position will be used whenever needed
                #  to find the current robot that is battling.
                if robot_pos == self.opponent_current_position:
                    print("\n" + new_robot_fleet[robot_pos].name)
                    #  Set the initial robot opponent against the dino contender
                    self.current_robot_opponent = new_robot_fleet[robot_pos]
                    break
            #  Print out attack choices
            print("\n*******************************************************\n\n"
                  "Here are your attack choices:")
            self.show_dino_opponent_options(self.current_robot_opponent, self.taunt)
            # New status of the game, False once winner decided
            outcome = False

        # The user decides that they wish to be an ally of the robots
        elif chosen_side.lower() == "robot":  # outcome will be false, always.
            print("This is your randomly chosen robot champion:\n")
            for index in range(0, len(self.robot_fleet) - 1):
                print(f"{self.robot_fleet[index].name}")
                if index == self.user_current_position:
                    self.user_robot = self.robot_fleet[index]
            print(f"\n*******************************************************\n\n"
                  f"Your first champion up to bat is {self.user_robot.name}. "
                  f"Let's fight against the herd of crazy dinosaurs!\n")
            print("You'll find your attack options below. Right now, you're \n"
                  "up against the first dinosaur in the herd: ")
            #  Create a new dinosaur herd, get the dino that is up first in the herd
            new_dino_herd = Herd().create_herd()
            for dino_pos in range(0, len(new_dino_herd)):
                #  The self.opponent_current_position will be used whenever needed
                #  to find the current dino that is battling.
                if dino_pos == self.opponent_current_position:
                    print("\n" + new_dino_herd[dino_pos].type)
                    #  Set the initial dino opponent against the robot contender
                    self.current_dino_opponent = new_dino_herd[dino_pos]
                    break
            #  Print out attack choices
            print("\n*******************************************************\n\n"
                  "Here are your attack choices:")
            self.show_robo_opponent_options(self.current_dino_opponent, self.taunt)
            # New status of the game, False once winner decided
            outcome = False
        return outcome

    # endregion

    # region Show_Dino_Opponent_Options
    def show_dino_opponent_options(self, opponent, scare):
        #  The opponent being a Robot()
        print("\n1. Use headbutt\n")
        print("2. Use scratch\n")
        print("3. Use intimidate\n"
              "\n*******************************************************\n")
        type_of_attack = input(f"Enter one of the options above "
                               f"to attack {opponent.name}:\n")
        #  Headbutt - count will always equal 0 - reverts count to 0, if 1
        if type_of_attack == "1":
            print("\n*******************************************************\n\n")
            self.current_robot_opponent = opponent
            self.dino_turn(opponent, 1)
        #  Scratch - count will always equal 0 - reverts count to 0, if 1
        elif type_of_attack == "2":
            print("\n*******************************************************\n\n")
            self.dino_turn(opponent, 2)
        #  Intimidate - count will only equal 0. Changes to 1, once used
        elif type_of_attack == "3" and scare == False:
            print(f"\n*******************************************************\n\n"
                  f"{self.user_dinosaur.type} made their opponent spill some "
                  f"oil. No damage caused, \nbut {self.current_robot_opponent.name} "
                  f"is too scared to play their turn.")
            print("\nYou get to go again!")
            self.taunt = True
            self.show_dino_opponent_options(opponent, self.taunt)
        #  Disable Intimidate if used consecutively, where count is == 1
        elif type_of_attack == "3" and scare == True:
            print("\n*******************************************************\n\n"
                  "You cannot use that attack in a consecutive fashion. "
                  "You will have to choose another form of attacking.")
            #  Only choosing a different form of attack will let you change the scare
            #  parameter back to False.
            self.show_dino_opponent_options(opponent, scare)
        #  Invalid choice
        else:
            print("\n*******************************************************\n\n"
                  "That's not a type of attack. Enter a valid choice!!")

    # endregion

    # region Show_Robo_Opponent_Options
    def show_robo_opponent_options(self, opponent, scare):
        #  The opponent being a Dinosaur()
        print("\n1. Use blaster\n")
        print("2. Use shockwave\n")
        print("3. Use educate\n"
              "\n*******************************************************\n")
        type_of_attack = input(f"Enter one of the options above "
                               f"to attack {opponent.type}:\n")
        #  Blaster - Reverts self.taunt to False
        if type_of_attack == "1":
            print("\n*******************************************************\n\n")
            self.current_dino_opponent = opponent
            self.robo_turn(opponent, 1)
        #  Shockwave - Reverts self.taunt to False
        elif type_of_attack == "2":
            print("\n*******************************************************\n\n")
            self.robo_turn(opponent, 2)
        #  Intimidate - Changes self.taunt to True.
        elif type_of_attack == "3" and scare == False:
            print(f"\n*******************************************************\n\n"
                  f"{self.user_robot.name} confused the dinosaur with modern"
                  f", 21st century education. No damage caused, \n"
                  f"but {self.current_dino_opponent.type} "
                  f"is too confused to play their turn.")
            print("\nYou get to go again!")
            self.taunt = True
            self.show_robo_opponent_options(opponent, self.taunt)
        #  Disable Intimidate if used consecutively, self.taunt still equal to True
        elif type_of_attack == "3" and scare == True:
            print("\n*******************************************************\n\n"
                  "You cannot use that attack in a consecutive fashion. "
                  "You will have to choose another form of attacking.")
            #  Only choosing a different form of attack will let you change the scare
            #  parameter back to False.
            self.show_robo_opponent_options(opponent, scare)
        #  Invalid choice
        else:
            print("\n*******************************************************\n\n"
                  "That's not a type of attack. Enter a valid choice!!")

    # endregion

    # region Dino_Turn
    def dino_turn(self, opponent, number):
        if number == 1:
            self.dino_option_one(opponent)
        elif number == 2:
            self.dino_option_two(opponent)

    # endregion

    # region Robo_Turn
    def robo_turn(self, opponent, number):
        if number == 1:
            self.robo_option_one(opponent)
        elif number == 2:
            self.robo_option_two(opponent)

    # endregion

    # region Helper method for robo_turn(self, robot_or_dino_opponent, number) - Blaster
    def robo_option_one(self, opponent):
        # Print the type of attack
        print(f"{self.user_robot.name} attacked with their {self.user_robot.weapon.type}!\n")
        random_damage = random.randint(0, 30)  # The damage will be any number between 0 and 30
        opponent.injury(random_damage)  # Injure the robot
        #  Set the incoming robot_or_dino opponent object = to the current robot fighting
        self.current_dino_opponent = opponent  # Assign to correct opponent object

        #  If the robots health and the dinosaur's health are both above 0, keep playing
        if self.current_dino_opponent.health > 0 and self.user_robot.health > 0:
            #  If the dino health and robot health are both above 0, and the user chooses num 1:
            print(f"Now, {opponent.type} has only "
                  f"{opponent.health} health!")  # Dino health
            print(f"It's now {opponent.type}'s turn to"
                  f" attack!")  # Dino turn to attack
            opponent.attack(self.user_robot)  # Dino attack (automatic)
            #  Outcome of last dino attack on robot
            print(f"{self.user_robot.name}'s current health is: {self.user_robot.health}")
            if self.taunt == True:
                self.taunt = False
                self.show_robo_opponent_options(self.current_dino_opponent, self.taunt)
            else:
                # self.taunt is already False, no change necessary
                self.show_robo_opponent_options(self.current_dino_opponent, self.taunt)

        #  The opponent's health is less than or equal to 0:
        elif self.current_dino_opponent.health <= 0 and self.user_robot.health > 0:
            #  Notify the user that the robot is destroyed and find the next one.
            print("The dinosaur has been obliterated! On to the next one!")
            self.user_current_position = self.user_current_position + 1  # Get the next position

            #  Create a new dino contender, only if the current position is less than the size of fleet
            if self.user_current_position < len(self.dino_herd) \
                    and self.dino_herd[self.opponent_current_position].type != "EndGame":
                new_dino_fighter = self.new_dino_opponent(self.user_current_position)
                self.taunt == False  # Update the taunt to False
                self.user_dinosaur.health = 100  # Update the health bar
                self.show_robo_opponent_options(new_dino_fighter, self.taunt)  # Pass the variables in
            elif self.dino_herd[self.opponent_current_position].type == "EndGame":
                print("\nIt looks like all the dinosaurs have been destroyed!")
                self.winner = "Robots"
                self.display_winners()
        #  The robot's health is less than or equal to 0, and there are still robots in the fleet
        elif self.user_robot.health <= 0 \
            and self.robot_fleet[self.user_current_position + 1].name != "EndGame":
            print(f"It appears that {self.robot_fleet[self.user_current_position].name} has fallen!")
            self.user_current_position = self.user_current_position + 1
            self.user_robot = self.robot_fleet[self.user_current_position]
            self.user_robot.health = 100
            print("Don't worry! There are still robots in your fleet!")
            print(f"The next robot in your fleet is: {self.user_robot.name}")
            self.taunt = False
            self.current_dino_opponent.health = 100
            self.show_robot_opponent_options(self.current_dino_opponent, self.taunt)
        #  The robot's health is less than or equal to 0, END GAME
        elif self.user_robot.health <= 0:
            print("\nLooks like you lost, bud! Try again next time.")
            self.winner = self.current_dino_opponent.type
            self.display_winners()
    # endregion

    # region Helper method for robo_turn(self, robo_or_dino_opponent, number) - Shockwave
    def robo_option_two(self, opponent):
        # Print the type of attack
        print(f"{self.user_robot.name} attacked with shockwave!\n")
        random_damage = random.randint(0, 30)  # The damage will be any number between 0 and 30
        opponent.injury(random_damage)  # Injure the robot
        #  Set the incoming robot_or_dino opponent object = to the current robot fighting
        self.current_dino_opponent = opponent  # Assign to correct opponent object

        #  If the robots health and the dinosaur's health are both above 0, keep playing
        if self.current_dino_opponent.health > 0 and self.user_robot.health > 0:
            #  If the dino health and robot health are both above 0, and the user chooses num 1:
            print(f"Now, {opponent.type} has only "
                  f"{opponent.health} health!")  # Dino health
            print(f"It's now {opponent.type}'s turn to"
                  f" attack!")  # Dino turn to attack
            opponent.attack(self.user_robot)  # Dino attack (automatic)
            #  Outcome of last dino attack on robot
            print(f"{self.user_robot.name}'s current health is: {self.user_robot.health}")
            if self.taunt == True:
                self.taunt = False
                self.show_robo_opponent_options(self.current_dino_opponent, self.taunt)
            else:
                # self.taunt is already False, no change necessary
                self.show_robo_opponent_options(self.current_dino_opponent, self.taunt)

        #  The opponent's health is less than or equal to 0:
        elif self.current_dino_opponent.health <= 0 and self.user_robot.health > 0:
            #  Notify the user that the robot is destroyed and find the next one.
            print("The dinosaur has been obliterated! On to the next one!")
            self.user_current_position = self.user_current_position + 1  # Get the next position

            #  Create a new dino contender, only if the current position is less than the size of fleet
            if self.user_current_position < len(self.dino_herd) \
                    and self.dino_herd[self.opponent_current_position].type != "EndGame":
                new_dino_fighter = self.new_dino_opponent(self.user_current_position)
                self.taunt == False  # Update the taunt to False
                self.user_dinosaur.health = 100  # Update the health bar
                self.show_robo_opponent_options(new_dino_fighter, self.taunt)  # Pass the variables in
            elif self.dino_herd[self.opponent_current_position].type == "EndGame":
                print("\nIt looks like all the dinosaurs have been destroyed!")
                self.winner = "Robots"
                self.display_winners()
        #  The robot's health is less than or equal to 0, and there are still robots in the fleet
        elif self.user_robot.health <= 0 \
            and self.robot_fleet[self.user_current_position + 1].name != "EndGame":
            print(f"It appears that {self.robot_fleet[self.user_current_position].name} has fallen!")
            self.user_current_position = self.user_current_position + 1
            self.user_robot = self.robot_fleet[self.user_current_position]
            self.user_robot.health = 100
            print("Don't worry! There are still robots in your fleet!")
            print(f"The next robot in your fleet is: {self.user_robot.name}")
            self.taunt = False
            self.current_dino_opponent.health = 100
            self.show_robot_opponent_options(self.current_dino_opponent, self.taunt)
        #  The robot's health is less than or equal to 0, END GAME
        elif self.user_robot.health <= 0:
            print("\nLooks like you lost, bud! Try again next time.")
            self.winner = self.current_dino_opponent.type
            self.display_winners()
    # endregion

    #  region Helper method for dino_turn(self, robot_or_dino_opponent, number) - Headbutt
    def dino_option_one(self, opponent):
        print(f"{self.user_dinosaur.type} attacked with headbutt!\n")  # Print the type of attack
        random_damage = random.randint(0, 30)  # The damage will be any number between 0 and 30
        opponent.injury(random_damage)  # Injure the robot
        #  Set the incoming robot_or_dino opponent object = to the current robot fighting
        self.current_robot_opponent = opponent  # Assign to correct opponent object

        #  If the robots health and the dinosaur's health are both above 0, keep playing
        if self.current_robot_opponent.health > 0 and self.user_dinosaur.health > 0:
            #  If the dino health and robot health are both above 0, and the user chooses num 1:
            print(f"Now, {opponent.name} has only "
                  f"{opponent.health} health!")  # Robot health
            print(f"It's now {opponent.name}'s turn to"
                  f" attack!")  # Robot turn to attack
            opponent.attack(self.user_dinosaur)  # Robot attack (automatic)
            #  Outcome of last robot attack on dino
            print(f"{self.user_dinosaur.type}'s current health is: {self.user_dinosaur.health}")
            if self.taunt == True:
                self.taunt = False
                self.show_dino_opponent_options(self.current_robot_opponent, self.taunt)
            else:
                # self.taunt is already False, no change necessary
                self.show_dino_opponent_options(self.current_robot_opponent, self.taunt)

        #  The opponent's health is less than or equal to 0:
        elif self.current_robot_opponent.health <= 0 and self.user_dinosaur.health > 0:
            #  Notify the user that the robot is destroyed and find the next one.
            print("The robot has been destroyed! On to the next one!")
            self.opponent_current_position = self.opponent_current_position + 1  # Get the next position

            #  Create a new robot contender, only if the current position is less than the size of fleet
            if self.opponent_current_position < len(self.robot_fleet) \
                    and self.robot_fleet[self.opponent_current_position].name != "EndGame":
                new_robot_fighter = self.new_robot_opponent(self.opponent_current_position)
                self.taunt = False  # Update the taunt to False
                self.user_dinosaur.health = 100  # Update the health bar                 -------
                self.show_dino_opponent_options(new_robot_fighter, self.taunt)  # Pass the variables in
            elif self.robot_fleet[self.opponent_current_position].name == "EndGame":
                print("\nIt looks like all the robots have been annihilated!")
                self.winner = "Dinosaurs"
                self.display_winners()

        #  The dinosaur's health is less than or equal to 0, and there are still dinosaurs in the herd
        elif self.user_dinosaur.health <= 0 and self.dino_herd[self.user_current_position + 1].type != "EndGame":
            print(f"It appears that {self.dino_herd[self.user_current_position].type} has fallen!")
            self.user_current_position = self.user_current_position + 1
            self.user_dinosaur = self.dino_herd[self.user_current_position]
            self.user_dinosaur.health = 100  # Update the health bar                 -------
            print("Don't worry! There are still dinos in your herd!")
            print(f"The next dino up to bat is: {self.user_dinosaur.type}")
            self.taunt = False
            self.current_robot_opponent.health = 100  # Update the health bar                 -------
            self.show_dino_opponent_options(self.current_robot_opponent, self.taunt)

        #  The dinosaur's health is less than or equal to 0, END GAME
        elif self.user_dinosaur.health <= 0 and self.dino_herd[self.user_current_position + 1].type == "EndGame":
            print("\nLooks like you you're out of dinosaurs, bud! Try again next time.")
            self.winner = "Robots"
            self.display_winners()
    # endregion

    # region Helper method for dino_turn(self, robot_or_dino_opponent, number) - Scratch
    def dino_option_two(self, opponent):
        print(f"{self.user_dinosaur.type} attacked with scratch!\n")  # Print the type of attack
        random_damage = random.randint(0, 30)  # The damage will be any number between 0 and 30
        opponent.injury(random_damage)  # Injure the robot
        #  Set the incoming robot_or_dino opponent object = to the current robot fighting
        self.current_robot_opponent = opponent  # Assign to correct opponent object

        #  If the robots health and the dinosaur's health are both above 0, keep playing
        if self.current_robot_opponent.health > 0 and self.user_dinosaur.health > 0:
            #  If the dino health and robot health are both above 0, and the user chooses num 1:
            print(f"Now, {opponent.name} has only "
                  f"{opponent.health} health!")  # Robot health
            print(f"It's now {opponent.name}'s turn to"
                  f" attack!")  # Robot turn to attack
            opponent.attack(self.user_dinosaur)  # Robot attack (automatic)
            #  Outcome of last robot attack on dino
            print(f"{self.user_dinosaur.type}'s current health is: {self.user_dinosaur.health}")
            if self.taunt == True:
                self.taunt = False
                self.show_dino_opponent_options(self.current_robot_opponent, self.taunt)
            else:
                # self.taunt is already False, no change necessary
                self.show_dino_opponent_options(self.current_robot_opponent, self.taunt)

        #  The opponent's health is less than or equal to 0:
        elif self.current_robot_opponent.health <= 0 and self.user_dinosaur.health > 0:
            #  Notify the user that the robot is destroyed and find the next one.
            print("The robot has been destroyed! On to the next one!")
            self.opponent_current_position = self.opponent_current_position + 1  # Get the next position

            #  Create a new robot contender, only if the current position is less than the size of fleet
            if self.opponent_current_position < len(self.robot_fleet) \
                    and self.robot_fleet[self.opponent_current_position].name != "EndGame":
                new_robot_fighter = self.new_robot_opponent(self.opponent_current_position)
                self.taunt = False  # Update the taunt to False
                self.user_dinosaur.health = 25  # Update the health bar                 -------
                self.show_dino_opponent_options(new_robot_fighter, self.taunt)  # Pass the variables in
            elif self.robot_fleet[self.opponent_current_position].name == "EndGame":
                print("\nIt looks like all the robots have been annihilated!")
                self.winner = "Dinosaurs"
                self.display_winners()

        #  The dinosaur's health is less than or equal to 0, and there are still dinosaurs in the herd
        elif self.user_dinosaur.health <= 0 and self.dino_herd[self.user_current_position + 1].type != "EndGame":
            print(f"It appears that {self.dino_herd[self.user_current_position].type} has fallen!")
            self.user_current_position = self.user_current_position + 1
            self.user_dinosaur = self.dino_herd[self.user_current_position]
            self.user_dinosaur.health = 100  # Update the health bar                 -------
            print("Don't worry! There are still dinos in your herd!")
            print(f"The next dino up to bat is: {self.user_dinosaur.type}")
            self.taunt = False
            self.current_robot_opponent.health = 100  # Update the health bar                 -------
            self.show_dino_opponent_options(self.current_robot_opponent, self.taunt)

        #  The dinosaur's health is less than or equal to 0, END GAME
        elif self.user_dinosaur.health <= 0 and self.dino_herd[self.user_current_position + 1].type == "EndGame":
            print("\nLooks like you you're out of dinosaurs, bud! Try again next time.")
            self.winner = "Robots"
            self.display_winners()
    # endregion

    # region New Robot Fleet()
    def new_robot_opponent(self, position):
        result_robot = Robot("")
        new_robot_fleet = Fleet().create_fleet()
        for robot_pos in range(0, len(new_robot_fleet)):
            if robot_pos == position:
                print("\n" + new_robot_fleet[robot_pos].name + "\n")
                #  Set the initial robot opponent against the dino contender
                result_robot = new_robot_fleet[robot_pos]
                break
        return result_robot  # Returns the robot next in line

    # endregion

    # region New Dinosaur Herd()
    def new_dino_opponent(self, position):
        result_dino = Dinosaur("", 0)
        new_dino_herd = Herd().create_herd()
        for dino_pos in range(0, len(new_dino_herd)):
            if dino_pos == position:
                print("\n" + new_dino_herd[dino_pos].type + "\n")
                #  Set the initial dino opponent against the robot contender
                result_dino = new_dino_herd[dino_pos]
                break
        return result_dino  # Returns the dino next in line

    # endregion

    # region Display_Winners
    def display_winners(self):
        the_winner = f"The winner of the Robot vs Dinosaurs game is: {self.winner}\n" \
                     f"\n\nFeel free to try the game again to see if you get another \n" \
                     f"outcome!"
        print(f"{the_winner}\n\nEND GAME")
    # endregion

# endregion
