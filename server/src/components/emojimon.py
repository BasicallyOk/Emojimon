import json
import random
import copy
from utils import Utils


class Emojimon:
	"""
	The class for Emojimon, handles everything in relation to an emoji
	"""
	# Elemental type and identification
	# TODO: make elements a list in database and this be the index instead, keep it consistent
	el_type = "default"
	_id = 0  # All emojis should have id higher than 1, this is simply the default

	# Default stat for an emojimon
	hp = 1
	attack = 1
	sp_attack = 1
	defense = 1
	sp_defense = 1
	speed = 1

	# Default improvement stats
	hp_improv = 1
	attack_improv = 1
	sp_attack_improv = 1
	defense_improv = 1
	sp_defense_improv = 1
	speed_improv = 1

	# Experience point and evolutionary stats
	level = 1
	xp_requirement = 100
	# This means you need 100 more xp to level up, must be handled in a level up function
	xp_remaining = 100
	evolve_lvl = 100
	# This is the id of the emojimon this one will evolve to. It should evolve to the next emojidex id, but just in case
	evolve_to = 0  # 0 means no evolution

	# Evolutionary stats for xp requirement for level up
	xp_mult = 1.5  # This will mean xp_remaining will increase by 1.5 every single level up

	# Dictionary whose key-value correspond to level and the list of moves that reaching that level unlocks
	move_unlock = {} # TODO: add default moves once that is ready
	# List of moves that this emojimon can use (stored by id)
	move_pool = [] 
	# List of moves that is currently being used (locked to 4 moves) (stored by id)
	move_list = []

	def __init__(self, random: bool, id: int):
		"""
		Constructor
		Parameter:
			random (bool): whether or not we want to generate this randomly. 
				Needs to be here since Python does not allow for constructor overloading
			data (str): a json object that will be converted back into an emojimon
		"""
		if not id and not random:
			raise ValueError(
				'If random is set to false, data must be a non-empty json string')

		if random:
			self.random_gen()
			self._id = id
			self.evolve_to += 1
		else:
			pass

	def fetch_emojimon(self, id: int):
		"""
		Fetch emojimon object from the database, for now it will be a local json document
		Parameter: 
			id (int): emojidex id of the emoji
		"""
		pass

	def random_gen(self):
		element_types = ['earth', 'air', 'fire', 'nature', 'ice', 'water']

		# Randomize element type
		self.el_type = random.choice(element_types)

		# Emojimon Stat
		self.hp = random.randint(1, 20)
		self.attack = random.randint(1, 20)
		self.sp_attack = random.randint(1, 20)
		self.defense = random.randint(1, 20)
		self.sp_defense = random.randint(1, 20)
		self.speed = random.randint(1, 20)

		# Emojimon improvement stats
		self.hp_improv = random.uniform(1, 2)
		self.attack_improv = random.uniform(1, 2)
		self.sp_attack_improv = random.uniform(1, 2)
		self.defense_improv = random.uniform(1, 2)
		self.sp_defense_improv = random.uniform(1, 2)
		self.speed_improv = random.uniform(1, 2)

		# XP_mult randomizer
		self.xp_mult = random.uniform(1.3, 2)

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
	
	def convert_python(self, json_file):
		"""
		converts json objects to python objects
		"""
		
		data= json.load(open(json_file, "rt"))
		
		for key in data:
			self.__dict__[key] = data[key]


def main():
	"""
	Main function
	"""
	emojimon = Emojimon(random=True, id=0)
	print(emojimon.__dict__)
	Utils.json_encoder(emojimon)


if __name__ == '__main__':
	main()
