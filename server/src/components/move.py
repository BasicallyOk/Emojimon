import json
import random
import emojimon

# TO-DO: Name generatpr for the move. Probably gonna have a JSON file to store the move....
#           Add the functions to add the move in the Emojimon class


class Move:
    """A baseline class for an Emojimon's Move Card."""
    # Attack types and identification
    attk_type = "default"   # Physical or Emotional. Maybe Emotional Level Mechanics like in Ruina?
    _id = 0     # Like emojimon, this is just the default.

    # Basic stats for a move class
    name = ""
    speed = 0
    attk_pw = 0
    fp = 0  # the number of times you can use an Emotional Move

    def __init__(self, random: bool, id: int):
        """
            Initializes the arguments for an Emojimon's Move, whose data acquired using its id value in the database
            Parameters:
                random (bool): whether or not we want to generate this randomly.
                Needs to be here since Python does not allow constructor overloading
                id (int): the index of the Move in the database that leads to a JSON object
        """
        if not random and not int:
            raise ValueError('if random is set to false, then the id value must be set to the default value of 0')

        if random:
            self.random_gen()
            self._id = id

    def random_gen(self):
        """
            Randomly generate everything in the move stats, including its name
        """
        self.name = self._name_gen()
        self.speed = random.randint(1, 6)   # Follow the average Ruina speed dice....
        self.attk_pw = random.randint(0, 5)
        self.attk_type = random.choice(['physical', 'emotional'])
        if self.attk_type == 'emotional':
            self.fp = random.randint(1, 5)

    def _name_gen(self):
        """
            Randomly generate the name of the move
        """
        FILE_PATH = "move_names.json"
        result = ""
        with open(FILE_PATH) as f:
            choices = json.load(f)
        return result