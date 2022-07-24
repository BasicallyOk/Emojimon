import json
import random
from emojimon import Emojimon

# TO-DO: Maybe in the future, do sth with the API from Wordnik in generating random moves name?
#        It states that it can even provide synonyms and antonyms of a word so it seems promising....


class Move:
  """A baseline class for an Emojimon's Move Card."""
  emoji = None
  # Attack types and identification
  attk_type = "default"   # Physical or Emotional. Maybe Emotional Level Mechanics like in Ruina?
  _id = 0     # Like its counterpart in the Emojimon class, this is just the default value.

  # Basic stats for a move class.
  name = ""
  speed = 0
  attk_pw = 0
  fp = 0  # the number of times you can use an Emotional Move, a.k.a Focus Points

  def __init__(self, random: bool, id: int, owner: Emojimon):
    """
    Initializes the arguments for an Emojimon's Move, whose data acquired using its id value in the database
    Parameters:
      random (bool): whether or not we want to generate this randomly.
      Needs to be here since Python does not allow constructor overloading
      id (int): the index of the Move in the database that leads to a JSON object
      owner (Emojimon): The reference to the emoji that owns this move.
                      This is a composition relationship between an Emojimon object and a Move object.
    """
    if not random and not int:
      raise ValueError('if random is set to false, then the id value must be set to the default value of 0')

    if random:
      self.random_gen()
      self._id = id
    else:
      pass
    self.emoji = owner

  def random_gen(self):
    """
    Randomly generate everything in the move stats, including its name
    """
    self._name_gen()
    self.speed = random.randint(1, 6)   # All ranges here are balanced using eyeballs and hopes. And wishes.
    self.attk_pw = random.randint(0, 5)
    self.attk_type = random.choice(['physical', 'emotional'])
    if self.attk_type == 'emotional':
      self.fp = random.randint(1, 5)

  def _name_gen(self):
    """
    Randomly generate the name of the move
    """
    FILE_PATH = "move_names.json"
    # This is band-aid solution currently used for generating random move name based on the emoji's elements.
    # If possible, the keys in the json file would be the index of the elemental types instead in the future.
    # Or using an online dictionary API...
    with open(FILE_PATH) as f:
      words = json.load(f)
      self.name = f"{random.choice(words[self.emoji.el_type])} {random.choice(words['nouns'])}"
