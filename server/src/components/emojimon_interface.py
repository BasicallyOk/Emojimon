"""
Emojimon interface class to abstract base_emojimon and instance_emojimon
"""

# import statements go here

__author__ = "Khoa Nguyen" # Insert your name here if you're writing the initial code
__maintainer__ = "" # Insert your name here if you're fixing bugs or make improvements

class EmojimonInterface:
	"""The interface class"""

	# Define class attributes 
	_id = 0 # In the case of Base_Emojimon, emojidex id

	# Elemental type and identification
	# TODO: make elements a list in database and this be the index instead, keep it consistent
	element_type = "Normal"

	# Emojimon stats, will mean different things depending on which class it is
	# Each stat's minimum is 1
	# All stats must sum up to 24
	attack = 4
	special_attack = 4
	defense = 4
	special_defense = 4
	speed = 4
	hp = 4

	# Evolution stats
	evolve_to = None
	evolve_requirement = 100

	# Misc stats
	move_pool = []

	def get_id(self) -> int:
		return self._id

	def get_stats(self) -> dict:
		"""
		Getter function for stats

		Returns:
			Return a dictionary with key-value pair being stat-stat value
		"""
		return {
			"attack": self.attack,
			"special_attack": self.special_attack,
			"defense": self.defense,
			"special_defense": self.special_defense,
			"speed": self.speed,
			"hp": self.hp
		}

	def get_move_pool(self) -> list:
		"""
		Getter function for move pool
		Since the list will be passed as reference here, the move pool
		can be set directly using the returned list

		Returns:
			Return the move pool
		"""
		return self.move_pool

	def add_move(self, id):
		"""
		Add a move to move pool.
		Returns nothing.
		TODO: Implement move querying
		"""
		pass

	def get_emoji_type(self):
		"""
		A function that returns a list of the Emoji's one or two types as a list
		TODO: make the types a list in the first place

		Returns:
			Return the types as a list
		"""
		typeList = [self.emojiType1, self.emojiType2]
		return typeList

	def from_json(self, json_obj):
		"""
		converts json objects to python objects
		TODO: Can probably be done better
		"""
		
		for key in json_obj:
			self.__dict__[key] = json_obj[key]
		pass


def main(): 
    """Main driver code for testing"""
    pass


if __name__ == "__main__":
    """Runs when specifically called from command line"""
    main()