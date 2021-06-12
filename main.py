from battlefield import BattleField
from dinosaur import Dinosaur
from robot import Robot

new_game = BattleField()
new_game.run_game()

print("\n*******************************************************\n")

dino_one = Dinosaur("Raptor", 80)
robot_one = Robot("Lightning-One")

print(f"The dino's current health is {dino_one.get_health()}")
print(f"The robot's current health is {robot_one.get_health()}")



