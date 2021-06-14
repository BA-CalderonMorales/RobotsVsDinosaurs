from dinosaur import Dinosaur

# region Herd class
class Herd:
    # region Constructor
    def __init__(self):
        self.dinosaurs = self.create_herd()
    # endregion

    # region Create_Herd
    def create_herd(self):
        """Create herd of dinosaurs"""
        herd_of_dinos = list()
        all_types = ["Raptor", "Triceratops", "Tyrannosaurus", "Spinosaurus"]
        power_level = [80, 85, 90, 100]
        for index in range(0, len(all_types)):
            herd_of_dinos.append(Dinosaur(all_types[index], power_level[index]))
        return herd_of_dinos
    # endregion

    # region Create String
    def __str__(self):
        result = ""
        for index in self.dinosaurs:
            result += f"{index.type}\n"
        return result
    # endregion
# endregion