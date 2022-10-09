"""
Store the default values and level up modifiers so that the Emojimon class
can either recreate the latest state of a Trainer's Emojimon or create a brand new Emojimon.
This is the base calculation layer.
"""

# import statements go here
import random
from emojimon_interface import EmojimonInterface

__author__ = "Huy Anh Nguyen" # Insert your name here if you're writing the initial code
__maintainer__ = "" # Insert your name here if you're fixing bugs or make improvements


SUM_DEF_STATS = 24  # The total number of points that can be distributed across each key in the default_stats dictionary.
SUM_LEV_UP_MOD = 7 # The total number of points that can be distributed across each key in the level_up_modifiers dictionary.

class EmojimonBase (EmojimonInterface):
	"""Store the default values and its own default level up modifiers"""
	# If EmojimonBase is supposed to be the only class whose instances' data are stored on the database,
	# should id be here instead of in the EmojimonInterface?
		
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
		super().__init__()
		self._id = id
		if not random and not id:
			raise ValueError('If random is set to false, data must be a non-empty json string')
		if random:
			self.default_stats = self.get_stats()
			self.level_up_modifiers = self.get_modifiers()
			self.random_gen(self.default_stats, total=SUM_DEF_STATS)
			self.random_gen(self.level_up_modifiers, total=SUM_LEV_UP_MOD)
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
		"""
		dict_len = len(val_dict)
		keys_list = list(val_dict.keys())
		# Ensure no bias like the one in Monty Hall Problem. 
		# The algorithm used to ensure uniform distribution as much as possible.
		# It is based on this StackOverflow link:
		# https://stackoverflow.com/questions/8064629/random-numbers-that-add-to-100-matlab/8068956#8068956
		random.shuffle(keys_list)
		if total - dict_len < dict_len:
			results = [0] + [round(random.uniform(0, total - dict_len), 2) for i in range(dict_len - 1)] + [total - dict_len]
		else:
			results = [0] + [random.randint(0, total - dict_len) for i in range(dict_len - 1)] + [total - dict_len] 
		results.sort()
		for i in range(1, len(results)):
			val_dict[list(val_dict.keys())[i-1]] = 1 + results[i] - results[i-1] 


	def fetch_emojimon(self):
		"""
		Fetch the BaseEmojimon instance's data from the database
		"""
		pass

def main(): 
	"""Main driver code for testing"""
	rando = EmojimonBase(id=0, random=True)
	print(rando.default_stats)
	print(rando.level_up_modifiers)


if __name__ == "__main__":
	"""Runs when specifically called from command line"""
	main()