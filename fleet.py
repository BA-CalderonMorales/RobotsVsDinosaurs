from robot import Robot

# region Fleet class
class Fleet:
    # region Constructor
    def __init__(self):
        self.robots = self.create_fleet()
    # endregion

    # region Create_Fleet
    def create_fleet(self):
        """Create the fleet of robots"""
        fleet_of_robots = list()
        all_names = ["Lightning", "Heafty", "Omega", "Zulu"]
        for index in range(0, len(all_names)):
            fleet_of_robots.append(Robot(all_names[index]))
        return fleet_of_robots
    # endregion

    # region Create String
    def __str__(self):
        result = ""
        for index in self.robots:
            result += f"{index.name}\n"
        return result
    # endregion
# endregion