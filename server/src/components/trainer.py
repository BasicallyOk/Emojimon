"""
Trainer is a class that represents a player character.
Handles anything with regards to player management, including storing emojis and transferring them.
"""

from emojimon import Emojimon
from utils import Utils

__author__ = "Khoa Nguyen" # Insert your name here if you're writing the initial code
__maintainer__ = "Khoa Nguyen" # Insert your name here if you're fixing bugs or make improvements

class Trainer:
    emojis=[] # All owned emojis
    emoji_team=[] # Can only have 4 at a time. Emojis used for battle.

    def __init__(id:int=None, save:bool=(not id)):
        """
        Constructor for Trainer

        Keyword arguments:
        id -- the id of the trainer if they already exist in the db. Defaulted to None.
        save -- whether we should create the trainer in db. Default to True if id is None.
        """
        if not id: # Generate random trainer, then push to db
            pass
        else: # Fetch trainer from db
            if type(id) is not int:
                # Make sure argument type is valid
                raise Exception('Trainer constructor requires an integer ID')

            Utils.fetch_from_db('trainers', id)
        pass

    
    def add_emojis(self, *ids):
        """
        Add emojis to the list of owned emojis
        Keyword arguments:
            *ids (List<int>) -- Arbitrary list of emoji ids to add to collection  
        """
        for id in ids:
            if type(id) is not int:
                raise Exception('Trainer.add_emojis() requires a list of integer ids. Invalid id type given: ' + type(id))
            self.emojis.append(Emojimon(False, id))


def main(): 
    """Main driver code for testing"""
    pass


if __name__ == "__main__":
    """Runs when specifically called from command line"""
    main()