"""
Store the default values and level up modifiers so that the Emojimon class
can either recreate the latest state of a Trainer's Emojimon or create a brand new Emojimon.
"""

# import statements go here
from Emojimon.emojimon_interface import EmojimonInterface

__author__ = "Huy Anh Nguyen" # Insert your name here if you're writing the initial code
__maintainer__ = "" # Insert your name here if you're fixing bugs or make improvements

class EmojimonBase (EmojimonInterface):
    """Store the default values and its own default level up modifiers"""
    # If EmojimonBase is supposed to be the only class whose instances' data are stored on the database,
    # should id be here instead of in the EmojimonInterface?
    
    # Define class attributes 
    default_stats = {
        "attack": 1,
        "special_attack": 1,
        "defense": 1,
        "special_defense": 1,
        "speed": 1,
        "hp": 1
        }   # Default stats for the Emojimon. The sum of all of the values of the keys has to be a constant number.
    level_up_modifiers = {
        "attack": 1,
        "special_attack": 1,
        "defense": 1,
        "special_defense": 1,
        "speed": 1,
        "hp": 1 
    }       # Default level up modifiers for the Emojimon to apply multiplicatively on the default_stats.
            # The sum of all the values of the keys has to be a constant number.
    sum_def_stats = 24  # The total number of points that can be distributed across each key in the default_stats dictionary.
    sum_lev_up_mods = 7 # The total number of points that can be distributed across each key in the level_up_modifiers dictionary.

    def __init__(self, id: int, random: bool):
        """
        Initialize the attributes and will either fetch the data of an existing Emojimon or
        create a new one dependent on the value of the <random> flag.
        
        Keyword arguments:
            id (int) -- the identifier for the EmojimonBase instance in the database. 0 is false.
            random (bool) -- whether we should create a brand new Emojimon in the database.

        Returns:
            If anything is returned, describe it here
        """
        super.__init__()
        self._id = id
        if not random and not id:
            raise ValueError('If random is set to false, data must be a non-empty json string')
        if random:
            pass
        else:
            self.fetch_emojimon()
            pass

    def random_gen(self, val_dict: dict, total: int):
        """
        Generate random stats for the default_stats dictionary and the level_up_modifiers.
        All values start with 1, and the rest of the scores will be randomly distributed across the keys' values.
    
        Keyword Arguments:
            val_dict (dict) -- the dictionary with key being strings and values being either an int or float.
            total (dict) -- the total sum of values the dictionary must have.

        Returns
            a dictionary of keys with changed values
        """
        if_decimal = False
        difference = total
        dict_len = len(val_dict)
        if (total - len(dict_len) < len(dict_len)):
            if_decimal = True

        for key in val_dict.keys():
            if if_decimal:
                # if decimal => use random.decimal. if not, use random.randint.
                # Subtract the result from the left, and use that left to find the upperbound for random for 
                # next key.
                pass
        pass

    def fetch_emojimon(self):
        """
        Fetch the BaseEmojimon instance's data from the database
        """
        pass

    def attr_func(self, param1: int):
        """
        Give short description of what the function does, plus a short summary of how.
        This is just a constructor so we can keep it short.
        Keyword arguments are of EXTREME IMPORTANCE. Code readability starts here.

        Keyword arguments:
            param1 (int) -- give description of what this is, as well as what it should include

        Returns:
            If anything is returned, describe it here
        """
        pass


def main(): 
    """Main driver code for testing"""
    pass


if __name__ == "__main__":
    """Runs when specifically called from command line"""
    main()