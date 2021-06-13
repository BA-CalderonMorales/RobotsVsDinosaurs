import fleet
import herd
from battlefield import BattleField
from dinosaur import Dinosaur
from robot import Robot

new_game = BattleField() # Creates a new instance of the game
new_game.run_game() # Runs the game

print("\n*******************************************************\n")

# region Proper Instantiation - Dinosaur, Weapon, and Robot classes
"""
As a developer, I want to instantiate three Robot objects and three
Dinosaur objects and assign the appropriate values to all objects
"""

""" 
Please uncomment the big, multiline comment within this region
After uncommenting the code, please comment out the code so as
to let the main game at the end of the game function properly.
Do this with the rest of the regions until you reach the game, 
where the game you can just run and play in the console.
"""

"""

dino_one = Dinosaur("Raptor", 80)
robot_one = Robot("Lightning")

dino_two = Dinosaur("Triceratops", 90)
robot_two = Robot("Heavy")

dino_three = Dinosaur("Tyrannosaurus", 100)
robot_three = Robot("Omega")

print(f"The {dino_one.type}'s current health is {dino_one.get_health()}")
print(f"{robot_one.name}'s current health is {robot_one.get_health()}")

print(f"The {dino_two.type}'s current health is {dino_two.get_health()}")
print(f"{robot_two.name}'s current health is {robot_two.get_health()}")

print(f"The {dino_three.type}'s current health is {dino_three.get_health()}")
print(f"{robot_three.name}'s current health is {robot_three.get_health()}")


print("\n*******************************************************\n")

print(f"{dino_one.type} decides to attack {robot_one.name}!")
dino_one.attack(robot_one)
print(f"After an attack by {dino_one.type}, {robot_one.name} has this much health: {robot_one.get_health()}")

print("\n*******************************************************\n")

print(f"{robot_one.name} decides to attack {dino_one.type}!")
robot_one.attack(dino_one)
print(f"After an attack by {robot_one.name}, {dino_one.type} has this much health: {dino_one.get_health()}")

print("\n*******************************************************\n")

print(f"{robot_one.name}'s current weapon is: {robot_one.weapon.type}")
print(f"{robot_one.name} has a weapon power level of: {robot_one.weapon.power}")

"""
# endregion

# region Proper Instantiation - Fleet and Herd classes
"""
You can see what the fleets and herds will be made up of by 
uncommenting the content below
"""

"""
fleet_one = fleet.Fleet()
print(fleet_one)

herd_one = herd.Herd()
print(herd_one)
"""

# endregion

# region Proper Instantiation - Battlefield
"""
In this region, you can see how I've set up all the 
game components regarding how everything is suppose
to play out in a game level. Currently, the game
is running on one level. 
"""

""" 
Uncomment the content below to see what each component
of the game is suppose to do.
"""




# endregion

