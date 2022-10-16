"""
Store the specific instance of an Emojimon based on a base Emojimon class
"""

# import statements go here
import random
import string
from emojimon_interface import EmojimonInterface
from emojimon_base import EmojimonBase
from utils import Utils

__author__ = "Khoa Nguyen, Connor Killingbeck" # Insert your name here if you're writing the initial code
__maintainer__ = "" # Insert your name here if you're fixing bugs or make improvements

SUM_LEV_UP_MOD = 7 # The total number of points that can be distributed across each key in the level_up_modifiers dictionary.

class Emojimon (EmojimonInterface):
	"""
	The class for Emojimon instance, handles everything in relation to a caught emoji
	"""
	
	emojidex_id = 0  # The id of the associated emojimon

	# Level up modifiers, must add up to 7
	attack_mod = 1.2
	special_attack_mod = 1.2
	defense_mod = 1.2
	special_defense_mod = 1.2
	speed_mod = 1
	hp_mod = 1.2

	# Experience point and evolutionary stats
	level = 1

	base_xp_requirement = 100
	# This means you need 100 more xp to level up, must be handled in a level up function
	xp_remaining = 100

	# Evolutionary stats for xp requirement for level up
	# xp_mult = 1.5  # This will mean xp_remaining will increase by 1.5 every single level up

	# Dictionary whose key-value correspond to level and the list of moves that reaching that level unlocks
	move_unlock = {} # TODO: add default moves once that is ready

	# List of moves that is currently being used (locked to 4 moves) (stored by id)
	move_list = []

	def __init__(self, emojidex_id: int, random: bool, json_obj:string=None):
		"""
		Constructor
		TODO: more input validation
		Parameter:
			random (bool): whether or not we want to generate this randomly. 
				Needs to be here since Python does not allow for constructor overloading
			json_obj (string): the json object to 
			emojidex_id (int): the id of the emojidex
		"""
		super().__init__()

		if not random and not json_obj:
			raise ValueError(
				'If random is set to false, data must be a non-empty json string')

		if random:
			self.random_gen(SUM_LEV_UP_MOD)
			self._id = emojidex_id
			self.emojidex_id = emojidex_id
			self.recalculate_stats()
			#TODO: randomizing evolution
		else:
			# TODO: parse
			self.from_json(json_obj) 

	def fetch_emojimon(self, id: int):
		"""
		Fetch emojimon object from the database, for now it will be a local json document
		Parameter: 
			id (int): emojidex id of the emoji
		"""
		pass

	def recalculate_stats(self):
		"""
		Recalculate the stats of the emojimon based on the modifiers of the instance and base stats
		Returns: 
			dictionary storing the stats
		"""
		base_emojimon = EmojimonBase(self.emojidex_id, False)
		self.attack = base_emojimon.attack * pow(self.attack_mod, self.level/20)
		self.special_attack = base_emojimon.special_attack * pow(self.special_attack_mod, self.level/20)
		self.defense = base_emojimon.defense * pow(self.defense_mod, self.level/20)
		self.special_defense = base_emojimon.special_defense * pow(self.special_defense_mod, self.level/20)
		self.speed = base_emojimon.speed * pow(self.speed_mod, self.level/20)
		self.hp = base_emojimon.hp * pow(self.hp_mod, self.level/20)
		return self.get_stats()

	def random_gen(self, total: int):
		"""
		Generate random stats for the default_stats dictionary and the level_up_modifiers.
		All values start with 1, and the rest of the scores will be randomly distributed across the keys' values.
	
		Keyword Arguments:
			stat_mod_dict (dict) -- the dictionary with key being strings and values being either an int or float.
			total (dict) -- the total sum of values the dictionary must have.
		"""
		# TODO: dual-types?
		types = ["Normal", "Robot", "Ninja", "Fire", "Water", "Dinosaur", "Earth", "Sound", "Wind", "Darkness", "Light", "Plasma", "Solar", "Lunar", "Meme", "Magic"]

		# Randomize element type
		self.element_type = random.choice(types)

		stat_mod_dict = self.get_modifiers()
		
		dict_len = len(stat_mod_dict)
		keys_list = list(stat_mod_dict.keys())
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
			stat_mod_dict[list(stat_mod_dict.keys())[i-1]] = 1 + results[i] - results[i-1]

		#TODO refactor
		self.attack_mod = stat_mod_dict["attack_mod"]
		self.defense_mod = stat_mod_dict["defense_mod"]
		self.special_attack_mod = stat_mod_dict["special_attack_mod"]
		self.special_defense_mod = stat_mod_dict["special_defense_mod"]
		self.speed_mod = stat_mod_dict["speed_mod"]
		self.hp_mod = stat_mod_dict["hp_mod"]

	def get_modifiers(self) -> dict:
		"""
		Getter function for modifiers

		Returns:
			Return a dictionary with key-value pair being modifier-modifier value
		"""
		return {
			"attack_mod": self.attack_mod,
			"special_attack_mod": self.special_attack_mod,
			"defense_mod": self.defense_mod,
			"special_defense_mod": self.special_defense_mod,
			"speed_mod": self.speed_mod,
			"hp_mod": self.hp_mod
		}

	def add_xp(self, xp_gained: int):
		"""
		Handles adding xp to an emoji, if the emoji receives enough xp it will also level up and potentially evolve
		Parameter:
			xp_gained (int): The amount of xp gained by this emojimon
		"""
		self.xp_remaining -= xp_gained
		if self.xp_remaining <= 0:
			self.level_up_handler()
			self.xp_remaining = self.xp_requirement * self.xp_mult + self.xp_remaining

	def level_up_handler(self):
		"""
		Handles leveling 
		"""
		self.level += 1
		if self.level == self.evolve_lvl:
			self.evolve_handler()

	def evolve_handler(self):
		pass

	def get_move_list(self):
		return self.move_list

	def learn_move(self, move_id: int):
		"""
		Adds a move to the move list of the emojimon
		Some items can allow you to learn moves that is not part of the move_unlock
		Parameter:
			move_id (int): The id of the move to be added
		"""
		self.move_list.append(move_id)
		if len(self.move_list) > 4:
			self.move_list.pop(0)

	def check_for_move_unlock(self):
		"""
		Learn moves that are unlocked at the current level
		Fairly inefficient, is there a better way?
		"""
		if self.level in self.move_unlock:
			for move in self.move_unlock[self.level]:
				if move not in self.move_list:
					self.move_list.append(move)

	def get_id(self):
		"""
		Getter method for returning the id of the Emojimon object.
		"""
		return self._id

	def get_info(self):
		"""
		Getter method for getting the information needed to apply to move effect scaling
		"""
		info_dict = {
			"hp": self.hp,
			"attack": self.attack,
			"sp_attack": self.sp_attack,
			"defense": self.defense,
			"sp_defense": self.sp_defense,
			"speed": self.speed,
		}
		return info_dict


def main():
	"""
	Main function
	"""
	emojimon = Emojimon(emojidex_id=69, random=True)
	print(emojimon.__dict__)


if __name__ == '__main__':
	main()
